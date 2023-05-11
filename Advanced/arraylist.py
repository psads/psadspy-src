#!/usr/bin/env python
"""ArrayList implementation"""


class ArrayList:
    def __init__(self):
        self.size_exponent = 0
        self.max_size = 0
        self.last_index = 0
        self.my_array = []

    def append(self, val):
        if self.last_index > self.max_size - 1:
            self.__resize()
        self.my_array[self.last_index] = val
        self.last_index += 1

    def __resize(self):
        new_size = 2 ** self.size_exponent
        print("new_size = ", new_size)
        new_array = [0] * new_size
        for i in range(self.max_size):
            new_array[i] = self.my_array[i]

        self.max_size = new_size
        self.my_array = new_array
        self.size_exponent += 1

    def __getitem__(self, idx):
        if idx < self.last_index:
            return self.my_array[idx]
        raise LookupError("index out of bounds")

    def __setitem__(self, idx, val):
        if idx < self.last_index:
            self.my_array[idx] = val
        raise LookupError("index out of bounds")

    def insert(self, idx, val):
        if self.last_index > self.max_size - 1:
            self.__resize()
        for i in range(self.last_index, idx - 1, -1):
            self.my_array[i + 1] = self.my_array[i]
        self.last_index += 1
        self.my_array[idx] = val


lst = ArrayList()
for i in range(100):
    lst.append(i)
