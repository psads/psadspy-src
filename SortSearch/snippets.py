#!/usr/bin/env python3
"""Snippets of code"""


def sequential_search(a_list, item):
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos = pos + 1

    return False


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
assert not sequential_search(test_list, 3)
assert sequential_search(test_list, 13)


def ordered_sequential_search(a_list, item):
    pos = 0
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:
                return False
            else:
                pos = pos + 1

    return False


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
assert not ordered_sequential_search(test_list, 3)
assert ordered_sequential_search(test_list, 13)


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

assert not binary_search(test_list, 3)
assert binary_search(test_list, 13)


def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(
                a_list[:midpoint], item
            )
        else:
            return binary_search_rec(
                a_list[midpoint + 1 :], item
            )


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

assert not binary_search_rec(test_list, 3)
assert binary_search_rec(test_list, 13)


def hash_str(a_string, table_size):
    current_sum = 0
    for pos in range(len(a_string)):
        current_sum = current_sum + ord(a_string[pos])

    return current_sum % table_size


def hash_str2(a_string, table_size):
    return sum([ord(c) for c in a_string]) % table_size


assert hash_str("cat", 11) == hash_str2("cat", 11)
assert hash_str("dog", 13) == hash_str2("dog", 13)
assert hash_str("rabbit", 101) == hash_str2(
    "rabbit", 101
)

