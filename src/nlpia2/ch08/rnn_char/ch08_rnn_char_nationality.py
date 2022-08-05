# -*- coding: utf-8 -*-
"""

    $ python predict.py Hinton
    (-0.47) Scottish
    (-1.52) English
    (-3.57) Irish

    $ python predict.py Schmidhuber
    (-0.19) German
    (-2.48) Czech
    (-2.68) Dutch
"""
from collections import Counter
import copy
from pathlib import Path
import time

import torch
import torch.nn as nn
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

from nlpia2.init import SRC_DATA_DIR, maybe_download
from nlpia2.string_normalizers import Asciifier, ASCII_NAME_CHARS

from persistence import save_model  # , load_model_meta  # noqa


class RNN(nn.Module):
    def __init__(self, vocab_size, n_hidden, n_categories):
        super(RNN, self).__init__()

        self.n_hidden = n_hidden
        self.n_categories = n_categories  # <1> n_categories = n_outputs (one-hot)

        self.i2h = nn.Linear(vocab_size + n_hidden, n_hidden)
        self.i2o = nn.Linear(vocab_size + n_hidden, n_categories)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, char_tens, hidden):  # <2> x = input = char_tens
        combined = torch.cat((char_tens, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def init_hidden(self):
        return torch.zeros(1, self.n_hidden)


MODEL_PATH = Path(__file__).with_suffix('').name

# META = load_model_meta(MODEL_PATH)

META = {
    'categories': [
        "Arabic", "Irish", "Spanish", "French", "German", "English",
        "Korean", "Vietnamese", "Scottish", "Japanese", "Polish",
        "Greek", "Czech", "Italian", "Portuguese", "Russian", "Dutch", "Chinese",
        "Indian", "Ethiopian", "Nigerian", "Nepalese",
    ],
    'char2i': {
        "g": 0, "J": 1, "j": 2, "l": 3, "X": 4, "e": 5, "L": 6, "H": 7, " ": 8,
        "'": 9, "w": 10, "O": 11, "U": 12, "E": 13, "c": 14, "F": 15, "a": 16,
        "Q": 17, "y": 18, "u": 19, "I": 20, "W": 21, ",": 22, "p": 23, "b": 24,
        "z": 25, "G": 26, "T": 27, "t": 28, "q": 29, "S": 30, "m": 31, "d": 32,
        "K": 33, "n": 34, "i": 35, "x": 36, "Y": 37, "M": 38, "R": 39, "r": 40,
        "N": 41, "-": 42, "f": 43, "Z": 44, "s": 45, "D": 46, "P": 47, "o": 48,
        ";": 49, "v": 50, "k": 51, "V": 52, "h": 53, "C": 54, "A": 55, ".": 56,
        "B": 57
    }
}
META['n_hidden'] = 128
META['n_categories'] = len(META['categories'])
META["model"] = RNN(
    len(META['char2i']),
    n_hidden=META['n_hidden'],
    n_categories=META['n_categories']
)

# save_model(MODEL_PATH, **META)


CATEGORIES = META['categories']
n_categories = META.get('n_categories', len(CATEGORIES))
assert n_categories == len(CATEGORIES)
n_hidden = META.get('n_hidden', 128)
CHAR2I = META['char2i']


# FIXME, get rid of this global rnn model
rnn = META.get('model', None)

if rnn is None:
    rnn = RNN(
        len(META['char2i']),
        n_hidden=n_hidden,
        n_categories=n_categories,
    )

if 'state_dict' in META:
    rnn.load_state_dict(META['state_dict'])


asciify = Asciifier(include=ASCII_NAME_CHARS)


def dedupe_mapping_df(df, key_column='surname', value_column='nationality'):
    key_value_tuples = list(zip(df[key_column], [value_column]))
    key_value_counts = [[k[0], k[1], v] for (k, v) in Counter(key_value_tuples).items()]
    return pd.DataFrame(key_value_counts, columns=[key_column, value_column, 'count'])


def load_names_from_text(data_dir=SRC_DATA_DIR, text_col='surname', categories=None, target='nationality', dedupe=False):
    """ load names (lines of text) from text files if filename is among categories provided

    Inputs:
      categories (list of str): None will load all categories

    Returns:
      DataFrame with columns=['surname', 'nationality', 'count']

    ```python
    !curl - O https: // download.pytorch.org / tutorial / data.zip
    !unzip data.zip
    load_names_from_text(data_dir=Path.cwd())
    ```

    >>> df = load_names_from_text(dedupe=True, categories=None)
    >>> df['category'].unique()
    >>> len(df) > 10000
    True
    >>> df2 = load_names_from_text(dedupe=False, categories=None)
    >>> len(df2) > len(df)
    21516
    >>> df['count'].sum() == len(df2)
    True
    >>> df.columns[:-1] == df2.columns
    array([ True,  True])
    """
    name_label_counts = []
    print(f"Looking for files for {len(categories or [])} categories: {categories}")
    data_dir = Path(data_dir) / 'names'
    if not data_dir.is_dir():
        data_dir = data_dir.parent
    for i, filepath in enumerate(data_dir.glob('*.txt')):
        filepath = Path(filepath)
        print(f"Loading file {i}: {filepath}.")
        category = filepath.with_suffix('').name
        if categories and category not in categories:
            print(f"The path {filepath} looks like a new {category}.")
            print(f"Add it to the {filepath.with_suffix('.meta.json')} and rerun.")
            continue
        filepath = maybe_download(filename=filepath)
        with filepath.open() as fin:
            lines = [asciify(line.rstrip()) for line in fin]
            name_label_counts += list(zip(lines, [category] * len(lines)))
    columns = [text_col, target]
    if dedupe:
        name_label_counts = [[k[0], k[1], v] for (k, v) in Counter(name_label_counts).items()]
        columns += ['count']
    return pd.DataFrame(name_label_counts, columns=columns)


def dataset_confusion(df, normalize=True, fillna='0', text_col='surname', target='nationality'):
    """ Given a df with columns name & category, assume "truth" is most popular category for a name """
    confusion = {c: Counter() for c in sorted(df[target].unique())}
    for i, g in df.groupby(text_col):
        counts = Counter(g[target])
        confusion[counts.most_common()[0][0]] += counts
    confusion = pd.DataFrame(confusion)
    confusion = confusion[confusion.index]
    if normalize:
        confusion /= confusion.sum(axis=1)
    if fillna is not None:
        confusion.fillna(fillna, inplace=True)
    confusion.index.name = 'most_common'
    return confusion


def encode_one_hot_vec(letter, char2i=CHAR2I):
    """ one - hot encode a single char """
    tensor = torch.zeros(1, len(char2i))
    tensor[0][char2i[letter]] = 1
    return tensor


def encode_one_hot_seq(line, char2i=CHAR2I):
    """ one - hot encode each char in a str = > matrix of size(len(str), len(alphabet)) """
    tensor = torch.zeros(len(line), 1, len(ASCII_NAME_CHARS))
    for pos, letter in enumerate(line):
        tensor[pos][0][char2i[letter]] = 1
    return tensor


def category_from_output(output, categories=CATEGORIES):
    top_n, top_i = output.topk(1)
    category_i = top_i[0].item()
    return categories[category_i], category_i


def output_from_str(s, char2i=CHAR2I, categories=CATEGORIES):
    """ TODO: put this in the model """
    global rnn

    inpt = encode_one_hot_seq(s, char2i=char2i)
    hidden = torch.zeros(1, n_hidden)

    output, next_hidden = rnn(inpt[0], hidden)
    print(output)

    return category_from_output(output, categories=categories)


def sample_groupby(df, num_samples=1, groupby='nationality', char2i=CHAR2I, replace=True, shuffle=True):
    """ balanced sampling of all categories """
    if sample_groupby.groups is None:
        sample_groupby.groups = df.groupby(groupby)
    df_sample = sample_groupby.groups.sample(num_samples, replace=replace)
    if shuffle:
        df_sample = df_sample.sample(len(df_sample))
    return df_sample


sample_groupby.groups = None


def random_example(groups, target='nationality', text_col='surname', categories=CATEGORIES, char2i=CHAR2I):
    """ balanced sampling of all categories """
    # ANTIPATTERN
    # random_example.df = getattr(random_example, 'df', df)
    # if 'count' not in df.columns:
    #     random_exmaple.df = dedupe_mapping_df(df)
    row = groups.sample(1).sample(1)
    name = row[text_col].iloc[0]
    category = row[target].iloc[0]
    category_tensor = torch.tensor([categories.index(category)], dtype=torch.long)
    line_tensor = encode_one_hot_seq(name, char2i=char2i)
    return category, name, category_tensor, line_tensor


def stratified_random_examples(
        groups, num_samples_per_group=1, replace=True, shuffle=True,
        target='nationality', text_col='surname', categories=CATEGORIES, char2i=CHAR2I):
    """ balanced sampling of all categories """
    df = groups.sample(num_samples_per_group, replace=replace)
    if shuffle:
        df = df.sample(len(df))
    names = df[text_col].values
    cats = df[target].values
    tqdm_fun = tqdm if len(cats) > 10000 else iter
    cat_tensors = [
        torch.tensor([categories.index(c)], dtype=torch.long) for c in
        tqdm_fun(cats)
    ]
    line_tensors = [
        encode_one_hot_seq(n, char2i=char2i) for n in tqdm_fun(names)
    ]
    return cats, names, cat_tensors, line_tensors


def train_sample(category_tensor, line_tensor, model=rnn,
                 criterion=nn.NLLLoss(), lr=.005,
                 char2i=CHAR2I, categories=CATEGORIES):
    """ train for one epoch(one batch of example tensors) """
    hidden = model.init_hidden()

    model.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = model(line_tensor[i], hidden)
    # print(f"output: {output}")
    # print(f"category_tensor: {category_tensor}")
    loss = criterion(output, category_tensor)
    # print(f"loss: {loss.item()}")
    loss.backward()

    # Add parameters' gradients to their values, multiplied by learning rate
    for p in model.parameters():
        p.data.add_(p.grad.data, alpha=-lr)

    return model, output, loss.item()


CRITERION = nn.NLLLoss()


def train_batch(df_batch, model, categories, target='nationality', text_col='surname', criterion=CRITERION, lr=.005, char2i=CHAR2I):
    """ train for one epoch(one batch of example tensors) """
    output_losses = []
    for i, row in df_batch.iterrows():
        category_tensor = torch.tensor([categories.index(row[target])], dtype=torch.long)
        line_tensor = encode_one_hot_seq(row[text_col], char2i=char2i)
        model, output, loss = train_sample(
            category_tensor,
            line_tensor,
            model=model,
            criterion=criterion,
            lr=lr,
            char2i=char2i,
            categories=categories)
        output_losses.append((output, loss))
    return model, output_losses


def time_elapsed(t0):
    """ Compute time since t0(t0=time.time() in seconds) """
    secs = time.time() - t0
    mins = secs // 60
    secs = int(secs - mins * 60)
    mins = int(mins)
    return f'{mins:02d}:{secs:02d}'


def evaluate_tensor(line_tensor, model=rnn):
    hidden = model.init_hidden()
    for i in range(line_tensor.size()[0]):
        output, hidden = model(line_tensor[i], hidden)
    return output


def predict_category(name, categories=CATEGORIES, char2i=CHAR2I, model=rnn):
    tensor = encode_one_hot_seq(name, char2i=char2i)
    pred_i = evaluate_tensor(tensor, model=model).topk(1)[1][0].item()
    return categories[pred_i]


def confusion_df(truth, pred, categories=CATEGORIES):
    """ Count mislabeled examples in entire dataset """
    pair_counts = Counter(zip(truth, pred))
    confusion = {c_tru: {c_pred: 0 for c_pred in categories} for c_tru in categories}
    for ((t, p), count) in pair_counts.items():
        confusion[t][p] = count
    return pd.DataFrame(confusion)


def predict_confusion(df, categories=CATEGORIES, target='nationality', text_col='surname'):
    df_conf = confusion_df(
        truth=df[target],
        pred=df[text_col].apply(predict_category).values,
        categories=categories,
    )
    return df_conf


def plot_confusion(df_conf):
    df_conf = df_conf.replace('', 0)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(df_conf.values)
    fig.colorbar(cax)

    ax.set_xticklabels([''] + list(df_conf.columns), rotation=90)
    ax.set_yticklabels([''] + list(df_conf.index))

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    plt.show()


def topk_predictions(text, target_col_label='nationality', topk=3, categories=CATEGORIES, char2i=CHAR2I, model=rnn):
    with torch.no_grad():
        output = evaluate_tensor(encode_one_hot_seq(text, char2i=char2i), model=model)
        topvalues, topindices = output.topk(topk, 1, True)
        predictions = []
        # TODO: try this:
        for rank, (log_loss_tens, category_index) in enumerate(zip(topvalues[0], topindices[0])):
            predictions.append(
                [rank, text, log_loss_tens.item(), categories[category_index]])
    return pd.DataFrame(predictions, columns='rank text log_loss'.split() + [target_col_label])


def print_predictions(text, target_col_label='nationality', n_predictions=3, categories=CATEGORIES, model=rnn):
    preds_df = topk_predictions(text=text, target_col_label=target_col_label, topk=n_predictions, categories=categories, model=model)
    if n_predictions > 1:
        print(preds_df)
    return preds_df


def print_example_tensor(text="O’Néàl", char2i=CHAR2I):

    # Transcode Unicode str ASCII without embellishments, diacritics (https://stackoverflow.com/a/518232/2809427)
    ascii_text = asciify(text)
    print(f'asciify({text}) => {ascii_text}')

    encoded_char = encode_one_hot_vec(ascii_text[0], char2i=char2i)
    print(f"encode_one_hot_vec({ascii_text[0]}): {encoded_char}")
    input_tensor = encode_one_hot_seq(ascii_text, char2i=char2i)
    print(f"input_tensor.size(): {input_tensor.size()}")


def print_dataset_samples(df, num_samples=3, replace=True, target='nationality'):
    print(sample_groupby(df, num_samples=num_samples, groupby=target, replace=replace))


def load_name_counts(filepath=SRC_DATA_DIR / 'names' / 'name_counts.csv.gz'):
    return pd.read_csv(filepath)


def train_batches(df=None, model=None, target='nationality', n_iters=5000, print_every=100, char2i=CHAR2I, categories=None):
    df = load_name_counts() if df is None else df
    categories = list(df['category'].unique())
    model = RNN(vocab_size=len(CHAR2I), n_hidden=128, n_categories=len(categories)) if model is None else model
    output_losses = []

    start = time.time()

    for it in tqdm(range(1, n_iters + 1)):
        df_batch = sample_groupby(df, num_samples=1, groupby=target, replace=True, shuffle=True)
        model, batch_output_losses = train_batch(df_batch, model=model, char2i=char2i, categories=categories, lr=.005)
        output_losses += batch_output_losses

        # Print iteration number, loss, name and guess
        if not it % print_every:
            predictions = [category_from_output(output, categories=categories) for output, loss in output_losses]
            predictions = pd.DataFrame(
                [list(row) for row in predictions],
                columns='pred pred_i'.split())
            df_batch['pred'] = predictions['pred']
            df_batch['pred_i'] = predictions['pred_i']
            print(f'{it:06d} {it*100//n_iters}% {time_elapsed(start)}')
            print(df_batch)

            output_losses.extend([list(x) for x in batch_output_losses])

    train_time = time_elapsed(start)
    return dict(model=rnn, n_hidden=model.n_hidden, losses=output_losses, train_time=train_time, categories=categories, char2i=char2i)


def preprocess_surname_nationality_df(df, target_col='nationality', text_col='surname'):
    new_rows = []
    # Some Ukranian names have Russian alternatives e.g. surname='Markevych (Russian: Markevich)'
    # With the Russian invasion of Ukraine it is important to distinguish between the two
    # (the nationalities and the languages of Russia and Ukraine)
    # issus = df['surname'].str.contains(r'(', regex=False)
    # retain only the Ukranian spelling for Ukranian names:
    df[target_col] = df[target_col].apply(lambda x: asciify(x))
    print(df)
    df[text_col] = df[text_col].str.split('(').apply(lambda x: x[0].strip())
    print(df)
    df[text_col] = df[text_col].apply(lambda x: asciify(x))
    print(df)
    df[text_col] = df[text_col].str.strip().str.strip(',')
    print(df)
    ismulti = ~df[text_col].str.match(r"^[- A-Za-z']+$")
    print(f"sum(ismulti): {sum(ismulti)}")
    if sum(ismulti) > 0:
        for i, row in df[ismulti].iterrows():
            base_row = row.to_dict()
            print(base_row)
            for name in row[text_col].split(','):
                name = name.strip().strip(',')
                new_row = copy.copy(base_row)
                new_row.update({text_col: name})
                new_rows.append(new_row)
        new_rows = pd.DataFrame(new_rows)
        print('NEW ROWS')
        print(new_rows)
        df = df.drop(ismulti, axis=0)
        df = pd.concat([df, new_rows])
    return df


def train_fast(df=None, model=rnn, n_iters=100000, print_every=10000, char2i=CHAR2I, target_col='nationality', categories=CATEGORIES):
    df = df if df is not None else load_names_from_text()
    df = df[df[target_col].isin(categories)].copy().reset_index()
    groups = df.groupby(target_col)

    current_loss = 0
    all_losses = []

    start = time.time()

    num_samples_per_group = int(n_iters // len(categories)) + 1
    print(f'num_samples_per_group: {num_samples_per_group}')
    cats, lines, category_tensors, line_tensors = stratified_random_examples(
        groups, num_samples_per_group=num_samples_per_group, categories=categories, replace=True)
    for it, (cat, line, cat_tensor, line_tensor) in tqdm(enumerate(zip(cats, lines, category_tensors, line_tensors))):
        model, output, loss = train_sample(cat_tensor, line_tensor, model=model, char2i=char2i, categories=categories, lr=.005)
        current_loss += loss

        if not (it + 1) % print_every:
            guess, guess_i = category_from_output(output, categories=categories)
            is_correct = '✓' if guess == cat else f'✗ \t (should be {cat.upper()})'
            print(f'{it:06d} {it*100//n_iters}% {time_elapsed(start)} {loss:.4f} {line}: {guess} {is_correct}')

            all_losses.append(current_loss / print_every)
            current_loss = 0

    train_time = time_elapsed(start)
    return dict(model=rnn, n_hidden=model.n_hidden, losses=all_losses, train_time=train_time, categories=categories, char2i=char2i)


def train(df=None, model=rnn, n_iters=5000, print_every=100, char2i=CHAR2I, target='nationality', categories=CATEGORIES):
    df = df if df is not None else load_names_from_text()
    df = df[df[target].isin(categories)].copy().reset_index()
    groups = df.groupby(target)

    current_loss = 0
    all_losses = []
    plot_every = print_every

    start = time.time()

    for it in range(n_iters):
        cats, lines, category_tensors, line_tensors = stratified_random_examples(groups, num_samples_per_group=1, categories=categories)
        for cat, line, cat_tensor, line_tensor in zip(cats, lines, category_tensors, line_tensors):
            model, output, loss = train_sample(cat_tensor, line_tensor, model=model, char2i=char2i, categories=categories, lr=.005)
            current_loss += loss

            if not (it + 1) % print_every:
                guess, guess_i = category_from_output(output, categories=categories)
                correct = '✓' if guess == cat else '✗ (%s)' % cat
                print(f'{it:06d} {(it*100) // n_iters}% {time_elapsed(start)} {loss:.4f} {line} => {guess} {correct}')

                all_losses.append(current_loss / plot_every)
                current_loss = 0

    train_time = time_elapsed(start)
    return dict(model=rnn, n_hidden=model.n_hidden, losses=all_losses, train_time=train_time, categories=categories, char2i=char2i)


def concatenate_surname_tables(html_dir=Path.home() / 'Downloads' / 'surnames',
                               html_text_col='surname', textfile_text_col='surname', html_target='nationality', textfile_target='category'):
    """ FIXME: use html_text_col='surname', textfile_text_col='name', html_target='nationality', textfile_target='category' """
    html_dir = Path(html_dir)
    filepaths = list(html_dir.glob('Most Common *.html'))
    dfs = []
    for fp in filepaths:
        nationality = fp.with_suffix('').name.replace('Most Common', '').replace('Surnames & Meanings', '').strip()
        fp = str(fp)
        df1 = pd.read_html(str(fp))[-1]
        df1.columns = 'rank surname count frequency'.split()
        df1['frequency'] = df1['frequency'].str.replace(',', '')
        df1['freq_numerator'] = df1['frequency'].str.split(':').apply(lambda x: float(x[0]))
        df1['freq_denominator'] = df1['frequency'].str.split(':').apply(lambda x: float(x[1]))
        df1['nationality'] = nationality
        dfs.append(df1)
    dftot = pd.concat(dfs)
    dftot = preprocess_surname_nationality_df(dftot)
    print(f"dftot.shape: {dftot.shape}")
    df = load_names_from_text(dedupe=True, categories=None)
    df = pd.concat([dftot, df])

    if textfile_text_col != html_text_col:
        df[html_text_col] = df[html_text_col].fillna(df[textfile_text_col][df[html_text_col].isna()]).values
        df = df.drop(columns=[textfile_text_col])
    if textfile_target != html_target:
        df[html_target] = df[html_target].fillna(df[textfile_target][df[html_target].isna()]).values
        df = df.drop(columns=[textfile_target])
    return df


def plot_training_curve(losses):
    plt.figure()
    plt.plot(losses)
    plt.show(block=False)

    print(f"META['categories']: {META['categories']}")
    print(f'CATEGORIES: {CATEGORIES}')
    print()
    print('Russia: https://en.wikipedia.org/wiki/Fyodor_Dostoevsky')
    print_predictions(text='Fyodor', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Dostoevsky', n_predictions=3, categories=CATEGORIES)
    print()
    print('Nigeria: https://en.wikipedia.org/wiki/Sanmi_Koyejo # Oluwasanmi')
    print_predictions(text='Oluwasanmi', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Sanmi', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Koyejo', n_predictions=3, categories=CATEGORIES)
    print()
    print('Japan: https://en.wikipedia.org/wiki/Satoshi_Nakamoto')
    print_predictions(text='Satoshi', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Nakamoto', n_predictions=3, categories=CATEGORIES)
    print()
    print('Etheopia: https://en.wikipedia.org/wiki/Rediet_Abebe')
    print_predictions(text='Rediet', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Abebe', n_predictions=3, categories=CATEGORIES)
    print()
    print('Italy: https://en.wikipedia.org/wiki/Silvio_Micali')
    print_predictions(text='Silvio', n_predictions=3, categories=CATEGORIES)
    print_predictions(text='Micali', n_predictions=3, categories=CATEGORIES)


def save_results(**results):
    # load/save test for use on the huggingface spaces server
    METANEW = copy.copy(results)
    # METANEW = dict(
    #     categories=CATEGORIES,
    #     char2i=CHAR2I
    # )
    METANEW['model'] = results['model']
    METANEW['losses'] = results['losses']
    METANEW['train_time'] = results['train_time']

    METANEW['state_dict'] = results['model'].state_dict()
    METANEW['min_loss'] = min(METANEW['losses'])
    print(f"min_loss: {METANEW['min_loss']}")
    train_time_str = str(results['train_time']).replace(':', 'min_') + 'sec'
    filename = str(MODEL_PATH) + f"-{METANEW['min_loss']:.3f}-{train_time_str}"
    filename = filename.replace('.', '_')
    save_model(filename, **METANEW)
    print(f'Model METANEW.keys(): {METANEW.keys()}')
    print(f'Saving model state_dict and meta to {filename}.*')


if __name__ == '__main__':
    repo = 'tangibleai/nlpia2'
    filepath = 'src/nlpia2/data/surname_nationalities.csv'
    suffix = '?inline=false'
    url = f"https://gitlab.com/{repo}/-/raw/main/{filepath}{suffix}"
    df = pd.read_csv(url)
    print(df)
    categories = list(df['nationality'].unique())
    print(categories)
    model = RNN(
        len(META['char2i']),
        n_hidden=n_hidden,
        n_categories=len(categories),
    )
    ans = input("Ready to start training (Y/N) [N]? ")
    if ans.lower().strip().startswith('y'):
        results = train(df, model=model, categories=categories)
        save_results(**results)
