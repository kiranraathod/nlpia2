# nlpia2

Official code repository for the book [_Natural Language Processing in Action, 2nd Edition_](https://proai.org/nlpia2e) by Maria Dyshel and Hobson Lane at [Tangible AI](https://tangibleai.com). It would not have happened without the generous work of [contributing authors](AUTHORS.md) and prosocial AI developers.

## Dependencies

Make sure you have Anaconda3 installed. And make sure you can run it from within a bash shell (terminal). The `conda --version` command should say something like '`4.10.3`.  Any version greater than `4.0.0` is fine.

Its also a good idea to create and activate conda environment where you can install big complicated packages like PyTorch and SpaCy without interfering with your other python projects. Here's how we did that for this book:

#### _`nlpia2/src/nlpia2/scripts/conda_install.sh`_
```bash
# create a new environment named "nlpia2" if one doesn't already exist:
conda activate nlpia2 \
    || conda create -n nlpia2 -y 'python==3.8.8' \
    && conda activate nlpia2

# install all of `nlpia2`'s dependences if they aren't already installed:
conda install -c defaults -c huggingface -c pytorch -c conda-forge -y \
    emoji \
    graphviz \
    huggingface_hub \
    jupyter \
    lxml \
    nltk \
    pytest \
    pytorch \
    regex \
    seaborn \
    scipy \
    scikit-learn \
    sentence-transformers \
    statsmodels \
    spacy \
    torchtext \
    transformers \
    xmltodict
```


## Install

You need to have `nlpia2/src/nlpia2` in your python path and some datasets downloaded into `.nlpia2-data/` for these scripts and notebooks to work.
There are two ways to make that happen:

### `pip install nlpia2`

The `pip install nlpia2` command will install the python source files within the PYTHON_PATH of your current (active) virtual environment, conda environment, or Docker container... wherever you ran that command.

The `pip install` command will also create a directory `$HOME/.nlpia2-data/` with all the data you need for `nlpia2`.

### `git clone git@gitlab.com:prosocialai/nlpia2`

If you `git clone git@gitlab.com:prosocialai/nlpia2` you will 
Or you can  then `cd nlpia2/src/nlpia2`.source code downloaded, or the nlpia2 package installed

