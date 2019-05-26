import numpy as np
from keras.models import Model
from keras.layers import Input, Conv2D, Dropout, Flatten, Dense, MaxPooling2D
from keras.optimizers import Adam

from model_abstract import AbstractModel


class KerasModel(AbstractModel):
    def __init__(self):
        inputs = Input((32, 32, 3))

        def __conv_pool_drop(current, filters, rate):
            current = Conv2D(filters=filters, kernel_size=(3, 3), padding='same', activation='relu')(current)
            current = MaxPooling2D(pool_size=(2, 2))(current)
            current = Dropout(rate)(current)
            return current

        now = __conv_pool_drop(inputs, 16, 0.25)
        now = __conv_pool_drop(now, 32, 0.25)
        now = __conv_pool_drop(now, 64, 0.25)

        now = Flatten()(now)
        now = Dense(128, activation='relu')(now)
        now = Dropout(0.25)(now)
        outputs = Dense(10, activation='softmax')(now)

        self.__model = Model(inputs=inputs, outputs=outputs)
        self.__model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

    def train_on_batch(self, x: np.ndarray, y: np.ndarray) -> (float, float):
        return self.__model.train_on_batch(x, y)

    def predict_on_batch(self, x: np.ndarray) -> np.ndarray:
        return self.__model.predict_on_batch(x)
