# coding: utf-8
import argparse
import time
import math
import os
import torch
import torch.nn as nn
import torch.onnx

import data
import model as rnn_models

DEFAULT_HYPERPARAMS = dict(
    annealing_loss_improvement_pct=1.0,
    batch_size=20, bptt=35,
    clip=0.25,
    cuda=True,
    datapath='./data/wikitext-2',
    device='',
    dropout=0.2,
    dry_run=False,
    emsize=200,
    epochs=1,
    log_interval=200,
    lr=20,
    rnn_type='LSTM',
    nhead=2,
    nhid=200,
    nlayers=2,
    onnx_export='',
    save='model.pt',
    seed=1111,
    tied=False)
"""
DEFAULT_HYPERPARAMS = dict(
    datapath='./data/wikitext-2',
    cuda=True,
    epochs=1,
    rnn_type='RNN_TANH',
    nhid=200,
    emsize=200,
    batch_size=20,
    lr=20,
    bptt=35,
    nlayers=1,
    clip=0.25,
    seed=1111,
    device='',
    dropout=0.2,
    onnx_export='',
    nhead=2,
)
"""


def parse_args():
    parser = argparse.ArgumentParser(description='PyTorch Wikitext-2 RNN/LSTM/GRU/Transformer Language Model')
    parser.add_argument('--datapath', type=str, default=DEFAULT_HYPERPARAMS['datapath'],
                        help='location of the data corpus')
    parser.add_argument('--rnn_type', type=str, default=DEFAULT_HYPERPARAMS['rnn_type'],
                        help='type of network (RNN_TANH, RNN_RELU, LSTM, GRU, Transformer)')
    parser.add_argument('--emsize', type=int, default=DEFAULT_HYPERPARAMS['emsize'],
                        help='size of word embeddings')
    parser.add_argument('--nhid', type=int, default=DEFAULT_HYPERPARAMS['nhid'],
                        help='number of hidden units per layer')
    parser.add_argument('--nlayers', type=int, default=DEFAULT_HYPERPARAMS['nlayers'],
                        help='number of layers')
    parser.add_argument('--lr', type=float, default=DEFAULT_HYPERPARAMS['lr'],
                        help='initial learning rate')
    parser.add_argument('--clip', type=float, default=DEFAULT_HYPERPARAMS['clip'],
                        help='gradient clipping')
    parser.add_argument('--epochs', type=int, default=DEFAULT_HYPERPARAMS['epochs'],
                        help='upper epoch limit')
    parser.add_argument('--batch_size', type=int, default=DEFAULT_HYPERPARAMS['batch_size'], metavar='N',
                        help='split each document into this number of independently trained batches (columns)')
    parser.add_argument('--bptt', type=int, default=DEFAULT_HYPERPARAMS['bptt'],
                        help='sequence length')
    parser.add_argument('--dropout', type=float, default=DEFAULT_HYPERPARAMS['dropout'],
                        help='dropout applied to layers (0 = no dropout)')
    parser.add_argument('--tied', action='store_true',
                        help='tie the word embedding and softmax weights')
    parser.add_argument('--seed', type=int, default=DEFAULT_HYPERPARAMS['seed'],
                        help='random seed')
    parser.add_argument('--device', type=str, default=DEFAULT_HYPERPARAMS['device'],
                        help='device string to use in torch.device() call')
    parser.add_argument('--cuda', action='store_true',
                        help='use CUDA')
    parser.add_argument('--log-interval', type=int, default=200, metavar='N',
                        help='report interval')
    parser.add_argument('--save', type=str, default='model.pt',
                        help='path to save the final model')
    parser.add_argument('--onnx_export', type=str, default=DEFAULT_HYPERPARAMS['onnx_export'],
                        help='path to export the final model in onnx format')
    parser.add_argument('--nhead', type=int, default=DEFAULT_HYPERPARAMS['nhead'],
                        help='the number of heads in the encoder/decoder of the transformer model')
    parser.add_argument('--dry-run', action='store_true',
                        help='verify the code and the model')
    parser.add_argument('--annealing_loss_improvement_pct', type=float, default=1.0,
                        help='For each epoch, if the loss is not smaller than this fraction of the previous best loss, the learning rate is reduced (default = 1.0).')
    args = parser.parse_args()

    return args


def main(**kwargs):
    corpus = data.Corpus(kwargs['datapath'])

    if not len(kwargs):
        kwargs = vars(parse_args())

    def batchify(dataset, batch_size=kwargs['batch_size']):
        # Starting from sequential data, batchify arranges the dataset into columns.
        # For instance, with the alphabet as the sequence and batch size 4, we'd get
        # ┌ a g m s ┐
        # │ b h n t │
        # │ c i o u │
        # │ d j p v │
        # │ e k q w │
        # └ f l r x ┘.
        # shape = (seq_len, batch_size)
        #
        # These columns are treated as independent by the model, which means that the
        # dependence of e. g. 'g' on 'f' can not be learned, but allows more efficient
        # batch processing.

        # Work out how cleanly dataset divides into batch_size (bsz) parts.
        num_segments = dataset.size(0) // batch_size
        # Trim off any extra elements that wouldn't cleanly fit (remainders).
        dataset = dataset.narrow(0, 0, num_segments * batch_size)
        # Evenly divide the data across the bsz batches.
        dataset = dataset.view(batch_size, -1).t().contiguous()
        return dataset.to(device)

    # Set the random seed manually for reproducibility.
    torch.manual_seed(kwargs['seed'])
    if torch.cuda.is_available():
        if not kwargs['cuda']:
            print("WARNING: You have a CUDA device, so you should probably run with --cuda.")

    device = kwargs['device'] or ("cuda" if kwargs['cuda'] else "cpu")
    device = torch.device(device)

    eval_batch_size = kwargs['batch_size']  # 10
    train_data = batchify(dataset=corpus.train, batch_size=kwargs['batch_size'])
    val_data = batchify(dataset=corpus.valid, batch_size=eval_batch_size)
    test_data = batchify(dataset=corpus.test, batch_size=eval_batch_size)

    # model = rnn_models.RNNModel('RNN_TANH')
    if kwargs['rnn_type'] == 'Transformer':
        model = rnn_models.TransformerModel(
            ntokens=len(corpus.dictionary), **kwargs).to(device)
    else:
        model = rnn_models.RNNModel(**kwargs).to(device)

    criterion = nn.NLLLoss()

    ###############################################################################
    # Training

    def repackage_hidden(h):
        """Wraps hidden states in new Tensors, to detach them from their history."""

        if isinstance(h, torch.Tensor):
            return h.detach()
        else:
            return tuple(repackage_hidden(v) for v in h)

    # get_batch subdivides the source data into chunks of length kwargs['bptt'].
    # If source is equal to the example output of the batchify function, with
    # a bptt-limit of 2, we'd get the following two Variables for i = 0:
    # ┌ a g m s ┐ ┌ b h n t ┐
    # └ b h n t ┘ └ c i o u ┘
    # Note that despite the name of the function, the subdivison of data is not
    # done along the batch dimension (i.e. dimension 1), since that was handled
    # by the batchify function. The chunks are along dimension 0, corresponding
    # to the seq_len dimension in the LSTM.

    def get_batch(source, i):
        seq_len = min(kwargs['bptt'], len(source) - 1 - i)
        data = source[i:i + seq_len]
        target = source[i + 1:i + 1 + seq_len].view(-1)
        return data, target

    def evaluate(data_source):
        # Turn on evaluation mode which disables dropout.
        model.eval()
        total_loss = 0.
        ntokens = len(corpus.dictionary)
        if kwargs['rnn_type'] != 'Transformer':
            hidden = model.init_hidden(eval_batch_size)
        with torch.no_grad():
            for i in range(0, data_source.size(0) - 1, kwargs['bptt']):
                data, targets = get_batch(data_source, i)
                if kwargs['rnn_type'] == 'Transformer':
                    output = model(data)
                    output = output.view(-1, ntokens)
                else:
                    output, hidden = model(data, hidden)
                    hidden = repackage_hidden(hidden)
                total_loss += len(data) * criterion(output, targets).item()
        return total_loss / (len(data_source) - 1)

    def train_epoch(model, train_data):
        # Training mode enables dropout layers
        model.train()
        total_loss = 0.
        start_time = time.time()
        ntokens = len(corpus.dictionary)
        if kwargs['rnn_type'] != 'Transformer':
            hidden = model.init_hidden(kwargs['batch_size'])
        for batch, i in enumerate(range(0, train_data.size(0) - 1, kwargs['bptt'])):
            data, targets = get_batch(train_data, i)
            # Starting each batch, we detach the hidden state from how it was previously produced.
            # If we didn't, the model would try backpropagating all the way to start of the dataset.
            model.zero_grad()
            if kwargs['rnn_type'] == 'Transformer':
                output = model(data)
                output = output.view(-1, ntokens)
            else:
                hidden = repackage_hidden(hidden)
                output, hidden = model(data, hidden)
            loss = criterion(output, targets)
            loss.backward()

            # `clip_grad_norm` helps prevent the exploding gradient problem in RNNs / LSTMs.
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.clip)
            for p in model.parameters():
                p.data.add_(p.grad, alpha=-lr)

            total_loss += loss.item()

            if batch and batch % args.log_interval == 0:
                cur_loss = total_loss / args.log_interval
                elapsed = time.time() - start_time
                print(('| epoch {:3d} | {:5d}/{:5d} batches | lr {:02.4f} | ms/batch {:5.2f} | '
                       'loss {:5.2f} | ppl {:8.2f}').format(
                    epoch, batch, len(train_data) // kwargs['bptt'], lr,
                    elapsed * 1000 / args.log_interval, cur_loss, math.exp(cur_loss)))
                total_loss = 0
                start_time = time.time()
            if args.dry_run:
                break

    def export_onnx(path, batch_size, seq_len):
        print('The model is also exported in ONNX format at {}.'.format(os.path.realpath(kwargs['onnx_export'])))
        model.eval()
        dummy_input = torch.LongTensor(seq_len * batch_size).zero_().view(-1, batch_size).to(device)
        hidden = model.init_hidden(batch_size)
        torch.onnx.export(model, (dummy_input, hidden), path)

    # Loop over epochs.
    lr = args.lr
    best_val_loss = None
    results = kwargs.copy()

    # [ctrl]-C to break out of training early and retain the latest best checkpoint (model.pt)
    try:
        epoch = 0
        epoch_time = 0
        for epoch_num in range(1, args.epochs + 1):
            epoch_start_time = time.time()
            train_epoch(model=model, train_data=train_data)
            val_loss = evaluate(val_data)
            epoch_time = time.time() - epoch_start_time
            results.update(dict(
                best_val_loss=best_val_loss,
                epoch_num=epoch_num,
                epoch_time=epoch_time,
                val_loss=val_loss,
                val_perplexity=math.exp(val_loss)))
            print('-' * 89)
            print(('| end of epoch {epoch_num:3d} | time: {epoch_time:5.2f}s | val loss {val_loss:5.2f} | '
                   'valid ppl {val_perplexity:8.2f}').format(**results))
            print('-' * 89)
            # Save the model if the validation loss is the best we've seen so far.
            if not best_val_loss or val_loss < args.annealing_loss_improvement_pct * best_val_loss:
                with open(args.save, 'wb') as f:
                    torch.save(model, f)
                best_val_loss = val_loss
            else:
                # Reduce the learning rate if no improvement has been seen in the validation dataset.
                lr /= 4

    except KeyboardInterrupt:
        print('-' * 89)
        print('Exiting from training early')

    # Load the best saved model.
    with open(args.save, 'rb') as f:
        model = torch.load(f)
        # after load the rnn params are not a continuous chunk of memory
        # this makes them a continuous chunk, and will speed up forward pass
        # Currently, only rnn model supports flatten_parameters function.
        if kwargs['rnn_type'] in ['RNN_TANH', 'RNN_RELU', 'LSTM', 'GRU']:
            model.rnn.flatten_parameters()

    # Run on test data.
    results['test_loss'] = evaluate(test_data)
    results['test_perplexity'] = evaluate(test_data)
    print('=' * 89)
    print('| End of training | test loss {test_loss:5.2f} | test ppl {test_perplexity:8.2f}'.format(
        **results))
    print('=' * 89)

    if len(kwargs['onnx_export']) > 0:
        # Export the model in ONNX format.
        export_onnx(kwargs['onnx_export'], batch_size=1, seq_len=kwargs['bptt'])

    return results


if __name__ == '__main__':
    args = parse_args()
    kwargs = vars(args)
    results = main(**kwargs)
