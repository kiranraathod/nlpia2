from itertools import product
import pandas as pd
import json

from main import main, DEFAULT_HYPERPARAMS


def grid_search(
        hidden_sizes=(200,),
        epoch_nums=(1, 12, 32),
        dropouts=(0, .2, .5),
        rnn_types=tuple('RNN_TANH RNN_RELU GRU LSTM'.split()),
        lrs=(.5, 2),
        nlayers_options=(1, 2, 3, 5),
):
    experiments = []
    for hidden_size, rnn_type, epochs, dropout, lr, nlayers in product(
            hidden_sizes, rnn_types, epoch_nums, dropouts, lrs, nlayers_options):
        kwargs = DEFAULT_HYPERPARAMS.copy()
        kwargs.update(dict(
            nhid=hidden_size,
            rnn_type=rnn_type,
            dropout=dropout,
            epochs=epochs,
            nlayers=nlayers_options,
            lr=lr))

        kwargs['filename'] = (
            'model_epochs_{epochs}_rnn_type_{rnn_type}_nhid_{nhid}_batch_size_{batch_size}'
            '_bptt_{bptt}_nlayers_{nlayers}').format(**kwargs)
        # print(
        #     ("python main.py {'--cuda' if cuda else ''} --epochs {epochs} --model_type {model_type}"
        #      " --nhid {nhid} --batch_size {batch_size} --bptt {bptt} --nlayers {nlayers} --save {filename}.pt").format(**kwargs)
        # )
        print(json.dumps(kwargs, indent=4))
        results = main(**kwargs)
        experiments.append(results)
        with open('experiments.txt', 'at') as fout:
            print(json.dumps(results, indent=4))
            fout.write(json.dumps(results) + '\n')
    with open('experiments.json', 'at') as fout:
        json.dump(fout, experiments)


if __name__ == '__main__':
    experiments = grid_search()
    print(experiments)
    df_experiments = pd.DataFrame(experiments)
    print(df_experiments)
    df_experiments.to_csv('experiments.csv')
