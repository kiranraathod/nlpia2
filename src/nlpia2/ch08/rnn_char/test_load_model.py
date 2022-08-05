import sys
from pathlib import Path

import pandas as pd
from ch08_rnn_char_nationality import RNN, CATEGORIES, rnn
from ch08_rnn_char_nationality import print_predictions
from persistence import load_model_meta


def check_predictions(names=None, target='category', nationalities=None, categories=CATEGORIES, min_correct=.4, model=None):
    if model is None:
        model = rnn
    if names is None or nationalities is None:
        names = 'Fyodor Dostoevsky Oluwasanmi Sanmi Koyejo Satoshi Nakamoto Rediet Abebe Silvio Micali'.split()
        nationalities = ['Russian'] * 2 + ['Nigerian'] * 3 + ['Japanese'] * 2 + ['Ethiopian'] * 2 + ['Italian'] * 2

    preds = []
    for name, nationality in zip(names, nationalities):
        preds.append(print_predictions(text=name, target_col_label=target, n_predictions=1, categories=CATEGORIES, model=rnn3))

    preds = pd.concat(preds)
    preds['true_nationality'] = nationalities
    print(preds)

    num_correct = (preds['true_nationality'] == preds[target]).sum()
    portion_correct = num_correct / len(preds)
    print(f'num_correct: {num_correct}  portion_correct: {portion_correct}')
    if 0 <= min_correct <= 1:
        assert portion_correct > min_correct

    return preds


if __name__ == '__main__':
    filebase = sys.argv[1] if len(sys.argv) > 1 else 'ch08_rnn_char_nationality'

    for fp in Path(filebase).parent.glob(f'{filebase}*.meta.json'):
        filepath3 = fp.with_suffix('')
        meta3 = load_model_meta(filepath3)
        rnn3 = RNN(vocab_size=len(meta3['char2i']), n_hidden=128, n_categories=len(meta3['categories']))
        meta3 = load_model_meta(filepath3, model=rnn3)

        df = check_predictions(model=rnn3, target='category', categories=meta3['categories'])
        print(df)
