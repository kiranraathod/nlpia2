import pytest  # noqa
import doctest
import nlpia2
import nlpia2.ch06
import nlpia2.ch06.spell


def test_spell():
    results = doctest.testmod(nlpia2.ch06.spell, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0


def test_nlpia2_package():
    results = doctest.testmod(nlpia2, optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE))
    assert results.failed == 0
