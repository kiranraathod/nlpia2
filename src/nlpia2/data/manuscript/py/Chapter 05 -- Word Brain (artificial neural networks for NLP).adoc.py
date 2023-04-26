np.random.seed(451)
tokens = "green egg egg ham ham ham spam spam spam spam".split()
bow = Counter(tokens)
x = pd.Series(bow)
x
x1, x2, x3, x4 = x
x1, x2, x3, x4
w0 = np.round(.1 * np.random.randn(), 2)
w0
w1, w2, w3, w4 = (.1 * np.random.randn(len(x))).round(2)
w1, w2, w3, w4
x = np.array([1, x1, x2, x3, x4])  # <1>
w = np.array([w0, w1, w2, w3, w4])  # <2>
y = np.sum(w * x) + 1.0 * x0  # <3>
y
threshold = 0.0
y = int(y > threshold)
threshold = 0.5
import pandas as pd
import numpy as np
pd.options.display.max_rows = 7
np.random.seed(451)
df = pd.read_csv('https://proai.org/baby-names-us.csv.gz')  # <1>
df = df.sample(10_000)
df
df = df.set_index(['name', 'sex'])
groups = df.groupby(['name', 'sex'])
counts = groups['count'].sum()
counts
counts[('Maria',)]
counts[('Avi',)]  # <1>
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(use_idf=False,  # <1>
    analyzer='char', ngram_range=(1, 3))  # <2>
vectorizer
df = pd.DataFrame([list(tup) for tup in counts.index.values],
                  columns=['name', 'sex'])
df['count'] = counts.values
df
df['istrain'] = np.random.rand(len(df)) < .9
df
df.index = pd.MultiIndex.from_tuples(
    zip(df['name'], df['sex']), names=['name_', 'sex_'])
df
df_most_common = {}  # <1>
for name, group in df.groupby('name'):
    row_dict = group.iloc[group['count'].argmax()].to_dict()
    df_most_common[(name, row_dict['sex'])] = row_dict
df_most_common = pd.DataFrame(df_most_common).T  # <2>
df_most_common['istest'] = ~df_most_common['istrain'].astype(bool)
df_most_common
istest = ~df_most_common['istrain'].astype(bool)
df_most_common['istest'] = istest
print(df_most_common)
df['istest'] = df_most_common['istest'].fillna(False)
istestisna = df['istest'].isna()
istrain = ~(df['istest'][~istestisna]).fillna(False)
df['istrain'] = istrain
df['istrain'].sum() / len(df)
df['istest'].sum() / len(df)
(df['istrain'] + df['istest']).sum() / len(df)
unique_names = df[istrain]['name'].unique()
vecs = vectorizer.fit_transform(unique_names)
vecs
vecs = pd.DataFrame(vecs.toarray())
vecs.columns = vectorizer.get_feature_names_out()
vecs.index = unique_names
vecs.iloc[:,:7]
vectorizer = TfidfVectorizer(analyzer='char',
   ngram_range=(1, 3), use_idf=False, lowercase=False)  # <1>
vecs = vectorizer.fit_transform(unique_names)
vecs = pd.DataFrame(vecs.toarray())
vecs.columns = vectorizer.get_feature_names_out()
vecs.index = unique_names
vecs.iloc[:,:5]
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
import pandas as pd
import re
dfs = pd.read_html('https://en.wikipedia.org/wiki/'
    + 'Comparison_of_deep-learning_software')
df = dfs[0]
import numpy as np
example_input = [1, .2, .1, .05, .2]
example_weights = [.2, .12, .4, .6, .90]
input_vector = np.array(example_input)
weights = np.array(example_weights)
bias_weight = .2
activation_level = np.dot(input_vector, weights) +\
    (bias_weight * 1)  # <1>
activation_level
threshold = 0.5
if activation_level >= threshold:
   perceptron_output = 1
else:
   perceptron_output = 0
perceptron_output
expected_output = 0
new_weights = []
for i, x in enumerate(example_input):
    new_weights.append(weights[i] + (expected_output -\
        perceptron_output) * x)  # <1>
weights = np.array(new_weights)
example_weights  # <2>
weights  # <3>
sample_data = [[0, 0],  # False, False
               [0, 1],  # False, True
               [1, 0],  # True, False
               [1, 1]]  # True, True
expected_results = [0,  # (False OR False) gives False
                    1,  # (False OR True ) gives True
                    1,  # (True  OR False) gives True
                    1]  # (True  OR True ) gives True
activation_threshold = 0.5
from random import random
import numpy as np
weights = np.random.random(2)/1000  # Small random float 0 < w < .001
weights
bias_weight = np.random.random() / 1000
bias_weight
for idx, sample in enumerate(sample_data):
    input_vector = np.array(sample)
    activation_level = np.dot(input_vector, weights) +\
        (bias_weight * 1)
    if activation_level > activation_threshold:
        perceptron_output = 1
    else:
        perceptron_output = 0
    print('Predicted {}'.format(perceptron_output))
    print('Expected: {}'.format(expected_results[idx]))
    print()
for iteration_num in range(5):
    correct_answers = 0
    for idx, sample in enumerate(sample_data):
        input_vector = np.array(sample)
        weights = np.array(weights)
        activation_level = np.dot(input_vector, weights) +\
            (bias_weight * 1)
        if activation_level > activation_threshold:
            perceptron_output = 1
        else:
            perceptron_output = 0
        if perceptron_output == expected_results[idx]:
            correct_answers += 1
        new_weights = []
        for i, x in enumerate(sample):  # <1>
            new_weights.append(weights[i] + (expected_results[idx] -\
                perceptron_output) * x)
        bias_weight = bias_weight + ((expected_results[idx] -\
            perceptron_output) * 1)  # <2>
        weights = np.array(new_weights)
    print('{} correct answers out of 4, for iteration {}'\
        .format(correct_answers, iteration_num))
import numpy as np
from keras.models import Sequential  # <1>
from keras.layers import Dense, Activation  # <2>
from keras.optimizers import SGD  # <3>
x_train = np.array([[0, 0],
                    [0, 1],
                    [1, 0],
                    [1, 1]])  # <4>
y_train = np.array([[0],
                    [1],
                    [1],
                    [0]])  # <5>
model = Sequential()
num_neurons = 10  # <6>
model.add(Dense(num_neurons, input_dim=2))  # <7>
model.add(Activation('tanh'))
model.add(Dense(1))  # <8>
model.add(Activation('sigmoid'))
model.summary()
sgd = SGD(lr=0.1)
model.compile(loss='binary_crossentropy', optimizer=sgd,
    metrics=['accuracy'])
model.predict(x_train)
model.predict_classes(x_train)
model.predict(x_train)
import h5py
model_structure = model.to_json()  # <1>
with open("basic_model.json", "w") as json_file:
    json_file.write(model_structure)
model.save_weights("basic_weights.h5")  # <2>
