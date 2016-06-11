Description
===========
Calculates a number of tags in a website page

Installation
------------
You will need ``Python 2.7``.

Clone repository or download tarball and extract it, and cd to the directory.

Run ``python setup.py test`` to run tests.

Run ``python setup.py install`` to install script. Executable ``tag-counter`` will be available after.


Usage
-----
1. Create DB and schema: ``tag-counter --reset-db``
2. Get the website page and count tags from it: ``tag-counter --get http://google.com``
3. View results: ``tag-counter --view http://google.com``
4. Get help: ``tag-counter -h``
