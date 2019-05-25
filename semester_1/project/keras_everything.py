import pandas as pd
import numpy as np
import os

from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.models import Model
from keras.layers import Dropout, Dense, Input, Lambda
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau, EarlyStopping

df = pd.read_csv('processed_table.csv')
df['label'] = (df['year'] - 2010) / 5  # .apply(lambda x: np.log(x))
df['filename'] = df['ad_id'].apply(lambda x: str(x) + '.jpg')

mobilenet = MobileNetV2(input_shape=(224, 224, 3), include_top=False, pooling='avg')
for layer in mobilenet.layers:
	layer.trainable = False

new_input = Input(shape=(224, 224, 3))
x = Lambda(lambda y: (y / 128) - 1)(new_input)
x = mobilenet(x)
x = Dropout(rate=0.2)(x)
x = Dense(256, activation='tanh')(x)
x = Dropout(rate=0.2)(x)
x = Dense(1)(x)

model = Model(input=new_input, output=x)
print(model.summary())

reduce = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=1, verbose=1)
stop = EarlyStopping(monitor='loss', patience=3, verbose=1)

# generator = ImageDataGenerator(horizontal_flip=True, validation_split=0.1)

generator = ImageDataGenerator(rotation_range=10, zoom_range=0.1,
							   width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True,
							   validation_split=0.1)  # , featurewise_center = True, featurewise_std_normalization = True)

train_generator = generator.flow_from_dataframe(df, directory='processed/compressed', subset='training', y_col='label',
												class_mode='other', target_size=(224, 224), batch_size=128)
val_generator = generator.flow_from_dataframe(df, directory='processed/compressed', subset='validation', y_col='label',
											  class_mode='other', target_size=(224, 224), batch_size=128)

model.compile(optimizer=Adam(lr=0.0001), loss='mse')
model.fit_generator(train_generator, steps_per_epoch=70, epochs=100,
					validation_data=val_generator, validation_steps=7, callbacks=[reduce, stop])

batch_x, batch_y = val_generator.next()
batch_predicted = model.predict(batch_x)
print((np.hstack((batch_y.reshape(-1, 1), batch_predicted)) * 5 + 2010).astype('int'))

from scipy.stats.stats import pearsonr

print(pearsonr(batch_y.reshape(-1, 1), batch_predicted)[0])

from matplotlib import pyplot as plt

plt.scatter(batch_y.reshape(-1, 1), batch_predicted)
plt.show()
