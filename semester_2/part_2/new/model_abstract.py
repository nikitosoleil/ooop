from abc import ABC, abstractmethod

import numpy as np


class AbstractModel(ABC):
    @abstractmethod
    def train_on_batch(self, x: np.ndarray, y: np.ndarray) -> (float, float):
        pass

    @abstractmethod
    def predict_on_batch(self, x: np.ndarray) -> np.ndarray:
        pass


class AbstractModelFactory(ABC):
    @abstractmethod
    def get_model(self) -> AbstractModel:
        pass

    # for extensibility demo purposes
    # @abstractmethod
    # def get_analyzer(self):
    #    pass
