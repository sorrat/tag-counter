import os

import pytest


@pytest.fixture
def db(monkeypatch):
    from tag_counter import settings
    from tag_counter.db import Db

    test_db_path = os.path.join(settings.ROOT_DIR, 'tests/test.db')
    monkeypatch.setattr('tag_counter.settings.DB_PATH', test_db_path)

    test_db = Db()
    test_db.reset_schema()
    return test_db
