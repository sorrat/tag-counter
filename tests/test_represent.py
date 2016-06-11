# -*- coding: utf-8 -*-
import random

from tag_counter.represent import format_tag_counts


def test_format_tag_counts():
    counts = [
        ('html', 1),
        ('head', 1),
        ('body', 1),
        ('meta', 9),
        ('style', 1),
        ('div', 13),
        ('h1', 3),
        ('p', 2),
        ('a', 10),
    ]
    random.shuffle(counts)

    first_line = format_tag_counts(counts).splitlines()[0]
    assert first_line.startswith('div')
    assert first_line.endswith('13')
