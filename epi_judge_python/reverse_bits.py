from test_framework import generic_test


def reverse_bits(x):
    x = '{:064b}'.format(x)
    x = ''.join(reversed(x))
    return int(x, 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
