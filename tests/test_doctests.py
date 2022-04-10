# -*- coding: utf-8 -*-

import pytest  # noqa
import doctest
import nlpia2
import nlpia2.ch06
import nlpia2.ch06.spell


__author__ = "Hobson Lane"
__copyright__ = "Hobson Lane"
__license__ = "mit"


def test_hypervec_module():
    results = doctest.testmod(nlpia2.ch06.spell, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0


def test_util_module():
    results = doctest.testmod(nlpia2, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0
