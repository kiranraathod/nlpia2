# -*- coding: utf-8 -*-
import pytest  # noqa
import doctest
from nlpia2.text_processing.extractors import test_file

from pathlib import Path

ADOC_DIR = Path(__file__).parent.parent.parent / 'nlpia-manuscript' / 'manuscript' / 'adoc'

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_manuscript_ch2(ch=2, skip=0):
    filepath = list(ADOC_DIR.glob(f'Chapter {ch:02d} -- *'))[0]
    results = test_file(filepath,
                        skip=skip,
                        verbose=True,
                        optionflags=(
                            doctest.ELLIPSIS |
                            doctest.NORMALIZE_WHITESPACE |
                            doctest.FAIL_FAST))
    assert results.failed == 0


if __name__ == '__main__':
    test_manuscript_ch2()
