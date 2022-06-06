from PyPDF2 import PdfFileReader

from nlpia2.constants import DATA_DIR

# side-by-side partially unredacted versions of the report
url_quinta_jurecic1 = 'https://assets.documentcloud.org/documents/6979584/Volume-I-Final.pdf'
url_quinta_jurecic2 = 'https://assets.documentcloud.org/documents/6979583/Volume-II-FINAL.pdf'
# stream = open(DATA_DIR / 'The-Mueller-Report.pdf', 'rb')
# reader = PdfFileReader(stream)

# muellerPages = []
# for pageNum in range(reader.numPages):
#     muellerPages.append([par for par in mueller1Reader.getPage(pageNum).extractText().split('\n')])
# mueller1.close()

# muellerParagraphs = sum(muellerPages, [])  # flatten the list of lists
# len(muellerParagraphs)
# asciitext = unicode2ascii(text)
# asciitext
# ords = pd.Series([ord(c) for c in asciitext])
# pd.Series(list(asciitext))[(ords > 128)]


import torch
import torch.nn as nn
from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os
import unicodedata
import string


all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters) + 1  # Plus EOS marker


def find_files(path):
    return glob.glob(path)

# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427


def unicode2ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


# Read a file and split into lines
def readLines(filename):
    with open(filename, encoding='utf-8') as some_file:
        return [unicode2ascii(line.strip()) for line in some_file]


# Build the category_lines dictionary, a list of lines per category
category_lines = {}
all_categories = []
for filename in find_files('data/names/*.txt'):
    category = os.path.splitext(os.path.basename(filename))[0]
    all_categories.append(category)
    lines = readLines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)

if n_categories == 0:
    raise RuntimeError('Data not found. Make sure that you downloaded data '
                       'from https://download.pytorch.org/tutorial/data.zip and extract it to '
                       'the current directory.')

print('# categories:', n_categories, all_categories)
print(unicode2ascii("O'Néàl"))


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_catories):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size

        self.i2h = nn.Linear(n_categories + input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(n_categories + input_size + hidden_size, output_size)
        self.o2o = nn.Linear(hidden_size + output_size, output_size)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, category, input, hidden):
        input_combined = torch.cat((category, input, hidden), 1)
        hidden = self.i2h(input_combined)
        output = self.i2o(input_combined)
        output_combined = torch.cat((hidden, output), 1)
        output = self.o2o(output_combined)
        output = self.dropout(output)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)
