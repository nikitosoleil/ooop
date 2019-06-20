from abc import ABC, abstractmethod
from typing import Iterable


class Driver(ABC, Iterable):  # pattern: bridge
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def find(self, value):
        pass
