#!/usr/bin/env python
import sys
from pathlib import Path

from nlpia2.text_processing.extractors import extract_code
from nlpia2.text_processing.converters import adocs2notebooks
# from pathlib import Path

from nlpia2.constants import OFFICIAL_ADOC_DIR, BASE_DIR

if __name__ == '__main__':
    adoc_dir = OFFICIAL_ADOC_DIR
    if sys.argv[1:]:
        adoc_dir = Path(sys.argv[1])
    dest_dir = BASE_DIR / 'notebooks'
    print(adoc_dir, '->', dest_dir)
    nbs = adocs2notebooks(adoc_dir, dest_dir=dest_dir)
    dest_dir = OFFICIAL_ADOC_DIR.parent.parent / 'code' / 'notebooks'
    # for d in nbs:
    #     print(d.keys())
    #     # src = d['filepath']
    #     dest = dest_dir / src.name
    #     print(adoc_dir, '->', dest_dir)

    # Path(dest).open('w').write(Path(src).open().read())
    print('Extracting .py file from .adoc using ')
    print('  nlpia2.text_processing.extractors.extract_code():')
    print('  ' + str(extract_code()).replace('\n', '\n  '))
