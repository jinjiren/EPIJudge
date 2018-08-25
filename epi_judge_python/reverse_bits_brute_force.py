from test_framework import generic_test


def reverse_bits(x):
    for i in range(32):
        j = 63 - i
        x_i = x >> i & 1
        x_j = x >> j & 1
        diff = x_i ^ x_j
        if diff:
            x ^= (1 << i) | (1 << j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits_brute_force.py",
                                       "reverse_bits.tsv",
                                       reverse_bits))
