import json
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
            '(url text PRIMARY KEY, counts text)')

    def insert_counts(self, url, counts):
        counts_dump = json.dumps(counts)
        self.conn.execute(
            'REPLACE INTO tag_counts (url, counts) VALUES (?,?)',
            [url, counts_dump])
        self.conn.commit()

    def read_counts(self, url):
        cursor = self.conn.execute(
            'SELECT counts FROM tag_counts WHERE url=?', [url])

        record = cursor.fetchone()
        return json.loads(record[0]) if record else []
