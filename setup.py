# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def read(filepath):
    return open(filepath).read()


setup(
    name = 'tag-counter',
    description = 'Calculates a number of tags in website page',
    long_description = read('README.rst'),
    version = 0.1,
    packages = find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts':
            ['tag-counter=tag_counter:main'],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
