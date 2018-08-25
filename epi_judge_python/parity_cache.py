from test_framework import generic_test


def parity(x, cache={}):
    def precompute_parity(x, length):
        while length > 1:
            length >>= 1
            x ^= x >> length
        return x & 1

    length = 8
    # be careful about the priority of `<<` and `-`
    bit_mask = (1 << length) - 1

    result = 0
    for i in range(64 // length):
        partial_bits = x >> (i * length) & bit_mask
        if partial_bits not in cache:
            partial_parity = precompute_parity(partial_bits, length)
            cache[partial_bits] = partial_parity
        else:
            partial_parity = cache[partial_bits]
        result ^= partial_parity
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity_cache.py", 'parity.tsv', parity))
