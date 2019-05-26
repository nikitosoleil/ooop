import numpy as np
import tensorflow as tf

from model_abstract import AbstractModel


class TFModel(AbstractModel):
    def __init__(self):
        self.__sess = tf.Session()

        with tf.variable_scope('input'):
            self.__x = tf.placeholder(tf.float32, (None, 32, 32, 3), name='features')
            self.__y = tf.placeholder(tf.float32, (None, 10), name='labels')
            self.__training = tf.placeholder(tf.bool, name='training')

        with tf.variable_scope('network'):
            def __conv_bn_pool_drop(now, name, filters, rate, training):
                with tf.variable_scope(name):
                    now = tf.layers.conv2d(now, filters=filters, kernel_size=(3, 3), padding='same',
                                           kernel_initializer=tf.initializers.glorot_normal, name='conv')
                    now = tf.nn.relu(now)
                    now = tf.layers.max_pooling2d(now, pool_size=(2, 2), strides=(1, 1), name='pool')
                    now = tf.layers.dropout(now, rate=rate, training=training, name='drop')
                    return now

            now = __conv_bn_pool_drop(self.__x, 'block1', 16, 0.25, self.__training)
            now = __conv_bn_pool_drop(now, 'block2', 32, 0.25, self.__training)
            now = __conv_bn_pool_drop(now, 'block3', 64, 0.25, self.__training)

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

        self.__loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=self.__y, logits=self.__output, name='loss'))
        self.__optimizer = tf.train.AdamOptimizer(0.0001)
        self.__step = self.__optimizer.minimize(self.__loss, name='step')

        self.__sess.run(tf.initialize_all_variables())

    def train_on_batch(self, x: np.ndarray, y: np.ndarray) -> (float, float):
        l, a, _ = self.__sess.run((self.__loss, self.__accuracy, self.__step),
                                  feed_dict={self.__x: x, self.__y: y, self.__training: True})
        return l, a

    def predict_on_batch(self, x: np.ndarray) -> np.ndarray:
        return self.__sess.run(self.__output, feed_dict={self.__x: x, self.__training: False})
