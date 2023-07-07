# -*- coding: utf-8 -*-

import pytest  # noqa
import doctest
import nlpia2
import nlpia2.ch06
import nlpia2.ch06.spell  # noqa
from nlpia2.text_processing.extractors import test_file

from pathlib import Path

# ADOC_DIR = Path(__file__).parent.parent.parent / 'nlpia-manuscript' / 'manuscript' / 'adoc'
from nlpia2.constants import ADOC_DIR

CH2_PATH = Path(list(ADOC_DIR.glob('Chapter-02*'))[0])

__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_manuscript_ch2():
    results = test_file(CH2_PATH, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0
