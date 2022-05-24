# !pip install dataframe-image
import dataframe_image as dfi

import pandas as pd
import numpy as np
import torch
from torch import nn
from pathlib import Path
from matplotlib import pyplot as plt

num_examples = 7
seq_len = 5
embedding_size = 1

dataset = torch.arange(
    num_examples * seq_len * embedding_size,
    dtype=torch.float)
dataset.resize_(num_examples, seq_len, embedding_size)

df = pd.DataFrame(np.arange(
    num_examples * seq_len * embedding_size,
    dtype=float).reshape(num_examples, seq_len * embedding_size))
IMAGES_DIR = Path.home() / 'code' / 'tangibleai' / 'nlpia-manuscript' / 'manuscript' / 'images' / 'ch07'

dfi.export(df, IMAGES_DIR / 'df-minimal-cnn-dataset.png', max_rows=7)
dataset = torch.from_numpy(df.values).resize(num_examples, seq_len, embedding_size)

x = dataset[0]
x.resize_(seq_len, embedding_size)

lin = nn.Linear(embedding_size * seq_len, 1)

kernel_size = 2
stride = 1

# cnn = MinimalCNN(
#     stride=stride,
#     kernel_size=kernel_size,
#     seq_len=seq_len)
# print(cnn.conv.weight.size())
# cnn.forward(x)
