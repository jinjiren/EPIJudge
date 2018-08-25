from test_framework import generic_test


def parity(x):
    length = 64
    while length > 1:
        # note that we need to use `//` here, otherwise length will be `float`,
        # and you get "unsupported operand type(s) for >>: 'int' and 'float'"
        # I believe this is specific to python3
        length //= 2
        x ^= x >> length
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
