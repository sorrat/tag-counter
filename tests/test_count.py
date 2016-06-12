from tag_counter.count import count_tags, count_tags_in_string
from helpers import assert_lists_equal


EXAMPLE_PAGE = '''
<!doctype html>
<html>
  <head>
    <title>Example Domain</title>
    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <style type="text/css">
    </style>
  </head>

  <body>
    <div>
      <h1>Example Domain</h1>
      <p>This domain is established to be used for illustrative examples in documents</p>
      <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
  </body>
</html>
'''

EXAMPLE_PAGE_TAG_COUNTS = (
    ('html', 1),
    ('head', 1),
    ('title', 1),
    ('meta', 2),
    ('style', 1),
    ('body', 1),
    ('div', 1),
    ('h1', 1),
    ('p', 2),
    ('a', 1),
)


def test_count_tags_in_string():
    assert_lists_equal(
        EXAMPLE_PAGE_TAG_COUNTS,
        count_tags_in_string(EXAMPLE_PAGE)
    )


def test_count_tags(db, monkeypatch):
    url = 'http://example.org'

    assert db.read_counts(url) == []  # db is empty

    monkeypatch.setattr('tag_counter.count.readpage', lambda url: EXAMPLE_PAGE)
    count_tags(url)

    assert_lists_equal(
        EXAMPLE_PAGE_TAG_COUNTS,
        db.read_counts(url)
    )
