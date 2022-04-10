# -*- coding: utf-8 -*-

import pytest  # noqa
from nessvec.files import load_glove
import doctest
import nessvec
import nessvec.hypervec
import nessvec.util


__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_load_glove():
    # filepath=os.path.join(BIGDATA_PATH, 'GoogleNews-vectors-negative300.bin.gz')
    wv = load_glove(50, 6)
    assert len(wv) == 400000
    return wv


def test_hypervec_module():
    results = doctest.testmod(nessvec.hypervec, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0


def test_util_module():
    results = doctest.testmod(nessvec.util, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0
