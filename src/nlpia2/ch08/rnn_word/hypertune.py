from itertools import product
import pandas as pd

from main import main, DEFAULT_HYPERPARAMS


def grid_search(
        hidden_sizes=(200,),
        rnn_types=tuple('GRU RNN_TANH RNN_RELU LSTM'.split())):
    experiments = []
    for hidden_size, rnn_type in product(hidden_sizes, rnn_types):
        kwargs = DEFAULT_HYPERPARAMS.copy()
        kwargs.update(dict(nhid=hidden_size, rnn_type=rnn_type))

        kwargs['filename'] = (
            'model_epochs_{epochs}_rnn_type_{rnn_type}_nhid_{nhid}_batch_size_{batch_size}'
            '_bptt_{bptt}_nlayers_{nlayers}').format(**kwargs)
        # print(
        #     ("python main.py {'--cuda' if cuda else ''} --epochs {epochs} --model_type {model_type}"
        #      " --nhid {nhid} --batch_size {batch_size} --bptt {bptt} --nlayers {nlayers} --save {filename}.pt").format(**kwargs)
        # )
        print(kwargs)
        results = main(**kwargs)
        experiments.append(results)
        with open('experiments.json', 'at') as fout:
            print(str(results))
            fout.write(str(results) + '\n')


if __name__ == '__main__':
    experiments = grid_search()
    df_experiments = pd.DataFrame(experiments)
    print(df_experiments)
    df_experiments.to_csv('experiments.csv')
