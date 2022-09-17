"""
Generate text starting with word sampled from Wikitext-2 vocabulary (33278 words)
"""
import argparse
import torch

import data

DEVICE = torch.device('cpu')


def parse_args():
    parser = argparse.ArgumentParser(description='PyTorch Wikitext-2 Language Model Generator')

    parser.add_argument('--data', type=str, default='./data/wikitext-2',
                        help='location of the data corpus')
    parser.add_argument('--checkpoint', type=str, default='./model.pt',
                        help='Model checkpoint file path to load (default: model.pt)')
    parser.add_argument('--outf', type=str, default='generated.txt',
                        help='Output file to write generated text to.')
    parser.add_argument('--words', type=int, default='1000',
                        help='Number of words to generate')
    parser.add_argument('--seed', type=int, default=1111,
                        help='random seed')
    parser.add_argument('--cuda', action='store_true',
                        help='use CUDA')
    parser.add_argument('--temperature', type=float, default=1.0,
                        help='Temperature (randomness) of generator. Must be greater than 1e-3. Larger values will increase randomness of generated text.')
    parser.add_argument('--log-interval', type=int, default=100,
                        help='reporting interval')
    parser.add_argument('--prompt', type=str, default='',
                        help='Prompt token to seed text generation. Tokens must be separated by spaces. Default = randomly selected.')
    return parser.parse_args()


def generate_word_hidden(model, vocab, input_word, hidden_tens=None, temperature=1, device=DEVICE):
    if hidden_tens is None:
        hidden_tens = model.init_hidden()
    input_tens = torch.LongTensor(
        [[corpus.dictionary.word2idx[input_word]]]).to(device)
    output_tens, hidden_tens = model(input_tens, hidden_tens)
    word_weights = output_tens.squeeze().div(temperature).exp().cpu()
    word_idx = torch.multinomial(word_weights, 1)[0]
    # if word_idx == IDX_UNK:
    #     continue
    input_tens.fill_(word_idx)
    return corpus.dictionary.idx2word[word_idx], hidden_tens


def generate_words(
        model, vocab, prompt,
        eos_words='<eos>', skip_words='<unk>', max_words=1024,
        temperature=1, seed=None):
    # IDX_UNK = dictionary.word2idx['<unk>']

    prompt_words = prompt
    if isinstance(prompt_words, str):
        prompt_words = prompt_words.split()
    output_words = []
    max_words = 1024
    hidden_tens = model.init_hidden()

    for word in prompt_words:
        unused_prediction, hidden_tens = generate_word_hidden(
            model=model, vocab=vocab, input_word=word, hidden_tens=hidden_tens)
    while word and word not in eos_words and len(output_words) < max_words:
        word, hidden_tens = generate_word_hidden(
            model=model, vocab=vocab,
            input_word=word, hidden_tens=hidden_tens,
            temperature=temperature)
        if not skip_words or word not in skip_words:
            output_words.append(word)
    return output_words


def generate_text(model, vocab, prompt, seed=1111, eos_words='<eos>', skip_words='<unk>', max_words=1024):
    words = generate_words(
        model=model, vocab=vocab, prompt=prompt,
        seed=seed, eos_word=eos_words, max_words=max_words)
    return ' '.join([w for w in words if not skip_words or w not in skip_words])


if __name__ == '__main__':
    args = parse_args()
    corpus = data.Corpus(args.data)

    token_id = corpus.dictionary(args.prompt) if args.prompt else torch.randint
    # Set the random seed manually for reproducibility.
    torch.manual_seed(args.seed)

    device = torch.device("cuda" if args.cuda else "cpu")

    with open(args.checkpoint, 'rb') as f:
        model = torch.load(f, map_location=device)
    model.eval()

    is_transformer_model = getattr(model, 'model_type') == 'Transformer'
    if not is_transformer_model:
        hidden = model.init_hidden(1)
    input = torch.randint(len(corpus.dictionary), (1, 1), dtype=torch.long).to(device)

    with open(args.outf, 'w') as outf:
        with torch.no_grad():  # don't compute or remember gradients
            for i in range(args.words):
                if is_transformer_model:
                    output = model(input, False)
                    word_weights = output[-1].squeeze().div(args.temperature).exp().cpu()
                    word_idx = torch.multinomial(word_weights, 1)[0]
                    word_tensor = torch.Tensor([[word_idx]]).long().to(device)
                    input = torch.cat([input, word_tensor], 0)
                else:
                    output, hidden = model(input, hidden)
                    word_weights = output.squeeze().div(args.temperature).exp().cpu()
                    word_idx = torch.multinomial(word_weights, 1)[0]
                    input.fill_(word_idx)

                word = corpus.dictionary.idx2word[word_idx]

                outf.write(word + ('\n' if i % 20 == 19 else ' '))

                if i % args.log_interval == 0:
                    print('| Generated {}/{} words'.format(i, args.words))
