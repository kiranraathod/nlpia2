from itertools import product

from main import main

DEFAULTS = dict(
    cuda=true,
    nepochs=10,
    model_type='RNN_TANH',
    nhid=200,
    batch_size=20,
    bptt=35,
    nlayers=1,
)


def train_hardcoded_examples(
        hidden_sizes=(200, 300, 400),
        rnn_types=tuple('GRU LSTM RNN_TANH RNN_RELU'.split())):
    for hidden_size, rnn_type in product(hidden_sizes, rnn_type):
        kwargs = DEFAULTS.copy()
        kwargs.update(dict(NHID=hidden_size, MODEL=rnn_type))

        locals().update(kwargs)
        filename = f'model_epochs_10_model_{model}_nhid_{nhid}_batch_size_{batch_size}_bptt_{bptt}_nlayers_{nlayers}'.format(**kwargs)
        print(
            f"python main.py {'--cuda' if cuda else ''} --epochs {nepochs} --model_type {model_type}"
            f" --nhid {nhid} --batch_size {batch_size} --bptt {bptt} --nlayers {nlayers} --save {filename}.pt"
        )
        print(kwargs)
        main(**kwargs)


MODEL = RNN_TANH
NLAYERS = 1
NEPOCHS = 6
NHID = 200
BATCH_SIZE = 20
BPTT = 35

function train_model_layers_epochs() {
    MODEL =$1
    NLAYERS =$2
    NEPOCHS =$3
    SAVE = tuning_model_${MODEL}_nlayers_${NLAYERS}_epochs_${NEPOCHS}_nhid_${NHID}_batch_size_${BATCH_SIZE}_bptt_${BPTT}_nlayers
    echo "python main.py --cuda --model $MODEL --nlayers $NLAYERS --epochs $NEPOCHS --nhid $NHID --batch_size $BATCH_SIZE --bptt $BPTT --save ${SAVE}.pt" | tee - a ${SAVE}.md
    python main.py - -cuda
    - -model $MODEL
    - -nlayers $NLAYERS
    - -epochs $NEPOCHS
    - -nhid $NHID
    - -batch_size $BATCH_SIZE
    - -bptt $BPTT
    - -save ${SAVE}.pt | tee ${SAVE}.md
    echo "python main.py --cuda --epochs $NEPOCHS --model $MODEL --nhid $NHID --batch_size $BATCH_SIZE --bptt $BPTT --nlayers $NLAYERS --save ${SAVE}.pt" | tee - a ${SAVE}.md
    # | end of epoch  10 | time: 35.52s | valid loss  6.91 | valid ppl  1002.38
    # | End of training | test loss  6.85 | test ppl   941.55
    # python main.py --cuda --epochs 10 --model RNN_TANH --nhid 200 --batch_size 20 --bptt 35 --nlayers 1 --save model_epochs_10_model_RNN_TANH_nhid_200_batch_size_20_bptt_35_nlayers_1.pt >> model_epochs_10_model_RNN_TANH_nhid_200_batch_size_20_bptt_35_nlayers_1.md
}


function tune_model_layer_epochs() {

    train_model_layers_epochs "RNN_TANH" 1 6
    # | end of epoch   6 | time: 23.10s | valid loss  7.89 | valid ppl  2661.77 | End of training | test loss  7.70 | test ppl  2205.54

    train_model_layers_epochs "RNN_RELU" 1 6
    # | end of epoch   6 | time: 23.07s | valid loss   nan | valid ppl      nan | End of training | test loss   nan | test ppl      nan

    train_model_layers_epochs "LSTM" 1 6
    # | end of epoch   6 | time: 23.60s | valid loss  5.03 | valid ppl   152.69 | End of training | test loss  4.96 | test ppl   142.69

    train_model_layers_epochs "GRU" 1 6
    # | end of epoch   6 | time: 23.44s | valid loss  4.94 | valid ppl   140.41 | End of training | test loss  4.87 | test ppl   130.37

    train_model_layers_epochs "RNN_TANH" 2 12
    train_model_layers_epochs "RNN_RELU" 2 12
    train_model_layers_epochs "LSTM" 2 12
    train_model_layers_epochs "GRU" 2 12
}
