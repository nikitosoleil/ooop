import numpy as np
from tqdm import tqdm

from data_abstract import AbstractSubset
from model_abstract import AbstractModel


class Trainer:
    def train(self, subset: AbstractSubset, model: AbstractModel, epochs: int):
        n = len(iter(subset))
        for i in range(epochs):
            loss, acc = 0, 0
            t = tqdm(iter(subset), desc='Epoch {0}'.format(i + 1))
            for x, y in t:
                loss_batch, acc_batch = model.train_on_batch(x, y)
                loss += loss_batch
                acc += acc_batch
            print('loss: {}, acc: {}'.format(loss / n, acc / n))


class Predictor:
    def predict(self, subset: AbstractSubset, model: AbstractModel):
        predictions = []
        for x, y in tqdm(subset):
            predictions.append(model.predict_on_batch(x))
        return np.vstack(predictions)
