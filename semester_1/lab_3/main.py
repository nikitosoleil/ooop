from data_generator import DataGenerator
from keras_model import KerasModel
from tf_model import TFModel
from pytorch_model import PyTorchModel
from sklearn.metrics import accuracy_score


def evaluate(true, predicted):
    true = true.argmax(axis=1)
    predicted = predicted.argmax(axis=1)
    print('Accuracy:', accuracy_score(true, predicted))


if __name__ == '__main__':
    dg = DataGenerator()
    dg.visualize()
    for model, name in [(PyTorchModel, 'PyTorch'), (KerasModel, 'Keras'), (TFModel, 'TF')]:
        model = model(dg)
        print(name)
        model.fit(2, 128)
        predicted = model.predict()
        evaluate(dg.test_y, predicted)
        input()
