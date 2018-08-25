from test_framework import generic_test


cache_length = 8
bit_mask = (1 << cache_length) - 1

def parity(x, cache={}):
    length = 64
    while length > 1:
        length >>= 1
        x ^= x >> length
        if length == cache_length:
            cache_key = x & bit_mask
            if cache_key in cache:
                return cache[x & bit_mask]
    cache[cache_key] = x & 1
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity_log_cache.py", 'parity.tsv', parity))
