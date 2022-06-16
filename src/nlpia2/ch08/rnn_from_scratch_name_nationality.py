""" Single-layer RNN "from scratch" in PyTorch

References:
  - https://www.twitch.tv/videos/1498823877"
  - https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html
  - https://gitlab.com/tangibleai/nlpia2/-/blob/main/src/nlpia2/ch08/rnn_from_scratch_name_nationality.py

Future work:
  - named entity recognizer for misspelled words/typos
  - named entity recognizer for drug names in any language (multilingual)
  - classify first names or full names for nationality
  - classify company names as nonprofits, for profits
  - regressor to estimate business size based on their name only
  - named entity recognizer to identify 

Exercises suggested by Shawn Robertson:
  - Try with a different dataset of line -> category, for example:
    - Any word -> language
    - First name -> gender
    - Character name -> writer
    - Page title -> blog or subreddit
  - Get better results with a bigger and/or better shaped network
    - Add more linear layers
    - Try the nn.LSTM and nn.GRU layers
    - Combine multiple of these RNNs as a higher level network

"""
from __future__ import unicode_literals, print_function, division
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
import random
import time
import torch
import torch.nn as nn
from io import open
from nlpia2.init import SRC_DATA_DIR, maybe_download
import seaborn as sns


from nlpia2.string_normalizers import Asciifier, ASCII_NAME_CHARS

name_char_vocab_size = len(ASCII_NAME_CHARS) + 1  # Plus EOS marker

asciify = Asciifier(include=ASCII_NAME_CHARS)


def find_files(path, pattern):
    return Path(path).glob(pattern)

# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427


# Read a file and split into lines
def read_lines(filename):
    with open(filename, encoding='utf-8') as some_file:
        return [asciify(line.rstrip()) for line in some_file]


# Build the category_lines dictionary, a list of lines per category
category_lines = {}
all_categories = []
for filepath in find_files(SRC_DATA_DIR / 'names', '*.txt'):
    filename = Path(filepath).name
    category = Path(filename).with_suffix('')
    filename = Path('names') / filename
    filepath = maybe_download(filename=filename)
    all_categories.append(category)
    lines = readLines(filepath)
    category_lines[category] = lines

n_categories = len(all_categories)

if n_categories == 0:
    raise RuntimeError('Data not found. Make sure that you downloaded data '
                       'from https://download.pytorch.org/tutorial/data.zip and extract it to '
                       'the current directory.')

print('# categories:', n_categories, all_categories)
print(asciify("O'Néàl"))


# Find letter index from all_letters, e.g. "a" = 0


letter2index =
    return all_letters.find(letter)

# Just for demonstration, turn a letter into a <1 x n_letters> Tensor


def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

# Turn a line into a <line_length x 1 x n_letters>,
# or an array of one-hot letter vectors


def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor


print(letterToTensor('J'))

print(lineToTensor('Jones').size())


class RNN(nn.Module):
    def __init__(self,
                 input_size,
                 hidden_size,
                 output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size

        self.i2h = nn.Linear(n_categories + input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(n_categories + input_size + hidden_size, output_size)
        self.o2o = nn.Linear(hidden_size + output_size, output_size)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, letter_vec, hidden):
        input_combined = torch.cat((letter_vec, hidden), 1)
        hidden = self.i2h(input_combined)
        output = self.i2o(input_combined)
        output_combined = torch.cat((hidden, output), 1)
        output = self.o2o(output_combined)
        output = self.dropout(output)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)


n_hidden = 128
rnn = RNN(n_letters, n_hidden, output_size=n_categories)


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)


n_hidden = 128
rnn = RNN(n_letters, n_hidden, n_categories)


letter_vec = letterToTensor('A')
hidden = torch.zeros(1, n_hidden)

output, next_hidden = rnn(letter_vec, hidden)


def categoryFromOutput(output):
    top_n, top_i = output.topk(1)
    category_i = top_i[0].item()
    return all_categories[category_i], category_i


print(categoryFromOutput(output))


def randomTrainingExample():
    category = random.choice(all_categories)
    line = random.choice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = lineToTensor(line)
    return category, line, category_tensor, line_tensor


for i in range(10):
    category, line, category_tensor, line_tensor = randomTrainingExample()
    print('category =', category, '/ line =', line)

learning_rate = 0.005  # If you set this too high, it might explode. If too low, it might not learn
criterion = nn.NLLLoss()


def train_example(category_tensor, line_tensor):
    hidden = rnn.initHidden()

    rnn.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)
    loss.backward()

    # Add parameters' gradients to their values, multiplied by learning rate
    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item()


# Keep track of losses for plotting
current_loss = 0
all_losses = []


def timeSince(since):
    now = time.time()
    s = now - since
    m = s // 60
    s -= m * 60
    return '%dm %ds' % (m, s)


start = time.time()


for iter in range(1, n_iters + 1):
    category, line, category_tensor, line_tensor = randomTrainingExample()
    output, loss = train(category_tensor, line_tensor)
    current_loss += loss

    # Print iter number, loss, name and guess
    if iter % print_every == 0:
        guess, guess_i = categoryFromOutput(output)
        correct = '✓' if guess == category else '✗ (%s)' % category
        print('%d %d%% (%s) %.4f %s / %s %s' % (iter, iter / n_iters * 100, timeSince(start), loss, line, guess, correct))

    # Add current loss avg to list of losses
    if iter % plot_every == 0:
        all_losses.append(current_loss / plot_every)
        current_loss = 0


plt.figure()
sns.set_theme('notebook')
sns.set_style()

plt.plot(all_losses, grid='on')
plt.show(block=False)

# Keep track of correct guesses in a confusion matrix
confusion = torch.zeros(n_categories, n_categories)
n_confusion = 10000

# Just return an output given a line


def evaluate(line_tensor):
    hidden = rnn.initHidden()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    return output


# Go through a bunch of examples and record which are correctly guessed
for i in range(n_confusion):
    category, line, category_tensor, line_tensor = randomTrainingExample()
    output = evaluate(line_tensor)
    guess, guess_i = categoryFromOutput(output)
    category_i = all_categories.index(category)
    confusion[category_i][guess_i] += 1

# Normalize by dividing every row by its sum
for i in range(n_categories):
    confusion[i] = confusion[i] / confusion[i].sum()

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(confusion.numpy())
fig.colorbar(cax)

# Set up axes
ax.set_xticklabels([''] + all_categories, rotation=90)
ax.set_yticklabels([''] + all_categories)

# Force label at every tick
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

# sphinx_gallery_thumbnail_number = 2
plt.show()
