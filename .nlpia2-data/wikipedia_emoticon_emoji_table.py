import pandas as pd
dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_emoticons')
dfs[0]
dfs[1]
pwd
dfs[1].to_csv('code/data/wikipedia_emoticon_emoji_table.csv', index=False)
dfs[1]
ls code/data
more code/data/wikipedia_emoticon_emoji_table.csv
df = pd.read_csv('code/data/wikipedia_emoticon_emoji_table.csv')
df
