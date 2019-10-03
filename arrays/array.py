#!/usr/bin/env python

"""things needed for dynamic array:
- size of it and protection from going past that
- size of objects (size of type)
- need space to append
- track allocated and used
- if we run out of space, we need to make a new one w more space and copy items over.
"""

class DynamicArray:
    def __init__(self, capacity = 8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity
        pass

    def append(self, value):
        """ add something to the end"""
        if self.count >= self.capacity:
            self.resize_array()

        self.storage[self.count] = value
        self.count += 1
        pass

    def insert(self, value, index):
        if self.count >= self.capacity:
            self.resize_array()

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1
        pass

    def remove(self, index):
        """
        - find index we want
        - replace with next value and move down list
        - subtract from count
        - return item
        """
        value = self.storage[index]

        for i in range(index, self.count-1):
            self.storage[i] = self.storage[i+1]

        self.count -= 1
        return value

    def prnt(self):
        for value in self.storage:
            print(value)
        pass

    def resize_array(self):
        """ resize array """
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i, item in enumerate(self.storage):
            new_storage[i] = item

        self.storage = new_storage


    def add_to_front(self, value):
        self.insert(value, 0)
        pass
