# -*- coding: utf-8 -*-
import pytest  # noqa
import doctest
from nlpia2.text_processing.extractors import test_file

# from pathlib import Path

from nlpia2.constants import ADOC_DIR
# Path(__file__).parent.parent.parent.parent / 'nlpia-manuscript' / 'manuscript' / 'adoc'

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_manuscript_ch2(ch=2, skip=0):
    glob = f'Chapter-{ch:02d}*'
    filepaths = list(ADOC_DIR.glob(glob))
    assert len(filepaths) > 0, f'{ADOC_DIR}/{glob}'
    results = test_file(filepaths[0],
                        skip=skip,
                        verbose=True,
                        optionflags=(
                            doctest.ELLIPSIS |
                            doctest.NORMALIZE_WHITESPACE |
                            doctest.FAIL_FAST))
    assert results.failed == 0


if __name__ == '__main__':
    test_manuscript_ch2()
