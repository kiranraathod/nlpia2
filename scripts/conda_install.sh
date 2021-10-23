conda create -n nlpia2 'python==3.8.8'
conda activate nlpia2
conda install jupyter spacy seaborn scipy scikit-learn transformers regex pytest
# conda install nltk
conda install -c pytorch pytorch torchtext
python spacy download en_core_web_sm
python spacy download en_core_web_md


