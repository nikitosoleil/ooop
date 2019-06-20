from typing import Iterator

from driver import Driver


class HashTable(Driver):
    def __init__(self, n: int = 10):
        self.__n = n
        self.__buckets = [[] for _ in range(n)]
        self.__len = 0

    def __bucket(self, value):
        return hash(value) % self.__n

    def add(self, value):
        self.__buckets[self.__bucket(value)].append(value)
        self.__len += 1

    def remove(self, value):
        if value in self.__buckets[self.__bucket(value)]:
            self.__len -= 1
            self.__buckets[self.__bucket(value)].remove(value)

    def find(self, value):
        for candidate in self.__buckets[self.__bucket(value)]:
            if candidate == value:
                return candidate
        return None

    @property
    def buckets(self):
        return self.__buckets

    def __len__(self):
        return self.__len

    def __iter__(self):  # pattern: factory method
        return TableIterator(self)


class TableIterator(Iterator):  # iterator
    def __init__(self, t: HashTable):
        self.__table = t
        self.__i = self.__j = 0

    def __next__(self):
        while True:
            if self.__i >= len(self.__table.buckets):
                raise StopIteration
            elif self.__j < len(self.__table.buckets[self.__i]):
                self.__j += 1
                return self.__table.buckets[self.__i][self.__j - 1]
            else:
                self.__i += 1
                self.__j = 0
