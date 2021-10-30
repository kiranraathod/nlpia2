""" Notes from mob programming session Wed Oct 27, 2021 5:30 Pacific
(email engineering@tangibleai.com for details)

You need to have nlpia2/src/nlpia2 in your python path (or your CWD)
  for this to work

See [README.md](https://gitlab.com/prosocialai/nlpia2/README.md) for details.

You can `pip install nlpia2`
OR
`git clone git@gitlab.com:prosocialai/nlpia2`
then `cd nlpia2/src/nlpia2`
"""

"""
>>> from tqdm import tqdm
>>> import pandas as pd
>>> import numpy as np
>>> from sklearn.feature_extraction.text import TfidfVectorizer
>>> from sklearn.linear_model import LogisticRegression
"""
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression  # noqa
"""
>>> df = pd.read_csv('.nlpia2-data/baby-names-region.csv.gz')
>>> vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
>>> vectorizer.fit(tqdm(df['name'][istrain]))
>>> vecs = vectorizer.transform(tqdm(df['name']))
>>> vecs
"""

"""
>>> np.random.seed(451)
>>> istrain = np.random.rand(len(df)) < .
>>> istrain.sum() / len(istrain)
"""
>>> from constants import DATA_DIR
>>> DATA_DIR
....nlpia-data/
"""
from constants import DATA_DIR

df = pd.read_csv(DATA_DIR / 'baby-names-region.csv.gz')
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
vectorizer.fit(tqdm(df['name'][istrain]))
vecs = vectorizer.transform(tqdm(df['name']))

"""
>>> istrain = np.random.rand(len(df)) < .9

"""
"""
>>> model = LogisticRegression(max_iter=10000)
>>> model.fit(vecs[istrain], df['sex'][istrain], sample_weight=df['freq'][istrain])
LogisticRegression(max_iter=10000)
"""

"""
>>> names = [
...    'Maria', 'Aditi', 'Jessica', 'Olessya', 'Una', 'Hanna', 'Winnie', 'Olessya',
...    'Sylvia', 'Vish', 'Mohammed', 'Jon', 'John', 'Ted', 'Kazuma', 'Meijke', 'Kemal']
"""

model = LogisticRegression(alpha=1, max_iter=10000)
model.fit(vecs[istrain], df['sex'][istrain], sample_weight=df['freq'][istrain])
# LogisticRegression(max_iter=10000)


names = [
    'Maria', 'Aditi', 'Jessica', 'Olessya', 'Una', 'Hanna', 'Winnie', 'Olessya',
    'Sylvia', 'Vish', 'Mohammed', 'Jon', 'John', 'Ted', 'Kazuma', 'Meijke', 'Kemal']

"""
names = [
    'Maria', 'Aditi', 'Jessica', 'Olessya', 'Una', 'Hanna', 'Winnie', 'Olessya',
    'Sylvia', 'Vish', 'Mohammed', 'Jon', 'John', 'Ted', 'Kazuma', 'Meijke', 'Kemal']
>>> pd.Series(model.predict(vectorizer.transform(names)), index=names)
Maria       F
Aditi       F
Jessica     F
Olessya     F
Una         F
Hanna       F
Winnie      F
Olessya     F
Sylvia      F
Vish        M
Mohammed    M
Jon         M
John        M
Ted         M
Kazuma      F
Meijke      M
Kemal       F
dtype: object
>>> (df['name'] == 'Kazuma').sum()
0
>>> (df['name'] == 'Kaz').sum()
1
>>> df[df['name'] == 'Kaz']
    region sex  year name  count      freq
2424961     LA   M  2015  Kaz      5  0.000002
>>> model.coef_
array([[-5.56584447e-01, 5.14287250e-02, 2.69276390e-06, ...,
        -1.39283459e-04, -1.21600561e-04, -9.11513939e-05]])
>>> pd.Series(model.coef_, index=vectorizer.get_feature_names())
>>> pd.Series(model.coef_, index=vectorizer.get_feature_names()[0])
>>> index = vectorizer.get_feature_names()
>>> index
['a',
 'aa',
 'aab',
...
>>> index.shape
>>> type(index)
list
>>> pd.Series(model.coef_[0], index=vectorizer.get_feature_names())
a - 0.556584
aa     0.051429
aab    0.000003
aac    0.021992
aad    0.000415
    ...
zze - 0.000103
zzi - 0.001919
zzl - 0.000139
zzm - 0.000122
zzy - 0.000091
Length: 5986, dtype: float64
>>> coef = pd.Series(model.coef_[0], index=vectorizer.get_feature_names())
>>> coef['Kaz']
>>> coef['az']
- 0.02216603297465453
>>> coef['azu']
- 0.0003656728319935028
>>> coef['zu']
- 0.0016125466401391323
>>> coef['zum']
5.621315934940933e-06
>>> coef['uma']
0.0007642577222082215
>>> coef['ma']
- 0.2804809937613128
>>> model.intercept_
array([0.08277136])
>>> coef['z']
- 0.06687313431457634
>>> coef['u']
0.02968187895127858
>>> coef['m']
- 0.03181555148151521
>>> coef['a']
- 0.556584447334144
>>> coef['Ka']
>>> coef['K']
>>> coef.index
Index(['a', 'aa', 'aab', 'aac', 'aad', 'aaf', 'aah', 'aai', 'aaj', 'aak',
       ...
       'zyq', 'zyr', 'zys', 'zz', 'zza', 'zze', 'zzi', 'zzl', 'zzm', 'zzy'],
      dtype='object', length=5986)
>>> coef['k']
0.06634704179666573
>>> coef['ka']
- 0.18216581846670435
>>> coef['kaz']
3.0355019959739112e-05
>>> kazvec = vectorizer.transform('Kazuma')
>>> kazvec = vectorizer.transform(['Kazuma'])
>>> coef[kazvec != 0]
>>> kazvec[kazvec != 0]
matrix([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
         0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
         0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> coef[kazvec != 0]
>>> kazvec[kazvec != 0]
matrix([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
         0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
         0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> kazvec[kazvec != 0].reshape()
>>> kazvec[kazvec != 0].reshape(kazvec.shape[1])
>>> kazvec[kazvec != 0].reshape((kazvec.shape[1],))
>>> kazvec[kazvec != 0].reshape((14,))
matrix([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
         0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
         0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> kazvec[kazvec != 0].flatten()
matrix([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
         0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
         0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> kazvec[kazvec != 0].ravel()
matrix([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
         0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
         0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> kazvec[kazvec != 0].astype(np.array)
>>> np.array(kazvec[kazvec != 0])
array([[0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
        0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
        0.32475817, 0.17116995, 0.31639993, 0.49863121]])
>>> np.array(kazvec[kazvec != 0])[0]
array([0.10064136, 0.24160243, 0.36640437, 0.11589853, 0.1563424,
       0.40920386, 0.09844366, 0.12768782, 0.12058102, 0.26053805,
       0.32475817, 0.17116995, 0.31639993, 0.49863121])
>>> coef
a - 0.556584
aa     0.051429
aab    0.000003
aac    0.021992
aad    0.000415
    ...
zze - 0.000103
zzi - 0.001919
zzl - 0.000139
zzm - 0.000122
zzy - 0.000091
Length: 5986, dtype: float64
>>> coef.values[np.array(kazvec[kazvec != 0])[0] > 0]
>>> coef.values[kazvec != 0]
>>> type(kazvec != 0)
scipy.sparse.csr.csr_matrix
>>> (kazvec != 0).todense()
matrix([[True, False, False, ..., False, False, False]])
>>> np.array((kazvec != 0).todense())[0]
array([True, False, False, ..., False, False, False])
>>> coef[np.array((kazvec != 0).todense())[0] != 0]
a - 0.556584
az - 0.022166
azu - 0.000366
k      0.066347
ka - 0.182166
kaz    0.000030
m - 0.031816
ma - 0.280481
u      0.029682
um - 0.008430
uma    0.000764
z - 0.066873
zu - 0.001613
zum    0.000006
dtype: float64
>>> model.predict(kazvec)
array(['F'], dtype=object)
>>> model.predict_proba(kazvec)
array([[0.51219282, 0.48780718]])
>>> pd.Series(model.predict_proba(vectorizer.transform(names))[:, 1], index=names)
Maria       0.381240
Aditi       0.477269
Jessica     0.483249
Olessya     0.499430
Una         0.481148
Hanna       0.426783
Winnie      0.484074
Olessya     0.499430
Sylvia      0.484732
Vish        0.516631
Mohammed    0.569390
Jon         0.619116
John        0.678048
Ted         0.546004
Kazuma      0.487807
Meijke      0.528277
Kemal       0.494326
dtype: float64
>>> model.classes_
array(['F', 'M'], dtype=object)
>>> hist
>>> hist - o - p - f kemal_kazuma_labeled_female.md
"""
