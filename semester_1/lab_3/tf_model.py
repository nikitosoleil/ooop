from base_model import BaseModel
import tensorflow as tf
import numpy as np
from math import ceil
from tqdm import tqdm


class TFModel(BaseModel):
    def __init__(self, dg):
        super().__init__(dg)
        self.__sess = tf.Session()

        self.__x_placeholder = tf.placeholder(tf.float32, (None, 32, 32, 3), name='features')
        self.__y_placeholder = tf.placeholder(tf.float32, (None, 10), name='labels')
        self.__batch_size = tf.placeholder(tf.int64, name='batch_size')

        self.__dataset = tf.data.Dataset.from_tensor_slices((self.__x_placeholder, self.__y_placeholder))
        self.__dataset = self.__dataset.batch(self.__batch_size).repeat()
        self.__iter = self.__dataset.make_initializable_iterator()

        with tf.variable_scope('input'):
            self.__x, self.__y = self.__iter.get_next()
            self.__training = tf.placeholder(tf.bool, name='training')

        with tf.variable_scope('network'):
            now = TFModel.__conv_bn_pool_drop(self.__x, 'block1', 16, 0.25, self.__training)
            now = TFModel.__conv_bn_pool_drop(now, 'block2', 32, 0.25, self.__training)
            now = TFModel.__conv_bn_pool_drop(now, 'block3', 64, 0.25, self.__training)

            with tf.variable_scope('dense'):
                now = tf.layers.flatten(now, name='flat')
                now = tf.layers.dense(now, units=128, activation='relu',
                                      kernel_initializer=tf.initializers.glorot_normal, name='dense')
                now = tf.layers.dropout(now, rate=0.25, training=self.__training, name='drop')

            with tf.variable_scope('output'):
                self.__output = tf.layers.dense(now, units=10, kernel_initializer=tf.initializers.glorot_normal,
                                                name='dense')
                self.__softmax = tf.nn.softmax(self.__output, name='softmax')

        self.__prediction = tf.argmax(self.__output, axis=1, name='prediction')
        with tf.variable_scope('metrics'):
            self.__accuracy = tf.reduce_sum(
                tf.cast(tf.equal(tf.argmax(self.__y, axis=1), self.__prediction), tf.float32), name='accuracy')

        self.__loss = tf.reduce_sum(
            tf.nn.softmax_cross_entropy_with_logits(labels=self.__y, logits=self.__output, name='loss'))
        self.__optimizer = tf.train.AdamOptimizer(0.0001)
        self.__step = self.__optimizer.minimize(self.__loss, name='step')

        self.__sess.run(tf.initialize_all_variables())

    def fit(self, epochs, batch_size):
        self.__sess.run(self.__iter.initializer,
                        feed_dict={self.__x_placeholder: self._dg.train_x, self.__y_placeholder: self._dg.train_y,
                                   self.__batch_size: batch_size})
        n = self._dg.train_y.shape[0]
        for i in range(epochs):
            loss, acc = 0, 0
            for j in tqdm(range(ceil(n / batch_size)), desc='Epoch {0}'.format(i + 1)):
                l, a, _ = self.__sess.run((self.__loss, self.__accuracy, self.__step),
                                          feed_dict={self.__training: True})
                loss += l
                acc += a
            print('loss: {}, acc: {}'.format(loss / n, acc / n))

    def predict(self):
        batch_size = 256
        self.__sess.run(self.__iter.initializer,
                        feed_dict={self.__x_placeholder: self._dg.test_x, self.__y_placeholder: self._dg.test_y,
                                   self.__batch_size: batch_size})
        n = self._dg.test_y.shape[0]
        prediction = []
        for j in range(ceil(n / batch_size)):
            p = self.__sess.run(self.__output, feed_dict={self.__training: False})
            prediction.append(p)
        prediction = np.vstack(prediction)
        return prediction

    @staticmethod
    def __conv_bn_pool_drop(now, name, filters, rate, training):
        with tf.variable_scope(name):
            now = tf.layers.conv2d(now, filters=filters, kernel_size=(3, 3), padding='same',
                                   kernel_initializer=tf.initializers.glorot_normal, name='conv')
            now = tf.nn.relu(now)
            now = tf.layers.max_pooling2d(now, pool_size=(2, 2), strides=(1, 1), name='pool')
            now = tf.layers.dropout(now, rate=rate, training=training, name='drop')
            return now
