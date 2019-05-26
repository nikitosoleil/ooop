from base_model import BaseModel
from keras.models import Model
from keras.layers import Input, Conv2D, Dropout, Flatten, Dense, MaxPooling2D
from keras.optimizers import Adam


class KerasModel(BaseModel):
    def __init__(self, dg):
        super().__init__(dg)

        inputs = Input((32, 32, 3))

        now = KerasModel.__conv_pool_drop(inputs, 16, 0.25)
        now = KerasModel.__conv_pool_drop(now, 32, 0.25)
        now = KerasModel.__conv_pool_drop(now, 64, 0.25)

        now = Flatten()(now)
        now = Dense(128, activation='relu')(now)
        now = Dropout(0.25)(now)
        outputs = Dense(10, activation='softmax')(now)

        self.__model = Model(inputs=inputs, outputs=outputs)

        self.__model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

        print(self.__model.summary())

    def fit(self, epochs, batch_size):
        self.__model.fit(self._dg.train_x, self._dg.train_y, batch_size, epochs, verbose=2,
                         validation_data=[self._dg.test_x, self._dg.test_y])

    def predict(self):
        return self.__model.predict(self._dg.test_x)

    @staticmethod
    def __conv_pool_drop(now, filters, rate):
        now = Conv2D(filters=filters, kernel_size=(3, 3), padding='same', activation='relu')(now)
        now = MaxPooling2D(pool_size=(2, 2))(now)
        now = Dropout(rate)(now)
        return now
