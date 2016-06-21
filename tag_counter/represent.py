# -*- coding: utf-8 -*-

from tag_counter.db import Db


def print_tag_counts(url):
    counts = Db().read_counts(url)
    print format_tag_counts(counts)


def desc_by_count(counts):
    _count = lambda x: int(x[1])
    return sorted(counts, key=_count, reverse=True)


def format_tag_counts(counts):
    max_tag_length = max(len(x[0]) for x in counts) + 1

    return '\n'.join(
        '{0:{2}} {1}'.format(tag, count, max_tag_length)
        for tag, count in desc_by_count(counts))
