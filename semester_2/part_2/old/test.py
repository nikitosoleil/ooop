import pytest

from sklearn.metrics import accuracy_score
from torch.cuda import empty_cache

from data_generator import DataGenerator
from keras_model import KerasModel
from tf_model import TFModel
from pytorch_model import PyTorchModel


def acc(true, predicted):
    true = true.argmax(axis=1)
    predicted = predicted.argmax(axis=1)
    return accuracy_score(true, predicted)


class Test:
    @pytest.fixture(scope='class')
    def dg(self):
        return DataGenerator()

    def test_generator(self, dg):
        assert dg.train_x.shape == (30000, 32, 32, 3)
        assert dg.test_x.shape == (10000, 32, 32, 3)
        assert dg.train_y.shape == (30000, 10)
        assert dg.test_y.shape == (10000, 10)

    @pytest.mark.parametrize("Model", [PyTorchModel, KerasModel, TFModel])
    def test_model(self, Model, dg):
        model = Model(dg)
        model.fit(1, 128)
        predicted = model.predict()
        assert predicted.shape == (10000, 10)
        assert acc(dg.test_y, predicted) > 0.2
