#!/usr/bin/env python3
"""Map ADT implementation"""


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def main():
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    assert h.slots == [
        77,
        44,
        55,
        20,
        26,
        93,
        17,
        None,
        None,
        31,
        54,
    ]
    assert h.data == [
        "bird",
        "goat",
        "pig",
        "chicken",
        "dog",
        "lion",
        "tiger",
        None,
        None,
        "cow",
        "cat",
    ]

    assert h[20] == "chicken"
    assert h[17] == "tiger"
    h[20] = "duck"
    assert h[20] == "duck"
    assert h.data == [
        "bird",
        "goat",
        "pig",
        "duck",
        "dog",
        "lion",
        "tiger",
        None,
        None,
        "cow",
        "cat",
    ]
    assert h[99] is None


if __name__ == "__main__":
    main()
    print("Done")
