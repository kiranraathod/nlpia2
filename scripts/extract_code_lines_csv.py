#/usr/bin/env python3

from nlpia2.text_processing.extractors import *

dfs = []
for f in Path('../nlpia-manuscript/manuscript/adoc').glob('*.adoc'):
    df = pd.DataFrame(extract_tagged_code_lines(f))
    df['filepath'] = str(f)
    df['filename'] = f.name
    dfs.append(df)
df = pd.concat(dfs)
df
df.to_csv('../nlpia-manuscript/manuscript/csv/code_lines_all.csv')
mkdir ../nlpia-manuscript/manuscript/csv/
df.to_csv('../nlpia-manuscript/manuscript/csv/code_lines_all.csv')
