#!/usr/bin/env python
import sys
from pathlib import Path

# from nlpia2.text_processing.extractors import extract_code
from nlpia2.text_processing.converters import adocs2notebooks
# from nlpia2.constants import BASE_DIR as NLPIA2_BASE_DIR

# from pathlib import Path

try:
    BASE_DIR = Path(__file__).parent.parent.parent
except Exception:
    BASE_DIR = Path.cwd()
assert BASE_DIR.is_dir(), "not {BASE_DIR}.is_dir()"
assert BASE_DIR.name == 'nlpia2'

ADOC_DIR = BASE_DIR / 'manuscript' / 'adoc'
assert ADOC_DIR.is_dir(), "not {ADOC_DIR}.is_dir()"

if __name__ == '__main__':
    adoc_dir = ADOC_DIR
    if sys.argv[1:]:
        adoc_dir = Path(sys.argv[1])
    dest_dir = BASE_DIR / 'notebooks'
    print(adoc_dir, '->', dest_dir)
    nbs = adocs2notebooks(adoc_dir, dest_dir=dest_dir, glob='Chapter-*.ipynb')
    dest_dir = BASE_DIR / 'code' / 'notebooks'
    # for d in nbs:
    #     print(d.keys())
    #     # src = d['filepath']
    #     dest = dest_dir / src.name
    #     print(adoc_dir, '->', dest_dir)

    # Path(dest).open('w').write(Path(src).open().read())

    # FIXME: extract_code() is broke for adoc files without any code blocks
    # print('Extracting .py file from .adoc using ')
    # print('  nlpia2.text_processing.extractors.extract_code():')
    # print('  ' + str(extract_code()).replace('\n', '\n  '))
