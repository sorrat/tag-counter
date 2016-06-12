# -*- coding: utf-8 -*-
from helpers import assert_lists_equal


def test_db_insert_and_read(db):
    url = 'example.org'

    counts = [
        ('h1', 1),
        ('span', 2),
        ('div', 5),
    ]
    db.insert_counts(url, counts)

    assert_lists_equal(
        counts,
        db.read_counts(url)
    )

    new_counts = [
        ('h1', 13),
        ('span', 17),
    ]
    db.insert_counts(url, new_counts)

    assert_lists_equal(
        new_counts,
        db.read_counts(url)
    )
