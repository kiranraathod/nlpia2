from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from ch08_rnn_char_nationality import RNN, train, save_results


MODEL_PATH = Path(__file__).with_suffix('').name
PYTORCH_TUTORIAL_CATEGORIES = [
    'Arabic', 'Chinese', 'Czech', 'Dutch', 'English', 'French', 'German', 'Greek', 'Irish', 'Italian', 'Japanese',
    'Korean', 'Nigerian', 'Polish', 'Portuguese', 'Russian', 'Scottish', 'Spanish', 'Vietnamese'
]
MANUALLY_ADDED_CATEGORIES = ['Ethiopian', 'Indian', 'Nepalese']


# META = load_model_meta(MODEL_PATH)

META = {
    'categories': [
        'Algerian', 'Arabic', 'Brazilian', 'Chilean', 'Chinese', 'Czech', 'Dutch', 'English', 'Ethiopian',
        'Finnish', 'French', 'German', 'Greek', 'Honduran', 'Indian', 'Irish', 'Italian', 'Japanese', 'Korean',
        'Malaysian', 'Mexican', 'Moroccan', 'Nepalese', 'Nicaraguan', 'Nigerian', 'Palestinian', 'Papua New Guinean',
        'Peruvian', 'Polish', 'Portuguese', 'Russian', 'Scottish', 'South African', 'Spanish', 'Ukrainian',
        'Venezuelan', 'Vietnamese'
    ],
    'char2i': {
        ' ': 0, "'": 1, ',': 2, '-': 3, '.': 4, ';': 5, 'A': 6, 'B': 7, 'C': 8, 'D': 9, 'E': 10,
        'F': 11, 'G': 12, 'H': 13, 'I': 14, 'J': 15, 'K': 16, 'L': 17, 'M': 18, 'N': 19, 'O': 20, 'P': 21,
        'Q': 22, 'R': 23, 'S': 24, 'T': 25, 'U': 26, 'V': 27, 'W': 28, 'X': 29, 'Y': 30, 'Z': 31, 'a': 32, 'b': 33,
        'c': 34, 'd': 35, 'e': 36, 'f': 37, 'g': 38, 'h': 39, 'i': 40, 'j': 41, 'k': 42, 'l': 43, 'm': 44, 'n': 45,
        'o': 46, 'p': 47, 'q': 48, 'r': 49, 's': 50, 't': 51, 'u': 52, 'v': 53, 'w': 54, 'x': 55, 'y': 56, 'z': 57
    },
}
META['n_hidden'] = 128
META['n_categories'] = len(META['categories'])
# save_model(MODEL_PATH, **META)

CATEGORIES = META['categories']
CHAR2I = META['char2i']


class RNNTagger(RNN):

    def __init__(self, n_hidden=128, categories=CATEGORIES, char2i=CHAR2I):
        super().__init__()
        self.categories = categories
        self.n_categories = len(self.categories)  # <1> n_categories = n_outputs (one-hot)
        print(f'RNN.categories: {self.categories}')
        print(f'RNN.n_categories: {self.n_categories}')

        self.char2i = dict(char2i)
        self.vocab_size = len(self.char2i)

        self.n_hidden = n_hidden

        self.W_c2h = nn.Linear(self.vocab_size + self.n_hidden, self.n_hidden)
        self.W_c2y = nn.Linear(self.vocab_size + self.n_hidden, self.n_categories)
        self.activation = nn.Sigmoid()

    # .Tagging in PyTorch
    # [source,python]
    # ----
    def forward(self, x, hidden):
        combined = torch.cat((x, hidden), 1)
        hidden = self.W_c2h(combined)
        y = self.W_c2y(combined)
        y = self.activation(y)  # <1>
        return y, hidden
    # ----
    # <1> if you use BCEWithLogitsLoss you can delete the activation layer for faster training

    def __str__(self):
        return (
            f"RNNTagger(\n    n_hidden={self.n_hidden},\n    n_categories={self.n_categories},\n"
            f"    categories=[{self.categories[0]}..{self.categories[-1]}],\n"
            f"    vocab_size={self.vocab_size},\n    char2i['A']={self.char2i['A']}\n)"
        )


def create_multihot_dataset(df, normalize=True, fillna=0, text_col='surname', target_col='nationality'):
    name_multihot_vecs = {}
    # FIXME: this dataset has already been deduplicated,
    #        so use the 'count' column instead of counting the nationality labels
    for text, group in df.groupby(text_col):
        name_multihot_vecs[text] = Counter(group[target_col])
    tags = pd.DataFrame(name_multihot_vecs).T.fillna(0)
    tags2 = pd.DataFrame()
    sums = tags.T.sum()
    for c in tags.columns:
        tags2[c] = tags[c] / sums
    return tags2


if __name__ == '__main__':
    repo = 'tangibleai/nlpia2'
    filepath = 'src/nlpia2/data/surname_nationalities.csv'
    suffix = '?inline=false'
    url = f"https://gitlab.com/{repo}/-/raw/main/{filepath}{suffix}"
    df = pd.read_csv(url)
    print(df)

    n_categories = 10
    ans = input(f"How many nationalities would you like to train on? [{n_categories}]? ")
    if ans.strip():
        n_categories = int(ans)
    categories = sorted(df['nationality'].unique())[:n_categories]
    print(f"categories: {categories}")

    char2i = META['char2i']
    char2i = dict(zip(sorted(char2i), range(len(char2i))))
    n_hidden = 128
    model = RNNTagger(
        char2i=char2i,
        categories=categories,
        n_hidden=128
    )
    print(f"model: {model}")

    n_iters = 10000
    ans = input(f"How many samples would you like to train on? [{n_iters}]? ")
    if ans.strip():
        n_iters = int(ans)

    lr = .005
    ans = input(f"What learning rate would you like to train with? [{lr}]? ")
    if ans.strip():
        lr = float(ans)

    critereon = nn.BCELoss()

    results = dict(lr=lr, n_iters=n_iters, critereon=critereon)
    print(f"hyperparams: {results}")

    if n_iters and n_hidden and lr:
        training_results = train(model=model, df=df, n_iters=n_iters, critereon=critereon, lr=lr)
        results.update(training_results)
        print(f"updated results: {results}")

        # required for computing the filename
        results['train_time'] = results.get('train_time', f'{np.random.randint(1000)}:np.random.randint(100)')
        results['losses'] = results.get('losses', [99])

        save_results(**results)
