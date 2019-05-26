from model_abstract import AbstractModel, AbstractModelFactory
from model_keras import KerasModel
from model_tf import TFModel
from model_pytorch import PyTorchModel


class KerasFactory(AbstractModelFactory):
    def get_model(self) -> AbstractModel:
        return KerasModel()


class TFFactory(AbstractModelFactory):
    def get_model(self) -> AbstractModel:
        return TFModel()


class PyTorchFactory(AbstractModelFactory):
    def get_model(self) -> AbstractModel:
        return PyTorchModel()
