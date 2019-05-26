from sklearn.metrics import accuracy_score

from data_cifar10 import Cifar10Factory
from model_factories import *
from pipelines import Trainer, Predictor


def evaluate(true, pred):
    true = true.argmax(axis=1)
    pred = pred.argmax(axis=1)
    print('Accuracy:', accuracy_score(true, pred))


if __name__ == '__main__':
    data_factory = Cifar10Factory()

    provider = data_factory.get_provider()
    provider.read('../cifar-10-batches-py/')

    # visualizer = data_factory.get_visualizer()
    # visualizer.visualize(provider)

    trainer = Trainer()
    predictor = Predictor()

    for model_factory, name in [(PyTorchFactory(), 'PyTorch'), (KerasFactory(), 'Keras'), (TFFactory(), 'TF')]:
        print(name)
        model = model_factory.get_model()

        trainer.train(provider.train, model, epochs=2)
        predicted = predictor.predict(provider.test, model)

        evaluate(provider.test.y, predicted)

        del model
