# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import collections
from HTMLParser import HTMLParser

from tag_counter.utils import readpage
from tag_counter.db import Db


def count_tags(url):
    page = readpage(url)
    counts = count_tags_in_string(page)
    Db().insert_counts(url, counts)


def count_tags_in_string(string):
    return HtmlTagCounter().run(string).items()


class HtmlTagCounter(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.counters[tag] += 1

    def run(self, html):
        self.counters = collections.defaultdict(int)
        self.feed(html)
        return self.counters
