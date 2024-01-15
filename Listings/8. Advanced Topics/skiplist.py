#!/usr/bin/env python
"""Skip list implementation"""


from random import randrange

import importlib.util
import pathlib
import sys

try:
    importlib.util.find_spec(
        ".".join(pathlib.Path(__file__).parts[-3]),
        "pythonds3",
    )
except ModuleNotFoundError:
    sys.path.append(
        f"{pathlib.Path(__file__).parents[1]}/"
    )
finally:
    from pythonds3.basic import Stack


class HeaderNode:
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value


class DataNode:
    def __init__(self, key, value):
        self._key = key
        self._data = value
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        self._down = value


class SkipList:
    def __init__(self):
        self._head = None

    def search(self, key):
        current = self._head
        while current:
            if current.next is None:
                current = current.down
            else:
                if current.next.key == key:
                    return current.next.data  # found
                if key < current.next.key:
                    current = current.down
                else:
                    current = current.next
        return None

    def insert(self, key, value):
        if self._head is None:
            self._head = HeaderNode()
            temp = DataNode(key, value)
            self._head.next = temp
            top = temp
            while randrange(2) == 1:
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self._head
                self._head = newhead
                top = temp
        else:
            tower = Stack()
            current = self._head
            while current:
                if current.next is None:
                    tower.push(current)
                    current = current.down
                else:
                    if current.next.key > key:
                        tower.push(current)
                        current = current.down
                    else:
                        current = current.next

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp
            while randrange(2) == 1:
                if tower.is_empty():
                    newhead = HeaderNode()
                    temp = DataNode(key, value)
                    temp.down = top
                    newhead.next = temp
                    newhead.down = self._head
                    self._head = newhead
                    top = temp
                else:
                    next_level = tower.pop()
                    temp = DataNode(key, value)
                    temp.down = top
                    temp.next = next_level.next
                    next_level.next = temp
                    top = temp


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)


hn = HeaderNode()
print(hn)
print(hn.next)
print(hn.down)
hn.next = 1
hn.down = 2
print(hn.next)
print(hn.down)

s = SkipList()
s.insert(10, "a")
s.insert(50, "e")
s.insert(30, "c")
s.insert(20, "b")
print(s.search(10))
