import pandas as pd
pd.options.display.width = 120  # <1>
pd.set_option('display.max_columns', 7)

DATA_DIR = ('https://gitlab.com/tangibleai/nlpia/-/raw/master/src/nlpia/data')
url= DATA_DIR + '/toxic_comment_small.csv'
comments = pd.read_csv(url)
index = ['comment{}{}'.format(i, '!'*j) for (i,j) in zip(range(len(comments)), comments.toxic)]  # <2>
comments = pd.DataFrame(comments.values, columns=comments.columns, index=index)
mask = comments.toxic.astype(bool).values
comments['toxic'] = comments.toxic.astype(int)
"""
>>> comments.head(6)
                                                        text  toxic
comment0   you have yet to identify where my edits violat...      0
comment1   "\n as i have already said,wp:rfc or wp:ani. (...      0
comment2   your vote on wikiquote simple english when it ...      0
comment3   your stalking of my edits i've opened a thread...      0
comment4!  straight from the smear site itself. the perso...      1
comment5   no, i can't see it either - and i've gone back...      0
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

nlp = spacy.load("en_core_web_sm")

def spacy_tokenizer(sentence):
    return [token.text for token in nlp(sentence.lower())]

tfidf = TfidfVectorizer(tokenizer=spacy_tokenizer)
tfidf_docs = tfidf.fit_transform(raw_documents=comments.text).toarray()
"""
>>> tfidf_docs.shape
(5000, 25172)
>>> comments.toxic.sum()
650
"""

mask = comments.toxic.astype(bool).values  # <1>
toxic_centroid = tfidf_docs[mask].mean(axis=0) # <2>
nontoxic_centroid = tfidf_docs[~mask].mean(axis=0)

toxicity_score = tfidf_docs.dot(toxic_centroid - nontoxic_centroid)
"""
>>> toxicity_score
array([-0.01469806, -0.02007376,  0.03856095, ..., -0.01014774, -0.00344281,  0.00395752])
"""

from sklearn.preprocessing import MinMaxScaler
comments['manual_score'] = MinMaxScaler().fit_transform(toxicity_score.reshape(-1, 1))
comments['manual_predict'] = (comments.manual_score > .5).astype(int)
"""
>>> comments['toxic manual_predict manual_score'.split()].round(2).head(6)
           toxic  manual_predict  manual_score
comment0       0               0          0.41
comment1       0               0          0.27
comment2       0               0          0.35
comment3       0               0          0.47
comment4!      1               0          0.48
comment5       0               0          0.31

"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda_tfidf = LinearDiscriminantAnalysis()
lda_tfidf = lda_tfidf.fit(tfidf_docs, comments['toxic'])  # <1>
comments['tfidf_predict'] = lda_tfidf.predict(tfidf_docs)
"""
round(float(lda_tfidf.score(tfidf_docs, comments['toxic'])), 3)
0.999
"""



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tfidf_docs, \
                comments.toxic.values, test_size=0.5, random_state=271828) # <1>
lda_tfidf_train = LinearDiscriminantAnalysis(n_components=1)
lda_tfidf_train = lda_tfidf_train.fit(X_train, y_train)  # <2>
"""
round(float(lda_tfidf_train.score(X_train, y_train)), 3)
round(float(lda_tfidf_train.score(X_test, y_test)), 3)

"""

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, lda_tfidf_train.predict(X_test))
"""
array([[1261,  913],
       [ 201,  125]], dtype=int64)
"""

import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(lda_tfidf_train,X_test, y_test, cmap="Greys",
                      display_labels=['non-toxic', 'toxic'], colorbar=False)
plt.show()


from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=16, n_iter=100)  # <1>
columns = ['topic{}'.format(i) for i in range(svd.n_components)]
svd_topic_vectors = svd.fit_transform(tfidf_docs)
svd_topic_vectors = pd.DataFrame(svd_topic_vectors, columns=columns,
                  index=index)
"""
>>> svd_topic_vectors.round(3).head(6)
           topic0  topic1  topic2  topic3  ...  topic12  topic13  topic14  topic15
comment0    0.121  -0.055   0.036  -0.040  ...    0.013   -0.038    0.089    0.011
comment1    0.215   0.141  -0.006  -0.006  ...   -0.040    0.079   -0.016   -0.070
comment2    0.342  -0.200   0.044  -0.070  ...    0.059   -0.138    0.023    0.069
comment3    0.130  -0.074   0.034  -0.018  ...    0.119   -0.060    0.014    0.073
comment4!   0.166  -0.081   0.040   0.136  ...    0.066   -0.008    0.063   -0.020
comment5    0.256  -0.122  -0.055   0.082  ...    0.011    0.093   -0.083   -0.074

"""

"""
>>> list(tfidf_model.vocabulary_.items())[:5] #<1>
[('you', 18890),
 ('have', 8093),
 ('yet', 18868),
 ('to', 17083),
 ('identify', 8721)]
"""

column_nums, terms = zip(*sorted(zip(tfidf.vocabulary_.values(),
     tfidf.vocabulary_.keys())))  # <2>
"""
>>> terms
('\n', '\n ', '\n \n', '\n \n ', '\n  ')
"""
topic_term_matrix = pd.DataFrame(svd.components_, columns=terms,
                   index=['topic{}'.format(i) for i in range(16)])
"""
>>> pd.options.display.max_columns = 8
>>> topic_term_matrix.head(4).round(3)
"""


X_train_16d, X_test_16d, y_train_16d, y_test_16d = train_test_split(svd_topic_vectors, \
                                                    comments.toxic.values, test_size=0.5, random_state=271828)
lda_svd = LinearDiscriminantAnalysis(n_components=1)
lda_svd = lda_svd.fit(X_train_16d, y_train_16d)  # <2>
round(float(lda_svd.score(X_train_16d, y_train_16d)), 3)
round(float(lda_svd.score(X_test_16d, y_test_16d)), 3)

"""
from sklearn.decomposition import PCA
pca_model = PCA(n_components=16)
tfidf_docs_16d = pca_model.fit_transform(tfidf_docs)


from sklearn.model_selection import train_test_split
X_train_16d, X_test_16d, y_train_16d, y_test_16d = train_test_split(tfidf_docs_16d, \
                                                    comments.toxic.values, test_size=0.5, random_state=271828)
lda_lsa = LinearDiscriminantAnalysis(n_components=1)
lda_lsa = lda_lsa.fit(X_train_16d, y_train_16d)  # <2>
round(float(lda_lsa.score(X_train_16d, y_train_16d)), 3)
round(float(lda_lsa.score(X_test_16d, y_test_16d)), 3)
"""


