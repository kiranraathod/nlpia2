# -*- coding: utf-8 -*-
import doctest
from nlpia2.text_extractors import test_file

from pathlib import Path

ADOC_DIR = Path(__file__).parent.parent.parent / 'nlpia-manuscript' / 'manuscript' / 'adoc'

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_chapter(ch=2):
    f""" Test Chapter {ch} """
    filepath = list(ADOC_DIR.glob(f'Chapter {ch:02d} -- *'))[0]
    results = test_file(filepath, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0


def test_all(chapters=range(1, 13)):
    for ch in chapters:
        test_chapter(ch=ch)
