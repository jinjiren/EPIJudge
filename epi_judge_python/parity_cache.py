from test_framework import generic_test


def sub_parity(x, length, cache):
    if x in cache:
        return cache[x]
    while length > 1:
        # note that we need to use `//` here, otherwise length will be `float`,
        # and you get "unsupported operand type(s) for >>: 'int' and 'float'"
        # I believe this is specific to python3
        length //= 2
        x ^= x >> length
    cache[x] = x & 1
    return x & 1

def parity(x):
    from operator import xor
    from functools import reduce
    length = 16
    cache = dict()

    result = 0
    for i in range(64 // length):
        print(hex(2 ** length - 1))
        result ^= sub_parity(x >> (i * length) & (2 ** length - 1), length, cache)

    return result



if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity_cache.py", 'parity.tsv', parity))
