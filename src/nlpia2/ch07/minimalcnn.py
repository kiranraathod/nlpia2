# !pip install dataframe-image
import dataframe_image as dfi

import pandas as pd
import numpy as np
import torch
from torch import nn
from pathlib import Path
from matplotlib import pyplot as plt


# num_examples = 7
num_channels = 1
# embedding_size = 1

kernel = [.5, -.5]
kernel_size = len(kernel)
stride = 1

x = [1, 1, 1, 0, 0, 0, 1, 1, 1]
seq_len = len(x)

x = np.array(x, np.float32)
x = torch.tensor(x)
print()
print(f"x.resize_({num_channels}, {num_channels}, {seq_len})")
print(x.resize_(num_channels, num_channels, seq_len))
print()
print('x')
print(x)

# dataset = torch.arange(
#     num_examples * seq_len * embedding_size,
#     dtype=torch.float)
# dataset.resize_(num_examples, seq_len, embedding_size)

# data = np.arange(
#     num_examples * seq_len * num_channels,
#     dtype=np.float32,
# )
# data = data.reshape(num_examples, seq_len * num_channels)
# df = pd.DataFrame(data)

# IMAGES_DIR = Path.home() / 'code' / 'tangibleai' / 'nlpia-manuscript' / 'manuscript' / 'images' / 'ch07'
# dfi.export(df, IMAGES_DIR / 'df-minimal-cnn-dataset.png', max_rows=7)

# dataset = torch.from_numpy(df.values)
# dataset.resize_(num_examples, seq_len, num_channels)

# x = dataset[0]
# x.resize_(seq_len, num_channels)

conv = nn.Conv1d(
    in_channels=num_channels,
    out_channels=num_channels,
    # groups=None,
    stride=1,
    kernel_size=2
)
print()
print(f"conv = nn.Conv1d({num_channels}, {num_channels}, stride={stride}, kernel_size={kernel_size})")
print(conv)

print()
print('conv.weight')
print(conv.weight)
print()
print('conv.bias')
print(conv.bias)

print()
print('conv.forward(x)')
print(conv.forward(x))

state = conv.state_dict()
print()
print('state (conv.state_dict()):')
print(state)

state['weight'] = torch.tensor(np.array([[kernel]], dtype=np.float32))
state['bias'] = torch.tensor([0])
print()
print('updated state:')
print(state)

conv.load_state_dict(state)
print()
print('updated conv:')
print(conv)

x = conv.forward(x)
print('x = conv.forward(x): ')
print(x)

pool_size = 3
pool_stride = 2
pool = nn.MaxPool1d(pool_size, pool_stride)
print(f"pool = nn.MaxPool1d({pool_size}, {pool_stride})")
print(pool)

pool.forward(x)
print('x = pool.forward(y): ')
print(x)

# lin = nn.Linear(embedding_size * seq_len, 1)

kernel_size = 2
stride = 1

# cnn = MinimalCNN(
#     stride=stride,
#     kernel_size=kernel_size,
#     seq_len=seq_len)
# print(cnn.conv.weight.size())
# cnn.forward(x)
