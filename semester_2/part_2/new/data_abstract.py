from typing import Iterator
from abc import ABC, abstractmethod

import numpy as np

from config import Config


class AbstractIterator(ABC, Iterator):
    def __init__(self, subset):
        self._subset = subset
        self._batch_size = Config().batch_size
        self._i = 0

    def __len__(self):
        return len(self._subset) // self._batch_size

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class AbstractSubset(ABC):
    def __init__(self, x, y):
        assert len(x) == len(y)
        self._x = x
        self._y = y

    def __len__(self):
        return len(self._x)

    # factory method
    @abstractmethod
    def __iter__(self) -> Iterator:
        pass

    @property
    def x(self) -> np.ndarray:
        return self._x

    @property
    def y(self) -> np.ndarray:
        return self._y


class AbstractProvider(ABC):
    def __init__(self):
        self._train = None
        self._test = None

    @abstractmethod
    def read(self, path: str):
        pass

    @property
    def train(self) -> AbstractSubset:
        return self._train

    @property
    def test(self) -> AbstractSubset:
        return self._test


class AbstractVisualizer(ABC):
    @abstractmethod
    def visualize(self, provider: AbstractProvider):
        pass


# factory
class AbstractDataFactory(ABC):
    @abstractmethod
    def get_provider(self) -> AbstractProvider:
        pass

    @abstractmethod
    def get_subset(self) -> AbstractSubset:
        pass

    @abstractmethod
    def get_visualizer(self) -> AbstractVisualizer:
        pass
