from itertools import product
import pandas as pd
from pathlib import Path
import json
import jsonlines

from main import main, DEFAULT_HYPERPARAMS


def grid_search(
        loss_name='test_loss',
        stop_improvement_fraction=0.001,
        no_improvement_count_max=5,

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
    hyperparam_ranges = dict(list(zip(hypernames, hypervalues)))
    hyperparameter_grid = list(product(*list(hyperparam_ranges.values())))
    json.dump(hyperparameter_grid, open(f'experiment_grid_{len(hyperparameter_grid)}.json', 'w'), indent=4)
    json.dump(hyperparam_ranges, open(f'experiment_plan_{len(hyperparam_ranges)}.json', 'w'), indent=4)
    df = pd.DataFrame(hyperparameter_grid, columns=list(hyperparam_ranges.keys()))
    df = df.sample(len(df))  # shuffle row order while retaining original index
    df.to_csv('experiment_grid.csv')

    best_loss = 1e6
    no_improvement_count = 0

    print(f'Running {len(hyperparameter_grid)} experiments...')
    experiments = []

    for idx, hyperparams in df.iterrows():
        train_kwargs = DEFAULT_HYPERPARAMS.copy()
        train_kwargs['id'] = idx
        train_kwargs.update(hyperparams.to_dict())
        train_kwargs['filename'] = f'model_{idx:04d}.pt'
        print(json.dumps(train_kwargs, indent=4))

        results = main(**train_kwargs)

        experiments.append(results)
        with open('experiments.jsonl', 'at') as fout:
            print(json.dumps(results, indent=4))
            fout.write(json.dumps(results) + '\n')

        improvement = best_loss - results[loss_name]
        if improvement < stop_improvement_fraction * best_loss:
            no_improvement_count += 1
            print(f'no improvement count: {no_improvement_count}')
        elif improvement > 0:
            best_loss = results[loss_name]
            no_improvement_count = 0
            print(f'NEW best_loss: {best_loss:7.3f} is {improvement * 100. / best_loss:7.3f}% improvement')

        if no_improvement_count > no_improvement_count_max:
            print(f'Stopping hyperparameter tuning at best_loss: {best_loss:7.4f}.')
            break

    with open('experiments.json', 'at') as fout:
        json.dump(experiments, fout)
    return experiments


def show_best_experiments(jsonl_path='experiments.jsonl', topk=10):
    jsonl_path = Path(jsonl_path)
    with jsonlines.open(jsonl_path) as fin:
        lines = list(fin)
    df = pd.DataFrame(lines)
    df.to_csv(jsonl_path.with_suffix('.csv'))
    cols = 'id rnn_type epochs lr num_layers dropout epoch_time val_loss test_loss'.split()
    print(df[[c for c in cols if c in df.columns]].round(2).sort_values('test_loss').head(topk))
    return df


if __name__ == '__main__':
    experiments = grid_search()
    print(experiments)
    df = pd.DataFrame(experiments)
    print(df)
    df.to_csv('experiments.csv')
    cols = 'rnn_type epochs lr num_layers dropout epoch_time val_loss test_loss'.split()
    print(df[cols].round(2).sort_values('test_loss').head())
