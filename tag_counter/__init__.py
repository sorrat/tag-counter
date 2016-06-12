# -*- coding: utf-8 -*-
import argparse

from tag_counter.db import Db
from tag_counter.count import count_tags
from tag_counter.represent import print_tag_counts


def url_with_schema(url):
    if not url.startswith('http'):
        msg = ("Invalid URL {0!r}: no schema supplied. "
               "Perhaps you meant http://{0}?"
               .format(url))
        raise argparse.ArgumentTypeError(msg)
    else:
        return url


def cmdline_args():
    parser = argparse.ArgumentParser(description='Tag counter')
    parser.add_argument('--reset-db', action='store_true',
                        help='Reset DB to initial state. And create schema')
    parser.add_argument('--get', dest='url_to_get', type=url_with_schema,
                        help='URL of website to count tags from')
    parser.add_argument('--view', dest='url_to_view', type=url_with_schema,
                        help='View results')
    return parser.parse_args()


def main():
    args = cmdline_args()

    if args.reset_db:
        Db().reset_schema()

    if args.url_to_get:
        count_tags(args.url_to_get)

    if args.url_to_view:
        print_tag_counts(args.url_to_view)
