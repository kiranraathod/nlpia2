"""
FIXME: Verify predict and compute_accuracy() functions by comparing to older versions in git

$ python main.py
Epoch: 1, loss: 0.71129, Train accuracy: 0.56970, Test accuracy: 0.64698
...
Epoch: 10, loss: 0.38202, Train accuracy: 0.80324, Test accuracy: 0.75984
"""
import logging
import numpy as np
import torch
import torch.nn as nn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)


def cnn_output_size(desired_conv_output_size, embedding_size, kernel_lengths, strides):
    """ Calculate the number of encoding dimensions output from CNN layers

    Convolved_Features = ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1
    Pooled_Features = ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1

    source: https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html
    """
    out_pool_total = 0
    for kernel_len, stride in zip(kernel_lengths, strides):
        out_conv = ((embedding_size - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool = ((out_conv - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool_total += out_pool

    # Returns "flattened" vector (input for fully connected layer)
    return out_pool_total * desired_conv_output_size


def compute_output_seq_len(input_seq_len, kernel_lengths, stride):
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
        out_conv = (
            (input_seq_len - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool = ((out_conv - 1 * (kernel_len - 1) - 1) // stride) + 1
        out_pool_total += out_pool

    # return the len of a "flattened" vector that is passed into a fully connected (Linear) layer
    return out_pool_total


class CNNTextClassifier(nn.ModuleList):

    def __init__(self, params=None, win=False, **kwargs):
        """ Conv1D layers concatenated into a single 1D vector

        python train.py --split_random_state=850753 --numpy_random_state=704 --torch_random_state=704463
        """

        self.random_state = kwargs.pop('random_state', None)
        if self.random_state is not None:
            self.torch_random_state = self.random_state
            self.numpy_random_state = self.random_state + 1
        if params.torch_random_state is None:
            self.torch_random_state = torch.random.initial_seed()
        else:
            self.torch_random_state = params.torch_random_state
        if params.numpy_random_state is None:
            self.numpy_random_state = np.random.get_state()[1][0]
        else:
            self.numpy_random_state = params.numpy_random_state

        torch.random.manual_seed(self.torch_random_state)
        np.random.seed(self.numpy_random_state)

        assert self.torch_random_state == torch.random.initial_seed()
        assert self.numpy_random_state == np.random.get_state()[1][0]

        super().__init__()

        self.convolvers = []
        self.poolers = []

        self.seq_len = params.seq_len
        self.vocab_size = params.vocab_size
        self.embedding_size = params.embedding_size
        self.kernel_lengths = list(params.kernel_lengths)

        self.stride = getattr(params, 'stride', 2)
        self.strides = getattr(params, 'strides')
        if not self.strides:
            self.strides = [self.stride] * len(self.kernel_lengths)
        if len(self.strides) < len(self.kernel_lengths):
            self.strides = list(self.strides) + [self.stride] * (len(self.kernel_lengths) - len(self.strides))

        self.dropout_portion = params.dropout_portion
        self.dropout = nn.Dropout(self.dropout_portion)

        self.conv_output_size = getattr(params, 'conv_output_size', 32)
        self.__dict__.update(kwargs)

        for param_name, param_val in vars(self).items():
            if param_name.startswith('_'):
                continue
            if param_name in kwargs:
                setattr(self, param_name, kwargs[param_name])
            log.info(f'MODEL: {param_name}: {getattr(self, param_name)} ({type(getattr(self, param_name))})')

        self.embedding = nn.Embedding(self.vocab_size + 1, self.embedding_size, padding_idx=0)

        # default: 4 CNN layers with max pooling
        for i, (kernel_len, stride) in enumerate(zip(self.kernel_lengths, self.strides)):
            self.convolvers.append(nn.Conv1d(self.seq_len, self.conv_output_size, kernel_len, stride))
            # setattr(self, f'conv_{i + 1}', self.convolvers[i])
            self.poolers.append(nn.MaxPool1d(kernel_len, stride))
            # setattr(self, f'pool_{i + 1}', self.poolers[i])

        self.encoding_size = cnn_output_size(
            desired_conv_output_size=self.conv_output_size,
            embedding_size=self.embedding_size,
            kernel_lengths=self.kernel_lengths,
            strides=self.strides,
        )
        self.linear_layer = nn.Linear(self.encoding_size, 1)

    def forward(self, x):
        """ Takes sequence of integers (token indices) and outputs binary class label """

        x = self.embedding(x)

        conv_outputs = []
        for (conv, pool) in zip(self.convolvers, self.poolers):
            z = conv(x)
            z = torch.relu(z)
            z = pool(z)
            conv_outputs.append(z)

        # The output of each convolutional layer is concatenated into a unique vector
        union = torch.cat(conv_outputs, 2)
        union = union.reshape(union.size(0), -1)

        # The "flattened" vector is passed through a fully connected layer
        out = self.linear_layer(union)
        # Dropout is applied
        out = self.dropout(out)
        # Activation function is applied
        out = torch.sigmoid(out)

        return out.squeeze()
