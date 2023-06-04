#/usr/bin/env python3

from nlpia2.text_processing.extractors import *

dfs = []
for f in Path('../nlpia-manuscript/manuscript/adoc').glob('*.adoc'):
    df = pd.DataFrame(extract_tagged_code_lines(f))
    df['filepath'] = str(f)
    df['filename'] = f.name
    dfs.append(df)
df = pd.concat(dfs)
datadir = Path('../nlpia-manuscript/manuscript/csv/')
datadir.mkdir(exist_ok=True)
df.to_csv(datadir / 'code_lines_all.csv')

