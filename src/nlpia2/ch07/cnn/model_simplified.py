import logging
import math
import torch
import torch.nn as nn

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)


# .Initialize your CNN hyperparameters

class CNNTextClassifier(nn.Module):

    def __init__(self, embeddings=(4000, 50)):
        super().__init__()

        try:
            shape = embeddings.shape
        except AttributeError:
            try:
                shape = embeddings.size()
            except AttributeError:
                shape = embeddings
        self.seq_len = 35                         # <1>
        self.vocab_size = shape[0]
        self.embedding_size = shape[1]
        self.kernel_lengths = [2, 3, 4, 5]        # <2>
        self.stride = 2
        self.conv_output_size = 32                # <3>

        self.dropout = nn.Dropout(.1)

        self.embedding = nn.Embedding(self.vocab_size + 1, self.embedding_size, padding_idx=0)

        self.convolvers = []
        self.poolers = []
        for i, kernel_len in enumerate(self.kernel_lengths):
            self.convolvers.append(nn.Conv1d(self.seq_len, self.conv_output_size, kernel_len, self.stride))
            self.poolers.append(nn.MaxPool1d(kernel_len, self.stride))

        self.encoding_size = self.cnn_output_size()
        self.linear_layer = nn.Linear(self.encoding_size, 1)

# <1> assume a maximum text length of 35 tokens
# <2> only one kernel layer is needed for reasonable results
# <3> the convolution output need not have the same number of channels as your embeddings

    # .Compute the shape of the CNN output
    def cnn_output_size(self):
        """ Calculate the number of encoding dimensions output from CNN layers

        Convolved_Features = ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1
        Pooled_Features = ((embedding_size + (2 * padding) - dilation * (kernel - 1) - 1) / stride) + 1

        source: https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html
        """
        out_pool_total = 0
        for kernel_len in self.kernel_lengths:
            out_conv = (
                (self.embedding_size - 1 * (kernel_len - 1) - 1) / self.stride) + 1
            out_conv = math.floor(out_conv)
            out_pool = ((out_conv - 1 * (kernel_len - 1) - 1) / self.stride) + 1
            out_pool = math.floor(out_pool)
            out_pool_total += out_pool

        # return the len of a "flattened" vector that is passed into a fully connected (Linear) layer
        return out_pool_total * self.conv_output_size

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
