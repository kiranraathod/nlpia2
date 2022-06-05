""" Model params hard coded
FIXME: Verify predict and compute_accuracy() functions by comparing to older versions in git

$ python main.py
Epoch: 1, loss: 0.71129, Train accuracy: 0.56970, Test accuracy: 0.64698
...
Epoch: 10, loss: 0.38202, Train accuracy: 0.80324, Test accuracy: 0.75984
"""
import time
from collections import Counter
import json
from itertools import chain
import logging
from pathlib import Path
import re
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from tqdm import tqdm  # noqa

from model_ch07 import CNNTextClassifier
# from model_ch07 import calc_conv_out_seq_len  # noqa


T0 = 1652404117  # number of seconds since 1970-01-01 as of May 12, 2022
MAX_SEED = 2**32 - 1
DATA_DIR = Path(__file__).parent / 'data'

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
log.setLevel(level=logging.INFO)


def tokenize_re(doc):
    return [tok for tok in re.findall(r'\w+', doc)]


hyperp = dict(
    use_glove=True,
    expand_glove_vocab=True,
    seq_len=40,
    vocab_size=2000,
    embedding_size=50,
    out_channels=50,
    num_stopwords=0,
    kernel_lengths=[1, 2, 3, 4, 5, 6],
    strides=[1, 1, 1, 1, 1, 1],
    batch_size=24,
    learning_rate=0.002,
    # TODO:
    # lots of dropout can cause the training accuracy to be worse than the test acc
    # low dropout can cause the model to overfit, so dropout should be incrementally increased
    dropout=0,
    num_epochs=400,
)


def pad(sequence, seq_len, pad_value=0):
    log.debug(f'BEFORE PADDING: {sequence}')
    padded = list(sequence)[:seq_len]
    padded = padded + [pad_value] * (seq_len - len(padded))
    log.debug(f'AFTER PADDING: {sequence}')
    return padded


def load_dataset(
    use_glove=True,
    expand_glove_vocab=bool(hyperp['expand_glove_vocab']),
    seq_len=int(hyperp['seq_len']),
    vocab_size=int(hyperp['vocab_size']),
    embedding_size=int(hyperp['embedding_size']),
    num_stopwords=int(hyperp['num_stopwords']),
    **kwargs,
):
    """ load and preprocess csv file: return [(token id sequences, label)...]

    1. load the CSV
    2. optionally fold the character case with lower()
    3. optionally remove punctuation characters (non-alpha chars)
    4. tokenize with regex or spacy (configurable)
    5. optionally remove stopwords (most frequent words)
    6. optionally remove infrequent words
    7. compute a reverse index (token->id)
    8. transform token sequences to `int` id sequences
    9. pad token id sequences so they are all the same length
    10. split your texts into training and test (validation) sets

    To be fully rigorous with your pipeline hygene you need to do train_test_split before
    tokenization and token filtering/folding, because this creates your vocabulary.
    And you don't want to let your model "cheat" by seeing the words in your test set that
    are not in your training set.
    So step 10 should be between step 1 and 2 and most of the other steps can be skipped for the test set.

    1, 10
    Then on trainset: 2, 3, 4, 5, 6, 7, 8, 9
    Then on testset: 2, 3, 4
    Then on the testset remove all words not in the vocab from the trainset
    Skip 8 on the testset because that's the vocab from trainset
    Just 9 (pad) is needed to complete your testset preprocessing.
    """
    import re
    from nessvec.files import load_vecs_df
    HOME_DATA_DIR = Path.home() / '.nlpia2-data'
    PAD_TOK = '<PAD>'

    retval = {}
    df = pd.read_csv(HOME_DATA_DIR / 'disaster-tweets.csv')
    df = df[['text', 'target']]
    df['target'] = (df['target'] > 0).astype(int)
    counts = Counter(chain(*[
        re.findall(r'[\w]+', t.lower()) for t in df['text']]))    # <1>
    vocab = [tok for tok, count in counts.most_common(vocab_size + num_stopwords)[num_stopwords:]]  # <2>
    if PAD_TOK not in vocab:
        vocab = [PAD_TOK] + list(vocab)

    # FIXME: Compare with and without glove by shuffling or not shuffling the index
    # Will also confirm that the word vocab and index are correct
    if use_glove:
        glove = load_vecs_df(HOME_DATA_DIR / 'glove.6B.50d.txt')
        num_glove_vecs, embed_dims = glove.shape
        new_embeddings = pd.DataFrame([pd.Series([0] * embed_dims, name=PAD_TOK)])
        glove = pd.concat([new_embeddings, glove])
        print(f'glove.shape {glove.shape}')
        print(glove)

        # <3> If your vocab of popular words contains words that glove does not
        #     you can expand your vocabulary by creating random vectors for each of these words
        # Because these words are really common in your domain (dataset) they are probably
        #     important for you language model to understand.
        if expand_glove_vocab:
            nonglove_words = [tok for tok in vocab if tok not in glove.index]   # <3>
            vocab.extend(nonglove_words)
            embed = []
            # create the new vocabulary (TODO: should be simple concat(df[nonglove_vocab], df[vocab]))
            for tok in vocab:                                              # <4>
                if tok in glove.index:
                    embed.append(glove.loc[tok])
                else:
                    embed.append(.1 * np.random.randn(embed_dims))
                    # embed.append(np.zeros(embed_dims))
            vocab = vocab[:vocab_size]
            embed = embed[:vocab_size]
        else:
            vocab = [tok for tok in vocab if tok in glove.index]
            print(f'len(vocab) {len(vocab)}')
            embed = glove.loc[vocab].values
        embed = pd.DataFrame(embed, index=vocab)
        print(f'df_glove before tensor: {embed}')
        print(f'glove.shape {glove.shape}')
        print(f'embed.shape {embed.shape} (after filtering')
        embed = torch.tensor(embed.values, dtype=torch.float32)
        print(f'embed.size() {embed.size()}')
        print(f'embed.size(): {embed.size()}')
        print(f'pd.Series(vocab):\n{pd.Series(vocab)}')
        retval['embed'] = embed
    else:
        retval['embed'] = torch.random.randn((vocab_size, embedding_size))
    assert 'embed' in retval, f'retval not in {retval.keys()}'

    # <1> tokenizing, case folding, and occurrence counting
    # <2> ignore the 3 most frequent tokens ("t", "co", "http")
    # <3> find
    # <3> skip unknown embeddings; alternatively create zero vectors
    # <4> ensure your embedding matrix is in the same order as your vocab

    # 7. compute reverse index
    tok2id = dict(zip(vocab, range(len(vocab))))

    # 8. Simplified: transform token sequences to integer id sequences
    id_sequences = [[i for i in map(tok2id.get, seq) if i is not None] for seq in df['text']]

    # 9. Simplified: pad token id sequences
    padded_sequences = []
    for seq in id_sequences:
        padded_sequences.append(pad(seq, seq_len=seq_len, pad_value=vocab.index(PAD_TOK)))
    padded_sequences = torch.IntTensor(padded_sequences)

    # 10. Configurable sampling for testset (test_size samples)
    retval.update(dict(zip(
        'x_train x_test y_train y_test'.split(),
        train_test_split(
            padded_sequences,
            list(df['target']),
            test_size=.1))))
    retval['vocab'] = vocab
    retval['tok2id'] = tok2id
    return retval


class DatasetMapper(Dataset):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


def calculate_accuracy(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    true_positives = 0
    true_negatives = 0
    for true, pred in zip(y_true, y_pred):
        if (pred >= 0.5) and (true == 1):
            true_positives += 1
        elif (pred < 0.5) and (true == 0):
            true_negatives += 1
        else:
            pass
    # Return accuracy
    return (true_positives + true_negatives) / len(y_true)


class Pipeline:

    def __init__(self, **kwargs):
        """
        win=True will set winning random seeds:
            "split_random_state": 850753,
            "numpy_random_state": 704,
            "torch_random_state": 704463,
            or
            python train.py --split_random_state=850753 --numpy_random_state=704 --torch_random_state=704463
        """
        super().__init__()
        self.__dict__.update(kwargs)
        print(vars(self))

        dataset = load_dataset(**kwargs)
        self.x_train = dataset['x_train']
        self.y_train = dataset['y_train']
        self.x_test = dataset['x_test']
        self.y_test = dataset['y_test']
        self.model = CNNTextClassifier(
            embeddings=dataset['embed'],
            out_channels=None,
            seq_len=hyperp['seq_len'],
            kernel_lengths=hyperp['kernel_lengths'],
            strides=hyperp['strides'],
        )

    def train(self, X=None, y=None):

        self.trainset_mapper = DatasetMapper(self.x_train, self.y_train)
        self.testset_mapper = DatasetMapper(self.x_test, self.y_test)

        self.loader_train = DataLoader(self.trainset_mapper, batch_size=self.batch_size)
        self.loader_test = DataLoader(self.testset_mapper, batch_size=self.batch_size)

        optimizer = optim.RMSprop(self.model.parameters(), lr=self.learning_rate)

        self.learning_curve = []
        for epoch in range(self.num_epochs):
            self.model.train()
            predictions = []
            for x_batch, y_batch in self.loader_train:
                y_batch = y_batch.type(torch.FloatTensor)
                # print(f'y_batch: {y_batch}')
                y_pred = self.model(x_batch)
                # print(f'y_pred: {y_pred}')
                loss = F.binary_cross_entropy(y_pred, y_batch)
                # print(f'loss: {loss}')
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # Save predictions
                predictions += list(y_pred.detach().numpy())

            test_predictions = self.predict()
            self.loss = loss.item()
            self.train_accuracy = calculate_accuracy(self.y_train, predictions)
            self.test_accuracy = calculate_accuracy(self.y_test, test_predictions)
            self.learning_curve += [[self.loss, self.train_accuracy, self.test_accuracy]]
            print(
                "Epoch: %d, loss: %.5f, Train accuracy: %.5f, Test accuracy: %.5f"
                % (epoch + 1, self.loss, self.train_accuracy, self.test_accuracy)
            )
        return self

    def predict(self, X=None):

        self.model.eval()  # evaluation mode
        predictions = []

        if X is not None:
            X_batches = zip([X], [[None] * len(X)])
        else:
            X_batches = list(zip(*self.loader_test))[0]
            y_batches = list(zip(*self.loader_test))[1]
        with torch.no_grad():
            for x_batch, y_batch in zip(X_batches, y_batches):
                y_pred = self.model(x_batch).detach().numpy()
                predictions += list(y_pred)
        return predictions

    def score(self, X, y):
        y_pred = self.predict(X)
        return np.mean((y_pred - y.detach.numpy())**2) ** .5

    def dump(self, filepath=None, indent=4):
        js = self.dumps(indent=indent)
        if filepath is None:
            t = int((time.time() - T0) / 60)
            filepath = f'disaster_tweets_cnn_pipeline_{t}.json'
        with open(filepath, 'w') as fout:
            fout.write(js)
        return js

    def dumps(self, indent=4):
        hashable_dict = {}
        for k, v in vars(self).items():
            if v is None or isinstance(v, (str, float, int, bool)):
                hashable_dict[k] = v
                continue
            if isinstance(v, (tuple, np.ndarray)):
                v = list(v)
            if isinstance(v, torch.Tensor):
                v = list(v.detach().numpy())
            if isinstance(v, list):
                if isinstance(v[0], torch.Tensor):
                    v = [list(x.detach().numpy()) for x in v]
            try:
                hashable_dict[k] = json.loads(json.dumps(v))
            except TypeError:
                pass
        return json.dumps(hashable_dict, indent=indent)


def parse_argv(sys_argv=sys.argv):
    argv = list(reversed(sys_argv[1:]))

    pipeline_args = []
    pipe_kwargs = {}  # dict(tokenizer='tokenize_re')
    while len(argv):
        a = argv.pop()
        if a.startswith('--'):
            if '=' in a:
                k, v = a.split('=')
                k = k.lstrip('-')
            else:
                k = a.lstrip('-')
                v = argv.pop()
            pipe_kwargs[k] = v
        else:
            pipeline_args.append(a)
    for k in pipe_kwargs:
        pipe_kwargs[k] = type(hyperp[k])(pipe_kwargs[k])
    # hyperp['use_glove'] = bool(int(hyperp['use_glove'])),
    # hyperp['expand_glove_vocab'] = bool(int(hyperp['expand_glove_vocab'])),
    # hyperp['seq_len'] = int(hyperp['seq_len']),
    # hyperp['vocab_size'] = int(hyperp['vocab_size']),
    # hyperp['embedding_size'] = int(hyperp['embedding_size']),
    # hyperp['num_stopwords'] = int(hyperp['num_stopwords'])
    return pipeline_args, pipe_kwargs


def main():

    cli_args, cli_kwargs = parse_argv(sys.argv)
    if len(cli_args):
        log.error(f'main.py does not accept positional args: {cli_args}')
    log.warning(f'kwargs: {cli_kwargs}')

    hyperp.update(cli_kwargs)
    pipeline = Pipeline(
        **hyperp)

    pipeline = pipeline.train()
    hyperparms = json.loads(pipeline.dump())

    # predictions = pipeline.predict()

    return dict(pipeline=pipeline, hyperp=hyperparms)


if __name__ == '__main__':

    # results = main()
    cli_args, cli_kwargs = parse_argv(sys.argv)
    if len(cli_args):
        log.error(f'main.py does not accept positional args: {cli_args}')
    log.warning(f'kwargs: {cli_kwargs}')

    hyperp.update(cli_kwargs)
    pipeline = Pipeline(**hyperp)

    pipeline = pipeline.train()
    hyperparms = json.loads(pipeline.dump())

    # predictions = pipeline.predict()

    results = dict(pipeline=pipeline, hyperp=hyperparms)
    print("=" * 100)
    print("=========== HYPERPARMS =============")
    print(results['hyperp'].keys())
    print("=" * 100)
