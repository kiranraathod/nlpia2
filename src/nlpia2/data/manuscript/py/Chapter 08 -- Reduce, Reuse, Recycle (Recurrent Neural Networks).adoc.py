tok = list(nlp('Hello world!'))[0]
tags = {k: getattr(tok, k) for k in dir(tok) if not k.startswith('_')}
tags = pd.Series({k: v for k, v in tags.items() if not str(v).startswith('<')})
tags.sample(10)  # <1>
asciify("O’Néàl")
repo = 'tangibleai/nlpia2'
filepath = 'src/nlpia2/data/surname_nationalities.csv'
suffix = '?inline=false'  # <1> 
url = f"https://gitlab.com/{repo}/-/raw/main/{filepath}{suffix}"
df = pd.read_csv(url, columns=['surname', 'nationality'])
df['nationality'].nunique()
fraction_unique = {}
for i, g in df.groupby('nationality'):
    fraction_unique[i] = g['surname'].nunique() / len(g)
pd.Series(fraction_unique).sort_values().head(7)
g = df[df['nationality'] == 'Arabic']
len(g)
g['name'].sort_values()
df.groupby('surname')
overlap = {}
for i, g in df.groupby('surname'):
    n = g['nationality'].nunique()
    if n > 1:
        overlap[i] = {'nunique': n, 'unique': list(g['nationality'].unique())}
overlap.sort_values('nunique', ascending=False)
%run classify_name_nationality.py
model.predict_category("Khalid")
predicitons = topk_predictions(model, 'Khalid', topk=4)
predictions
predictions = topk_predictions(model, 'Khalid', topk=4)
predictions['likelihood'] = np.exp(predictions['log_loss'])
predictions
num_eos = sum([vocab.idx2word[i] == '<eos>' for i in corpus.train.numpy()])
num_eos
num_unk = sum([vocab.idx2word[i] == '<unk>' for i in corpus.train.numpy()])
num_unk
num_normal = sum([
    vocab.idx2word[i] not in ('<unk>', '<eos>')
    for i in corpus.train.numpy()])
num_normal
num_unk / (num_normal + num_eos + num_unk)
