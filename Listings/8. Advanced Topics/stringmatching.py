#!/usr/bin/env python
"""KMP implementation"""


def simple_matcher(pattern, text):
    i = j = 0

    while True:
        if text[i] == pattern[j]:
            j = j + 1
        else:
            j = 0
        i = i + 1

        if i == len(text):
            return -1
        if j == len(pattern):
            return i - j


def mismatched_links(pattern):
    aug_pattern = "0" + pattern
    links = {1: 0}
    for k in range(2, len(aug_pattern)):
        s = links[k - 1]
        while s >= 1:
            if aug_pattern[s] == aug_pattern[k - 1]:
                break
            s = links[s]
        links[k] = s + 1
    return links


assert simple_matcher("ab", "ccabababcab") == 2
assert simple_matcher("xyz", "ccabababcab") == -1

assert mismatched_links("ACATA") == {
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 1,
}
print("Done")
