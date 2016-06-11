# -*- coding: utf-8 -*-

from tag_counter.db import Db


def print_tag_counts(url):
    counts = Db().read_counts(url)
    print format_tag_counts(counts)


def second(items):
    return items[1]


def reverse_by_second(counts):
    return sorted(counts, key=lambda array: int(array[1]), reverse=True)


def format_tag_counts(counts):
    second = lambda items: items[0]
    max_tag_length = max(len(x[0]) for x in counts) + 1

    return '\n'.join(
        '{0:{2}} {1}'.format(tag, count, max_tag_length)
        for tag, count in reverse_by_second(counts))
