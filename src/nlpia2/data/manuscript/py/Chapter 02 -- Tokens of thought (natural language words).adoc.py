text = ("Trust me, though, the words were on their way, and when "
        "they arrived, Liesel would hold them in her hands like "
        "the clouds, and she would wring them out, like the rain.")
tokens = text.split()
tokens[:8]
import re
pattern = r'\w+(?:\'\w+)?|[^\w\s]'  # <1>
texts = [text]
texts.append("There's no such thing as survival of the fittest. "
             "Survival of the most adequate, maybe.")
tokens = list(re.findall(pattern, texts[-1]))
tokens[:8]
tokens[8:16]
tokens[16:]
import numpy as np  # <1>
vocab = sorted(set(tokens))  # <2>
' '.join(vocab[:12])  # <3>
num_tokens = len(tokens)
num_tokens
vocab_size = len(vocab)
vocab_size
import spacy
spacy.cli.download('en_core_web_sm')  # <1>
nlp = spacy.load('en_core_web_sm')
doc = nlp(texts[-1])
type(doc)
tokens = [tok.text for tok in doc]
tokens[:9]
tokens[9:17]
from spacy import displacy
sentence = list(doc.sents)[0] # <1>
displacy.serve(sentence, style="dep")
!firefox 127.0.0.1:5000
import spacy
f = 'Chapter 02 -- Tokens of thought (natural language words).adoc'
nlp = spacy.load('en_core_web_sm')
%timeit nlp(text)  # <1>
text = open(f).read()
len(text)
doc = nlp(doc)
len(list(doc))
len(doc) / 4.67
nlp.pipe_names  # <1>
nlp = spacy.load('en_core_web_sm', disable=nlp.pipe_names)
%timeit nlp(text)
from nltk.tokenize import word_tokenize
%timeit word_tokenize(text)
len(word_tokenize(text))
pattern = r'\w+(?:\'\w+)?|[^\w\s]'
tokens = re.findall(pattern, text)  # <1>
len(tokens)
%timeit re.findall(pattern, text)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(ngram_range=(1, 2), analyzer='char')
vectorizer.fit(texts)
vocab = vectorizer.get_feature_names()
vocab[:7]
vectors = vectorizer.transform(texts)
df = pd.DataFrame(vectors.todense(), columns=vocab)
df.index = [t[:8] + '...' for t in texts]
df = df.T
df['total'] = df.T.sum()
df
df.sort_values('total').tail()
df['n'] = [len(tok) for tok in vocab]
df[df['n'] > 1].sort_values('total').tail()
text = 'Hiking home now'
text.startswith('Hi')
pattern = r'\w+(?:\'\w+)?|[^\w\s]'  # <1>
'Hi' in re.findall(pattern, text)  # <2>
'Hi' == re.findall(pattern, text)[0]  # <3>
import pandas as pd
onehot_vectors = np.zeros(
    (len(tokens), vocab_size), int)  # <1>
for i, word in enumerate(tokens):
    onehot_vectors[i, vocab.index(word)] = 1  # <2>
df_onehot = pd.DataFrame(onehot_vectors, columns=vocab)
df_onehot.shape
df_onehot.iloc[:,:8].replace(0, '')  # <3>
bow = sorted(set(re.findall(pattern, text)))
bow[:9]
bow[9:19]
bow[19:27]
v1 = pd.np.array([1, 2, 3])
v2 = pd.np.array([2, 3, 4])
v1.dot(v2)
(v1 * v2).sum()  # <1>
sum([x1 * x2 for x1, x2 in zip(v1, v2)])  # <2>
df = df.T
df.sent0.dot(df.sent1)
df.sent0.dot(df.sent2)
df.sent0.dot(df.sent3)
[(k, v) for (k, v) in (df.sent0 & df.sent3).items() if v]
from nltk.tokenize import TreebankWordTokenizer
texts.append("""
  If conscience and empathy were impediments to the advancement of
  self-interest, then we would have evolved to be amoral sociopaths.
  """  # <1>
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(texts[-1])[:6]
tokens[:8]
tokens[8:16]
tokens[16:]
import spacy
spacy.cli.download("en_core_web_sm")  # <1>
nlp = spacy.load("en_core_web_sm")   # <2>
doc = nlp("Monticello wasn't designated as UNESCO World Heritage\
  Site until 1987.")  # <3>
tokens = [token.text for token in doc]
tokens
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Nice guys finish first."  # <1>
doc = nlp(text)
for token in doc:
    print(f"{token.text:<11}{token.pos_:<10}{token.dep:<10}")
seg_list = jieba.cut("西安是一座举世闻名的文化古城") # <1>
list(seg_list)
import jieba
seg_list = jieba.cut("西安是一座举世闻名的文化古城", cut_all=True)  # <1>
list(seg_list)
seg_list = jieba.cut_for_search("西安是一座举世闻名的文化古城")
list(seg_list)
import jieba
from jieba import posseg
words = posseg.cut("西安是一座举世闻名的文化古城")
jieba.enable_paddle()  # <1>
words = posseg.cut("西安是一座举世闻名的文化古城",use_paddle=True)
list(words)
import spacy
spacy.cli.download("zh_core_web_sm")
nlpzh = spacy.load("zh_core_web_sm")
doc = nlpzh("西安是一座举世闻名的文化古城")
[(tok.text, tok.pos_) for tok in doc]
from nltk.tokenize.casual import casual_tokenize
texts.append("@rickrau mind BLOOOOOOOOWWWWWN by latest lex :*) !!!!!!!!")
casual_tokenize(texts[-1], reduce_len=True)
import requests
url = ("https://gitlab.com/tangibleai/nlpia/-/raw/master/"
       "src/nlpia/data/stopword_lists.json")
response = requests.get(url)
stop_words = response.json()['exhaustive']  # <1>
tokens = 'the words were just as I remembered them'.split()  # <2>
tokens_without_stopwords = [x for x in tokens if x not in stop_words]
print(tokens_without_stopwords)
import nltk
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
len(stop_words)
stop_words[:7]
[sw for sw in stopwords if len(sw) == 1]
resp = requests.get(url)
len(resp.json()['exhaustive'])
len(resp.json()['sklearn'])
len(resp.json()['spacy'])
len(resp.json()['nltk'])
len(resp.json()['reuters'])
tokens = ['House', 'Visitor', 'Center']
normalized_tokens = [x.lower() for x in tokens]
print(normalized_tokens)
def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$',
        word)[0][0].strip("'") for word in phrase.lower().split()])
stem('houses')
stem("Doctor House's calls")
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
' '.join([stemmer.stem(w).strip("'") for w in
  "dish washer's fairly washed dishes".split()])
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')
' '.join([stemmer.stem(w).strip("'") for w in
  "dish washer's fairly washed dishes".split()])
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("better")  # <1>
lemmatizer.lemmatize("better", pos="a")  # <2>
lemmatizer.lemmatize("good", pos="a")
lemmatizer.lemmatize("goods", pos="a")
lemmatizer.lemmatize("goods", pos="n")
lemmatizer.lemmatize("goodness", pos="n")
lemmatizer.lemmatize("best", pos="a")
stemmer.stem('goodness')
import spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp("better good goods goodness best")
for token in doc:
print(token.text, token.lemma_)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()
sa.lexicon  # <1>
[(tok, score) for tok, score in sa.lexicon.items()
  if " " in tok]  # <4>
sa.polarity_scores(text=\
  "Python is very readable and it's great for NLP.")
sa.polarity_scores(text=\
  "Python is not a bad choice for most applications.")
corpus = ["Absolutely perfect! Love it! :-) :-) :-)",
          "Horrible! Completely useless. :(",
          "It was OK. Some good and some bad things."]
for doc in corpus:
    scores = sa.polarity_scores(doc)
    print('{:+}: {}'.format(scores['compound'], doc))
from nlpia.data.loaders import get_data
movies = get_data('hutto_movies')
movies.head().round(2)
movies.describe().round(2)
import pandas as pd
pd.set_option('display.width', 75)  # <1>
from nltk.tokenize import casual_tokenize  # <2>
bags_of_words = []
from collections import Counter  # <3>
for text in movies.text:
    bags_of_words.append(Counter(casual_tokenize(text)))
df_bows = pd.DataFrame.from_records(bags_of_words)  # <4>
df_bows = df_bows.fillna(0).astype(int)  # <5>
df_bows.shape  # <6>
df_bows.head()
df_bows.head()[list(bags_of_words[0].keys())]
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb = nb.fit(df_bows, movies.sentiment > 0)  # <1>
movies['predicted_sentiment'] = (
  nb.predict_proba(df_bows))[:, 1] * 8 - 4  # <2>
movies['error'] = (movies.predicted_sentiment - movies.sentiment).abs()
movies.error.mean().round(1)
movies['''sentiment predicted_sentiment sentiment_ispositive\
  predicted_ispositive'''.split()].head(8)
(movies.predicted_ispositive ==
  movies.sentiment_ispositive).sum() / len(movies)
products = pd.read_csv('https://proai.org/product-reviews.csv.gz')
for text in products.text:
    bags_of_words.append(Counter(casual_tokenize(text)))
df_product_bows = pd.DataFrame.from_records(bags_of_words)
df_product_bows = df_product_bows.fillna(0).astype(int)
df_all_bows = df_bows.append(df_product_bows)
df_all_bows.columns  # <1>
df_product_bows = df_all_bows.iloc[len(movies):][df_bows.columns]  # <2>
df_product_bows.shape
df_bows.shape  # <3>
products['sentiment_ispositive'] = (products.sentiment > 0).astype(int)
products['predicted_ispositive'] = nb.predict(df_product_bows).astype(int)
products.head()
(products.predicted_ispositive == products.sentiment_ispositive).sum() / len(products)
