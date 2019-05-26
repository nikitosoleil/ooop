import pytest

from sklearn.metrics import accuracy_score

from data_cifar10 import Cifar10Factory
from model_factories import *
from pipelines import Trainer, Predictor


def acc(true, predicted):
    true = true.argmax(axis=1)
    predicted = predicted.argmax(axis=1)
    return accuracy_score(true, predicted)


class Test:
    @pytest.fixture(scope='class')
    def data_factory(self):
        return Cifar10Factory()

    @pytest.fixture(scope='class')
    def provider(self, data_factory):
        p = data_factory.get_provider()
        p.read('../cifar-10-batches-py/')
        return p

    def test_provider(self, provider):
        assert provider.train.x.shape == (30000, 32, 32, 3)
        assert provider.test.x.shape == (10000, 32, 32, 3)
        assert provider.train.y.shape == (30000, 10)
        assert provider.test.y.shape == (10000, 10)

    @pytest.fixture(scope='class')
    def trainer(self):
        return Trainer()

    @pytest.fixture(scope='class')
    def predictor(self):
        return Predictor()

    @pytest.mark.parametrize("model_factory", [PyTorchFactory(), KerasFactory(), TFFactory()])
    def test_model(self, model_factory, provider, trainer, predictor):
        model = model_factory.get_model()

        trainer.train(provider.train, model, epochs=2)
        predicted = predictor.predict(provider.test, model)

        assert predicted.shape == (10000, 10)
        assert acc(provider.test.y, predicted) > 0.2
