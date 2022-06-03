""" 1-D Convolutional Neural Network for NLP

# References
- best diagrams: https://arxiv.org/pdf/1510.03820.pdf
- Christopher Manning (Stanford NLP):
  https://cuuduongthancong.com/dlf/3400312/xu-ly-ngon-ngu-tu-nhien/christopher-manning/cs224n-2020-lecture11-convnets.pdf
- Zhang and Wallace (2015) A Sensitivity Analysis of (and Practitioners’ Guide to) CNN for Sentence Classification:
  https://arxiv.org/pdf/1510.03820.pdf
- Yoon Kim: https://arxiv.org/pdf/1408.5882.pdf
- data.csv for text classification: https://github.com/zackhy/TextClassification
- Discriminative neural sentence modeling: https://arxiv.org/pdf/1504.01106v5.pdf
- diagrams like mine: https://sumanshuarora.medium.com/understanding-pytorch-conv1d-shapes-for-text-classification-c1e1857f8533
- confirmation you need to transpose embeddings: https://stackoverflow.com/questions/62372938/understanding-input-shape-to-pytorch-conv1d
- detailed pooling match examples: https://machinelearningmastery.com/pooling-layers-for-convolutional-neural-networks/
- pooling over channels: https://stackoverflow.com/questions/46562612/pytorch-maxpooling-over-channels-dimension
- compare learning curves with and without dropout

FIXME: Verify predict and compute_accuracy() functions by comparing to older versions in git

Definitions (from PyTorch Docs):
    in_channels: Number of channels in the input image/sequence
    out_channels: Number of channels produced by the convolution (encoding vector length)
    kernel_size: Size of the convolving kernel
    stride: Stride of the convolution. Default: 1
    padding: Padding added to both sides of the input. Default: 0
    padding_mode: 'zeros', 'reflect', 'replicate' or 'circular'. Default: 'zeros'
    dilation: Spacing between kernel elements. Default: 1
    groups: Number of blocked connections from input channels to output channels. Default: 1
    bias (bool, optional) – If True, adds a learnable bias to the output. Default: True

$ python main.py
Epoch: 1, loss: 0.71129, Train accuracy: 0.56970, Test accuracy: 0.64698
...
Epoch: 10, loss: 0.38202, Train accuracy: 0.80324, Test accuracy: 0.75984
"""
import logging
import numpy as np  # noqa
import torch
import torch.nn as nn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

#####################################################################
# .Compute the shape of the CNN output (the number of the output encoding vector dimensions)


def lopez_calc_output_seq_len(embedding_size, kernel_lengths, strides, desired_output_channels=None):
    """ Calculate the number of encoding dimensions output from CNN layers

    Convolved_Features = ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1
    Pooled_Features =    ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1

    source: https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html
    """
    if desired_output_channels is None:
        desired_output_channels = embedding_size // 2  # FIXME: stride instead of 2
    out_pool_total = 0
    for kernel_len, stride in zip(kernel_lengths, strides):
        out_conv = ((embedding_size - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool = ((out_conv - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool_total += out_pool

    # Returns "flattened" vector (input for fully connected layer)
    return out_pool_total * desired_output_channels


def calc_conv_out_seq_len(seq_len, kernel_len, stride=1, dilation=1, padding=0):
    """ L_out = 1 + (L_in + 2 * padding - dilation * (kernel_size - 1) - 1) / stride """
    return 1 + (seq_len + 2 * padding - dilation * (kernel_len - 1) - 1) // stride


def total_out_seq_len(seq_len, kernel_lengths, stride=1, dilation=1, padding=0):
    """ Calculate the number of encoding dimensions output from CNN layers

    From PyTorch docs:
      L_out = 1 + (L_in + 2 * padding - dilation * (kernel_size - 1) - 1) / stride
    But padding=0 and dilation=1, because we're only doing a 'valid' convolution.
    So:
      L_out = 1 + (L_in - (kernel_size - 1) - 1) // stride

    source: https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html
    """
    out_pool_total = 0
    for kernel_len in kernel_lengths:
        conv_output_len = calc_conv_out_seq_len(
            seq_len=seq_len, kernel_len=kernel_len, stride=stride,
            dilation=dilation, padding=padding
        )
        out_pool = calc_conv_out_seq_len(
            seq_len=conv_output_len, kernel_len=kernel_len, stride=stride,
            dilation=dilation, padding=padding
        )
        out_pool_total += out_pool

    # return the len of a "flattened" vector that is passed into a fully connected (Linear) layer
    return out_pool_total

# .Compute the shape of the CNN output (the number of the output encoding vector dimensions)
##########################################################################


def listify(x, n=None):
    """ Convert a scalar or generator to a list

    >>> listify(2.7)
    [2.7]
    >>> listify(range(1, 4), n=7)
    [1, 2, 3, 1, 2, 3, 1]
    >>> listify(range(2, 7), n=1)
    [2]
    """
    if n is None:
        if isinstance(x, (int, float)):
            return [x]
        if isinstance(x, str):
            x = float(x)
            try:
                return [int(x)]
            except ValueError:
                return [float(x)]
        return list(x)
    x = listify(x)
    len_x = len(x)
    return [x[i % len_x] for i in range(n)]
    # raise NotImplementedError("Use numpy resize or torch.squeeze and unsqueeze()")


# .CNN hyperparameters
# [source,python]
# ----
class CNNTextClassifier(nn.Module):

    def __init__(self,
                 embeddings=torch.rand(20000, 50),
                 out_channels=None,
                 seq_len=40,
                 kernel_lengths=(1, 2, 3, 4, 5, 6),
                 strides=1,
                 stride=None,
                 ):
        super().__init__()

        self.seq_len = seq_len                          # <1>
        self.vocab_size = embeddings.shape[0]           # <2>
        self.embedding_size = embeddings.shape[1]       # <3>
        self.out_channels = out_channels                # <4>
        kernel_lengths = listify(kernel_lengths)
        self.kernel_lengths = listify(kernel_lengths)   # <5>
        if stride is not None:
            strides = stride
        strides = listify(strides, n=len(kernel_lengths))
        self.strides = strides                          # <6>
        self.dropout = nn.Dropout(.4)                   # <7>
        self.pool_stride = self.stride                  # <8>
# ----
# <1> `N_`: assume a maximum text length of 40 tokens
# <2> `V`: number of unique tokens (words) in your vocabulary
# <3> `E`: number of dimensions in your word embeddings
# <4> `K`: number of weights in each kernel
# <5> `S`: number of time steps (tokens) to slide the kernel forward with each step
# <6> `D`: portion of convolution output to
# <7> `P`: each convolution layer gets its own pooling function
# <8> `C`: the total convolutional output size depends on how many and what shape convolutions you choose

# .Initialize CNN embedding
# [source,python]
# ----
        self.embed = nn.Embedding(
            self.vocab_size,                            # <1>
            self.embedding_size,                        # <2>
            padding_idx=0)
        state = self.embed.state_dict()
        state['weight'] = embeddings                    # <3>
        self.embed.load_state_dict(state)
# ----
# <1> vocab_size includes a row vector for the padding token
# <2> for pretrained 50-D GloVe vectors set embedding_size to 50
# <3> pretrained embeddings must include a padding token embedding (usually zeros)

# .Construct convolution and pooling layers
# [source,python]
# ----
        self.convolvers = []
        self.poolers = []
        total_out_len = 0
        for i, kernel_len in enumerate(self.kernel_lengths):
            self.convolvers.append(
                nn.Conv1d(in_channels=self.embedding_size,
                          out_channels=self.out_channels,
                          kernel_size=kernel_len,
                          stride=self.stride))
            print(f'conv[{i}].weight.shape: {self.convolvers[-1].weight.shape}')
            conv_output_len = calc_conv_out_seq_len(
                seq_len=self.seq_len, kernel_len=kernel_len, stride=self.stride)
            print(f'conv_output_len: {conv_output_len}')
            self.poolers.append(
                nn.MaxPool1d(kernel_size=conv_output_len, stride=self.stride))  # <7>
            total_out_len += calc_conv_out_seq_len(
                seq_len=conv_output_len, kernel_len=conv_output_len, stride=self.stride)
            print(f'total_out_len: {total_out_len}')
            # Given input size: (32x1x34). Calculated output size: (32x1x0). Output size is too small
            print(f'poolers[{i}]: {self.poolers[-1]}')
        print(f'total_out_len: {total_out_len}')
        self.linear_layer = nn.Linear(self.out_channels * total_out_len, 1)
        print(f'linear_layer: {self.linear_layer}')
# ----

# .Running the CNN forward
# [source,python]
# ----
    def forward(self, x):
        """ Takes sequence of integers (token indices) and outputs binary class label """

        e = self.embed(x)
        # print(f"x.size(): {x.size()}")
        # if you transpose then you can make the in_channels = embedding size
        # print(f"e.shape: {e.shape}")
        e = e.transpose(1, 2)
        # print(f"e.transpose(1,2).shape: {e.shape}")

        conv_outputs = []
        for (conv, pool) in zip(self.convolvers, self.poolers):
            z = conv(e)
            # print(f"conv(x).size(): {z.size()}")
            z = torch.relu(z)  # <1>
            # print(f"conv(x).size().relu(): {z.size()}")
            # torch.max(z, dim=1) # chris manning
            z = pool(z)        # <2>
            # Given input size: (32x1x34). Calculated output size: (32x1x0). Output size is too small

            # print(f"z = pool(relu(conv(x).size())): {z.size()}")
            conv_outputs.append(z)

        cat = torch.cat(conv_outputs, 2)    # <3>
        # print(f"cat: {cat.size()}")
        enc = cat.reshape(cat.size(0), -1)  # <4>
        # print(f"enc: {enc.size()}")

        sparse_enc = self.dropout(enc)      # <5>
        # print(f"sparse_enc: {sparse_enc.size()}")

        # FIXME: .linear(input, self.weight, self.bias)
        # RuntimeError: mat1 and mat2 shapes cannot be multiplied (10x1155 and 48x1)

        out = self.linear_layer(sparse_enc)  # <6>
        # print(f"linear out: {out.shape}")
        out = torch.sigmoid(out)
        # print(f"sigmoid out: {out.shape}")

        return out.squeeze()
# <1> each convolution layer gets its own activation function
# <2> each convolution layer gets a pooling function
# <3> concatenate the pooling outputs to create a single vector
# <4> flatten the output tensor to create an encoding vector
# <5> dropout (zero out) some encoding dimensions to make it sparse
# <6> output a linear (weighted) combination of the encoding values
# <7> for a binary class squash the output between 0 and 1
