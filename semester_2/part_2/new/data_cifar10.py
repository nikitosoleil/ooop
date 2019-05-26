from typing import Iterator
import pickle

import numpy as np
from matplotlib import pyplot as plt

from data_abstract import AbstractIterator, AbstractSubset, AbstractProvider, AbstractVisualizer, AbstractDataFactory


class Cifar10Iterator(AbstractIterator):
    def __next__(self):
        if self._i < len(self._subset):
            batch_x = self._subset.x[self._i:self._i + self._batch_size]
            batch_y = self._subset.y[self._i:self._i + self._batch_size]
            self._i += self._batch_size
            return batch_x, batch_y
        else:
            raise StopIteration()


class Cifar10Subset(AbstractSubset):
    def __iter__(self) -> Iterator:
        return Cifar10Iterator(self)


class Cifar10Provider(AbstractProvider):
    def __init__(self):
        super().__init__()
        self.__label_names = None

    def read(self, path):
        with open(path + 'batches.meta', 'rb') as file:
            self.__label_names = pickle.load(file, encoding='bytes')[b'label_names']

        train_x = np.ndarray((0, 32 * 32 * 3))
        train_y = []
        for i in range(1, 4, 1):
            with open(path + 'data_batch_{}'.format(i), 'rb') as file:
                batch = pickle.load(file, encoding='bytes')
                train_x = np.vstack((train_x, batch[b'data']))
                train_y += batch[b'labels']
        train_x = train_x.reshape((-1, 3, 32, 32)).transpose(0, 2, 3, 1).astype('float32') / 255
        train_y = np.eye(10)[np.array(train_y)]
        self._train = Cifar10Subset(train_x, train_y)

        with open(path + 'test_batch', 'rb') as file:
            batch = pickle.load(file, encoding='bytes')
            test_x = batch[b'data'].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1).astype('float32') / 255
            test_y = np.eye(10)[np.array(batch[b'labels'])]
        self._test = Cifar10Subset(test_x, test_y)

    @property
    def label_names(self):
        return self.__label_names


class Cifar10Visualizer(AbstractVisualizer):
    def visualize(self, provider: Cifar10Provider):
        fig, ax = plt.subplots(2, 5, figsize=(10, 5))
        for i, subset in zip(range(2), [provider.train, provider.test]):
            for j in range(5):
                id = np.random.randint(0, subset.y.shape[0])
                ax[i, j].imshow(subset.x[id], interpolation='lanczos')
                ax[i, j].set_title(provider.label_names[subset.y[id].argmax()])
        plt.show()


class Cifar10Factory(AbstractDataFactory):
    def get_provider(self) -> AbstractProvider:
        return Cifar10Provider()

    def get_subset(self, *args) -> AbstractSubset:
        return Cifar10Subset(*args)

    def get_visualizer(self) -> AbstractVisualizer:
        return Cifar10Visualizer()
