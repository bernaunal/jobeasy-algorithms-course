from math import floor
from math import ceil


def split_in_half(string):
    string_len = len(string)
    print(string_len)
    half = ceil(string_len / 2)
    print(half)
    left = string[:half]
    right = string[half:]
    return right + left


print(split_in_half('bbbbbabbccccaaa'))