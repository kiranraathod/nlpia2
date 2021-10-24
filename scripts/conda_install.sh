conda activate nlpia2 || conda create -n nlpia2 'python==3.8.8' && conda activate nlpia2
conda install -c pytorch -y jupyter spacy seaborn scipy scikit-learn transformers regex pytest lxml nltk pytorch torchtext xmltodict
python ./conda_install_spacy_en_core_web_md.py || python ./scripts/conda_install_spacy_en_core_web_md.py

# python -c "import spacy; import os; from pathlib import Path; nlp=spacy.load('en_core_web_sm'); modeldir=Path(nlp._path).parent.parent; files = os.listdir(modeldir); assert(any(f.startswith('en_core_web_sm') for f in files))" || python -m spacy download en_core_web_sm
# python -c "import spacy; import os; from pathlib import Path; nlp=spacy.load('en_core_web_sm'); modeldir=Path(nlp._path).parent.parent; files = os.listdir(modeldir); assert(any(f.startswith('en_core_web_md') for f in files))" || python -m spacy download en_core_web_md



