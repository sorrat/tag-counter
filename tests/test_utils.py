# -*- coding: utf-8 -*-
from tag_counter.utils import readpage, memoize


def test_memoize():
    import random

    memoized = memoize(random.random)
    assert memoized() == memoized()


def test_readpage():
    page = readpage('http://example.org')
    assert 'Example Domain' in page
