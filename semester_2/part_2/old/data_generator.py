import pickle
import numpy as np
import matplotlib.pyplot as plt


class DataGenerator:
    def __init__(self):
        self.__path = '../cifar-10-batches-py/'
        with open(self.__path + 'batches.meta', 'rb') as file:
            self.__label_names = pickle.load(file, encoding='bytes')[b'label_names']
        self.__train_x = np.ndarray((0, 32 * 32 * 3))
        self.__train_y = []
        for i in range(1, 4, 1):
            with open(self.__path + 'data_batch_{}'.format(i), 'rb') as file:
                batch = pickle.load(file, encoding='bytes')
                self.__train_x = np.vstack((self.__train_x, batch[b'data']))
                self.__train_y += batch[b'labels']
        self.__train_x = self.__train_x.reshape((-1, 3, 32, 32)).transpose(0, 2, 3, 1).astype('float32') / 255
        self.__train_y = np.eye(10)[np.array(self.__train_y)]
        with open(self.__path + 'test_batch', 'rb') as file:
            batch = pickle.load(file, encoding='bytes')
            self.__test_x = batch[b'data'].reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1).astype('float32') / 255
            self.__test_y = np.eye(10)[np.array(batch[b'labels'])]

    @property
    def train_x(self):
        return self.__train_x

    @property
    def train_y(self):
        return self.__train_y

    @property
    def test_x(self):
        return self.__test_x

    @property
    def test_y(self):
        return self.__test_y

    def visualize(self):
        fig, ax = plt.subplots(2, 5, figsize=(10, 5))
        for i, x, y in zip(range(2), [self.train_x, self.test_x], [self.train_y, self.test_y]):
            for j in range(5):
                id = np.random.randint(0, y.shape[0])
                ax[i, j].imshow(x[id], interpolation='lanczos')
                ax[i, j].set_title(self.__label_names[y[id].argmax()])
        plt.show()
