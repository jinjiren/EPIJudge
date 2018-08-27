from test_framework import generic_test


cache = dict()


def partial_reverse_bits(x):
    for i in range(8):
        j = 15 - i
        x_i = x >> i & 1
        x_j = x >> j & 1
        diff = x_i ^ x_j
        if diff:
            x ^= (1 << i) | (1 << j)
    return x


def check_cache(x):
    if x in cache:
        return cache[x]
    else:
        result = partial_reverse_bits(x)
        cache[x] = result
        return result


def reverse_bits(x):
    x0 = x & 0xFFFF
    x1 = x >> 16 & 0xFFFF
    x2 = x >> 32 & 0xFFFF
    x3 = x >> 48 & 0xFFFF

    r_x0 = check_cache(x0)
    r_x1 = check_cache(x1)
    r_x2 = check_cache(x2)
    r_x3 = check_cache(x3)
    result = r_x0 << 48 | r_x1 << 32 | r_x2 << 16 | r_x3
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits_brute_force_cache.py",
                                       "reverse_bits.tsv",
                                       reverse_bits))
