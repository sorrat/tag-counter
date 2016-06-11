import urllib2


def readpage(url):
    return urllib2.urlopen(url).read()


# https://wiki.python.org/moin/PythonDecoratorLibrary#Alternate_memoize_as_dict_subclass
class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


