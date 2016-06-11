import sqlite3

from tag_counter import settings
from tag_counter.utils import memoize


@memoize
class Db(object):
    def __init__(self):
        self.conn = sqlite3.connect(settings.DB_PATH)

    def reset_schema(self):
        self.conn.execute(
            'DROP TABLE IF EXISTS tag_counts')
        self.conn.execute(
            'CREATE TABLE tag_counts '
            '(url text, tag text, count integer)')
        self.conn.execute(
            'CREATE UNIQUE INDEX url_tag_idx '
            'ON tag_counts (url, tag)')

    def insert_counts(self, url, counts):
        values = (
            [url, tag, count]
            for tag, count in counts
        )

        self.conn.executemany(
            'REPLACE INTO tag_counts (url, tag, count) VALUES (?,?,?)',
            values)
        self.conn.commit()

    def read_counts(self, url):
        cursor = self.conn.execute(
            'SELECT tag, count FROM tag_counts WHERE url=?', [url])

        return cursor.fetchall()
