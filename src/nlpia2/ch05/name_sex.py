import pandas as pd
pd.read_html('https://www.ssa.gov/oact/babynames/decades/names2010s.html')
for year in range(1940, 2020, 10):
    print(year)
for year in range(1940, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
dfs = []
for year in range(1940, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    dfs.extend(pd.read_html(url))
len(dfs)
df = pd.concat(dfs)
len(df)
df.describe()
df.describe(include='all')
for year in range(1800, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    dfs.extend(pd.read_html(url))
for year in range(1800, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    try:
        dfs.extend(pd.read_html(url))
    except HTTPError:
        pass
for year in range(1800, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    try:
        dfs.extend(pd.read_html(url))
    except pd.HTTPError:
        pass
import lxml
from lxml import *
who
dir(lxml)
dir(lxml.html)
dir(lxml.html.defs)
dir(lxml.html)
dir(lxml.html.Classes)
dir(lxml.html.open_http_urllib)
dir(pd)
dir(pd.util)
dir(pd.util._exceptions)
for year in range(1800, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    try:
        dfs.extend(pd.read_html(url))
    except Exception:
        pass
len(dfs)
df2 = pd.concat(dfs)
df2.describe(include='all')
pd.options.display.max_columns = 1000
df2.describe(include='all')
df.head()
df.sample(20)
for year in range(1800, 2020, 10):
    print(year)
    url = f'https://www.ssa.gov/oact/babynames/decades/names{year}s.html'
    print(url)
    try:
        dfs.extend(pd.read_html(url))
        for df in dfs:
            df['decade'] = year
    except Exception:
        pass
    sleep(2)
!unzip / home / hobs / Downloads / names.zip
pd.read_csv('Names_2010Census.csv')
names = _
names.describe(include='all')
!unzip / home / hobs / Downloads / len - us - first - names - database.zip
pd.read_csv('len-us-first-names-database/original/Common_Surnames_Census_2000.csv ')
pd.read_csv('len-us-first-names-database/original/Common_Surnames_Census_2000.csv')
pd.read_csv('len-us-first-names-database/data/ssa_names_db.csv')
pd.read_csv('/home/hobs/Downloads/baby-names-state.csv')
df = _
df.to_csv('/home/hobs/.nlpia2-data/baby-names-state.csv.gz', index=False)
df.describe(include='all')
pd.read_csv('/home/hobs/Downloads/baby-names-territories.csv')
dft = _
dft['state_abb'] = dft['territory_code']
del dft['territory_code']
dft.head()
df.head()
df = pd.concat([df, dft])
df.head()
df.describe(include='all')
dft.describe(include='all')
df['name'].apply(lambda s: ' ' in s).sum()
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
vectorizer.fit(df['name'])

df = pd.read_csv('.nlpia2-data/baby-names-region.csv.gz')
df['freq'] = 0.
for y in df['year'].unique():
    g = df[y == df['year']]
    tot = g['count'].sum()
    mask = y == df['year']
    df['freq'][mask] = df['count'][mask] / df['count'][mask].values.sum()
    print(y, tot, df['freq'][mask].sum())
df['freq'].sum().round(10)
df['year'].nunique()
df.to_csv('.nlpia2-data/baby-names-region.csv.gz', index=False)

df.head()
df.columns = list(df.columns)[:-1] + ['frequency']
model = LogisticRegression(class_weight=df['frequency'])
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
vectorizer.fit(df['name'])
vecs = vectorizer.transform(df['name'])
istrain = np.random.rand(len(vecs)) < .9
import numpy as np
istrain = np.random.rand(len(vecs)) < .9
istrain = np.random.rand(vecs.shape[0]) < .9
X_train = vecs[istrain]
y_train = df['sex'][istrain]
model.fit(X_train, y_train)
istrain.shape
y_train.head()
model.fit(X_train.values, y_train.values)
type(X_train)
model.fit(vecs, df['sex'].values)
model.fit(vecs, (df['sex'].values == 'F'))
sex = df['sex'].values == 'F'
sex.sum()
sex.sum() / len(sex)
model = LogisticRegression()
model.fit(vecs, df['sex'])
LogisticRegression?
LogisticRegression?
model.fit(vecs, df['sex'], sample_weight=df['frequency'])
model = LogisticRegression(class_weight=df10000['count'])
model.fit(vecs, df['sex'][istrain], sample_weight=df['frequency'][istrain])
model.fit(vecs[istrain], df['sex'][istrain], sample_weight=df['frequency'][istrain])
df.columns = list(df.columns)[:-1] + ['freq']
model.fit(vecs[istrain], df['sex'][istrain], sample_weight=df['freq'][istrain])
model.score(vecs[istrain], df['sex'][istrain], sample_weight=df['freq'][istrain])
model.score(vecs[~istrain], df['sex'][~istrain], sample_weight=df['freq']~[istrain])
model.score(vecs[~istrain], df['sex'][~istrain], sample_weight=df['freq'][~istrain])
model.predict(vectorizer.transform(['Hobson', 'Maria', 'Aditi', 'Vish', 'Jessica']))
names = ['Hobson', 'Maria', 'Aditi', 'Vish', 'Jessica', 'Mohammed', 'Olessya']
pd.Series(model.predict(vectorizer.transform(names)), index=names)
names = ['Maria', 'Aditi', 'Jessica', 'Olessya', 'Una', 'Hanna', 'Winnie', 'Olessya',
         'Sylvia', 'Vish', 'Mohammed', 'Jon', 'John', 'Ted', 'Kazuma', 'Meijke']
pd.Series(model.predict(vectorizer.transform(names)), index=names)
from torch import nn
history - o - p - f src / nlpia2 / ch05 / name_sex.md
history - f src / nlpia2 / ch05 / name_sex.py
