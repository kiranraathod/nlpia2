import pandas as pd


## Load Data
true = pd.read_csv()
fake = pd.read_csv('Fake.csv')

true['label'] = 1
fake['label'] = 0

fake.drop(labels=['subject','date', 'text'],axis=1,inplace=True)
true.drop(labels=['subject','date', 'text'],axis=1,inplace=True)

data = pd.concat([fake,true])

data.head()

## Clean the text