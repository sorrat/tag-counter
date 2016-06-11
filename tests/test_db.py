# -*- coding: utf-8 -*-

def test_db_insert_and_read(db):
    url = 'example.org'

    counts = [
        ('h1', 1),
        ('span', 2),
    ]
    db.insert_counts(url, counts)
    assert db.read_counts(url) == counts

    new_counts = [
        ('h1', 13),
        ('span', 17),
        ('div', 5),
    ]
    db.insert_counts(url, new_counts)
    assert sorted(db.read_counts(url)) == sorted(new_counts)
