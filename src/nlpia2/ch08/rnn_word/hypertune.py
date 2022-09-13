from itertools import product

from main import main, DEFAULT_HYPERPARAMS


def grid_search(
        hidden_sizes=(200,),
        rnn_types=tuple('GRU LSTM RNN_TANH RNN_RELU'.split())):
    for hidden_size, rnn_type in product(hidden_sizes, rnn_types):
        kwargs = DEFAULT_HYPERPARAMS.copy()
        kwargs.update(dict(NHID=hidden_size, MODEL=rnn_type))

        kwargs['filename'] = 'model_epochs_{epochs}_model_{model}_nhid_{nhid}_batch_size_{batch_size}_bptt_{bptt}_nlayers_{nlayers}'.format(**kwargs)
        print(
            ("python main.py {'--cuda' if cuda else ''} --epochs {epochs} --model_type {model_type}"
             " --nhid {nhid} --batch_size {batch_size} --bptt {bptt} --nlayers {nlayers} --save {filename}.pt").format(**kwargs)
        )
        print(kwargs)
        main(**kwargs)


if __name__ == '__main__':
    grid_search()
