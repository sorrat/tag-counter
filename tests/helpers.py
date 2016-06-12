def assert_lists_equal(a, b):
    a = sorted(tuple(x) for x in a)
    b = sorted(tuple(x) for x in b)
    assert a == b
