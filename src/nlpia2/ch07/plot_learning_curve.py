import json
import pandas as pd
from pathlib import Path

pd.options.display.max_columns = 100
pd.options.display.max_rows = 40


def best_hyperparms():
    paths = list((Path.home() / '.nlpia2-data' / 'log').glob('*'))
    df = []
    for p in paths:
        d = json.load(p.open())
        df.append({k: d.get(k) for k in d.keys() if k not in ('learning_curve', 'y_test', 'y_train')})
        df[-1]['filename'] = p.name[-12:-5]
    df = pd.DataFrame(df)
    df.sort_values('test_accuracy').round(2).tail(10).T


def learning_curve(filepath=Path.home() / '.nlpia2-data' / 'log' / 'disaster_tweets_cnn_pipeline_14728.json'):
    with Path(filepath).open() as fin:
        results = json.load(fin)

    curve = pd.DataFrame(results['learning_curve'],
                         columns=['loss', 'training_accuracy', 'test_accuracy'])
    return curve
