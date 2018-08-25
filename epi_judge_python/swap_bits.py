from test_framework import generic_test


def swap_bits(x, i, j):
    # get the value at indices i, j of x
    x_i = x >> i & 1
    x_j = x >> j & 1
    # test whether they are different
    diff = x_i ^ x_j
    # similar to
    # ```
    #     if diff:
    #         x ^= 1 << i | 1 << j
    # ```
    x ^= diff << i | diff << j
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
