from pathlib import Path
import torch

EOS_TOKEN = '<eos>'


class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []

    def add_word(self, word):
        if word not in self.word2idx:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.word2idx[word]

    def __len__(self):
        return len(self.idx2word)


class Corpus(object):
    def __init__(self, datadir):
        datadir = Path(datadir)
        if not datadir.is_dir():
            datadir = Path(__file__).parent / datadir

        self.dictionary = Dictionary()

        # avoid OOV complication by including all tokens in dictionary
        for split in 'train valid test'.split():
            filepath = datadir / f'{split}.txt'
            self.vocab_from_file(filepath)
            setattr(self, split, self.tokens2ids(filepath))

    def vocab_from_file(self, filepath):
        filepath = Path(filepath)
        with filepath.with_suffix('.txt').open() as f:
            for line in f:
                if not line.strip():
                    continue
                words = line.split() + [EOS_TOKEN]
                for word in words:
                    self.dictionary.add_word(word)
        return self.dictionary

    def tokens2ids(self, filepath):
        filepath = Path(filepath)
        assert filepath.is_file()

        with filepath.open() as fin:
            idss = []
            for line in fin:
                words = line.split() + ['<eos>']
                ids = []
                for word in words:
                    ids.append(self.dictionary.word2idx[word])
                idss.append(torch.tensor(ids).type(torch.int64))
            ids = torch.cat(idss)

        return ids  # id_sequences (1-D tensors of id numbers)
