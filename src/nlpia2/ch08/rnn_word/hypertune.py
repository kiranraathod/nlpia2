from itertools import product
import pandas as pd
import json
import jsonlines

from main import main, DEFAULT_HYPERPARAMS


def grid_search(
        hidden_size=(200,),
        epochs=(1, 12, 32),
        dropout=(0, .2, .5),
        rnn_type=tuple('RNN_TANH RNN_RELU GRU LSTM'.split()),
        lr=(.5, 2),
        num_layers=(1, 2, 3, 4, 5), **kwargs):
    hypernames = 'hidden_size epochs rnn_type dropout lr num_layers'.split()
    hypervalues = [hidden_size, epochs, rnn_type, dropout, lr, num_layers]
    hypervalues += list(kwargs.values())
    hypernames += list(kwargs.keys())
    hyperdict = dict(list(zip(hypernames, hypervalues)))
    hyperparameters_to_try = list(product(*list(hyperdict.values())))

    print(f'Running {len(hyperparameters_to_try)} experiments...')
    experiments = []
    for i, hyperparams in enumerate(hyperparameters_to_try):
        hyperparams = dict(zip(hypernames, hyperparams))
        train_kwargs = DEFAULT_HYPERPARAMS.copy()
        train_kwargs.update(hyperdict)
        train_kwargs['filename'] = (
            'model_epochs_{epochs}_rnn_type_{rnn_type}_hidden_size_{hidden_size}_batch_size_{batch_size}'
            '_bptt_{bptt}_num_layers_{num_layers}').format(**train_kwargs)
        print(json.dumps(train_kwargs, indent=4))

        results = main(**train_kwargs)

        experiments.append(results)
        with open('experiments.jsonl', 'at') as fout:
            print(json.dumps(results, indent=4))
            fout.write(json.dumps(results) + '\n')
    with open('experiments.json', 'at') as fout:
        json.dump(experiments, fout)
    return experiments


def show_best_experiments(topk=10):
    with jsonlines.open('experiments.jsonl') as fin:
        lines = list(fin)
    df = pd.DataFrame(lines)
    df.to_csv('experiments.csv')
    cols = 'rnn_type epochs lr num_layers dropout epoch_time val_loss test_loss'.split()
    print(df[cols].round(2).sort_values('test_loss').head(topk))
    return df


if __name__ == '__main__':
    experiments = grid_search()
    print(experiments)
    df = pd.DataFrame(experiments)
    print(df)
    df.to_csv('experiments.csv')
    cols = 'rnn_type epochs lr num_layers dropout epoch_time val_loss test_loss'.split()
    print(df[cols].round(2).sort_values('test_loss').head())
