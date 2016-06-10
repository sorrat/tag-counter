# -*- coding: utf-8 -*-
import argparse

from tag_counter.count import count_tags
from tag_counter.represent import print_tag_counts


def cmdline_args():
    parser = argparse.ArgumentParser(description='Tag counter')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--get', dest='url_to_get',
                       help='URL of website to count tags from')
    group.add_argument('--view', dest='url_to_view',
                       help='View results')
    return parser.parse_args()


def main():
    args = cmdline_args()

    if args.url_to_get:
        count_tags(args.url_to_get)

    if args.url_to_view:
        print_tag_counts(args.url_to_view)
