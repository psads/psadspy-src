#!/usr/bin/env python3
"""Deque Usage Example"""
from pythonds3.basic import Deque


# class Deque:
#     """Queue implementation as a list"""

#     def __init__(self):
#         """Create new deque"""
#         self._items = []

#     def is_empty(self):
#         """Check if the deque is empty"""
#         return not bool(self._items)

#     def add_front(self, item):
#         """Add an item to the front of the deque"""
#         self._items.append(item)

#     def add_rear(self, item):
#         """Add an item to the rear of the deque"""
#         self._items.insert(0, item)

#     def remove_front(self):
#         """Remove an item from the front of the deque"""
#         return self._items.pop()

#     def remove_rear(self):
#         """Remove an item from the rear of the deque"""
#         return self._items.pop(0)

#     def size(self):
#         """Get the number of items in the deque"""
#         return len(self._items)


# d = Deque()
# print(d.is_empty())
# d.add_rear(4)
# d.add_rear("dog")
# d.add_front("cat")
# d.add_front(True)
# print(d.size())
# print(d.is_empty())
# d.add_rear(8.4)
# print(d.remove_rear())
# print(d.remove_front())


def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True


assert pal_checker("lsdkjfskf") == False
assert pal_checker("radar") == True
