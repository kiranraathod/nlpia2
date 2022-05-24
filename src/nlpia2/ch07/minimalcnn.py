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
embedding_dims = 1

dataset = torch.arange(
    num_examples * seq_len * embedding_dims,
    dtype=torch.float)
dataset.resize_(num_examples, seq_len, embedding_dims)

df = pd.DataFrame(np.arange(
    num_examples * seq_len * embedding_dims,
    dtype=torch.float).reshape(num_examples, seq_len, embedding_dims),)
dfi.render
dataset = torch.from_numpy(df)

x = dataset[0]
x.resize_(seq_len, embedding_dims)

lin = nn.Linear(embedding_dims * seq_len, 1)

kernel_size = 2
stride = 1

cnn = MinimalCNN(
    stride=stride,
    kernel_size=kernel_size,
    seq_len=seq_len)
print(cnn.conv.weight.size())
cnn.forward(x)
