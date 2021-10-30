# neither year nor len are statistically significant predictors of sex
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression  # , Lasso

DATA_DIR = Path('.nlpia2-data')
df = pd.read_csv(DATA_DIR / 'baby-names-region.csv.gz')

df = df.sample(10_000, random_state=1989)
np.random.seed(451)
istrain = np.random.rand(len(df)) < .9
df['len'] = df['name'].str.len()
model = LogisticRegression(class_weight='balanced', max_iter=2000)
model.fit(df[['len', 'year']][istrain], df['sex'][istrain], sample_weight=df['count'][istrain])
model.score(df[['len', 'year']][istrain], df['sex'][istrain], sample_weight=df['count'][istrain])
model.score(df[['len', 'year']][~istrain], df['sex'][~istrain], sample_weight=df['count'][~istrain])

y_test = df['sex'][~istrain]
y_test_pred = model.predict(df[['len', 'year']][~istrain])
df_plot = pd.DataFrame()
df_plot['female'] = y_test
df_plot['female_pred'] = y_test_pred
y_test_proba = model.predict_proba(df[['len', 'year']][~istrain])
df_plot['female_proba'] = y_test_proba[:, 1]
df_plot.sample(30)
