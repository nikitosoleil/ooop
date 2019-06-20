from driver import Driver
from utils import timeit


class KeyValue:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return hash(self.key)


class Dict:
    def __init__(self, driver: Driver):
        self.__driver = driver

    @timeit
    def get(self, key):
        result = self.__driver.find(KeyValue(key))
        if result:
            return result.value
        else:
            return None

    @timeit
    def set(self, key, value):
        found = self.__driver.find(KeyValue(key))
        if found:
            found.value = value
        else:
            self.__driver.add(KeyValue(key, value))

    @timeit
    def remove(self, key):
        self.__driver.remove(KeyValue(key))

    def keys(self):
        return [value.key for value in self.__driver]

    def values(self):
        return [value.value for value in self.__driver]

    def items(self):
        return [(value.key, value.value) for value in self.__driver]


class Set:
    def __init__(self, driver: Driver):
        self.__driver = driver

    @timeit
    def isin(self, value):
        found = self.__driver.find(value)
        return found is not None

    @timeit
    def add(self, value):
        self.__driver.add(value)

    @timeit
    def remove(self, value):
        self.__driver.remove(value)

    def items(self):
        return list(self.__driver)

    def union(self, s: 'Set'):
        pass  # TODO

    def intersection(self, s: 'Set'):
        pass  # TODO
