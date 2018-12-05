from base.base_model import BaseModel
import tensorflow as tf


class AutoRiaModel(BaseModel):
	def __init__(self, config):
		super().__init__(config)
		self.x, self.y = None, None
		self.training = None
		self.out = None
		self.loss = None
		self.optimizer = None
		self.step = None
		self.build_model()
		self.init_saver()

	def build_model(self):
		with tf.variable_scope('input'):
			self.x = tf.placeholder(tf.float32, [None, self.config['image_height'], self.config['image_width'], self.config['image_depth']],
									'features')
			self.y = tf.placeholder(tf.float32, [None, 2], 'labels')
			self.training = tf.placeholder(tf.bool, name='training_flag')
			tf.add_to_collection('inputs', self.x)
			tf.add_to_collection('inputs', self.y)
			tf.add_to_collection('inputs', self.training)

		with tf.variable_scope('network'):
			tmp = AutoRiaModel.conv_bn_relu('block1', self.x, filter=8, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.conv_bn_relu('block2', tmp, filter=8, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.pool('pool1', tmp, pool_size=(5, 5), strides=(5, 5))

			tmp = AutoRiaModel.conv_bn_relu('block3', tmp, filter=16, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.conv_bn_relu('block4', tmp, filter=16, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.pool('pool2', tmp, pool_size=(4, 4), strides=(4, 4))

			tmp = AutoRiaModel.conv_bn_relu('block5', tmp, filter=32, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.conv_bn_relu('block6', tmp, filter=32, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.pool('pool3', tmp, pool_size=(2, 2), strides=(2, 2))

			tmp = AutoRiaModel.conv_bn_relu('block7', tmp, filter=64, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.conv_bn_relu('block8', tmp, filter=64, kernel_size=(3, 3), strides=(1, 1), padding='SAME', training=self.training)
			tmp = AutoRiaModel.pool('pool4', tmp, pool_size=(2, 2), strides=(2, 2))

			with tf.variable_scope('flat'):
				tmp = tf.layers.flatten(tmp, name='flat')

			tmp = AutoRiaModel.dense_bn_relu_drop('block9', tmp, units=256, training=self.training, rate=0.5)
			tmp = AutoRiaModel.dense_bn_relu_drop('block10', tmp, units=128, training=self.training, rate=0.3)

			with tf.variable_scope('output'):
				self.out = tf.layers.dense(tmp, 2, kernel_initializer=tf.initializers.random_normal, name='out')
				tf.add_to_collection('outputs', self.out)

		with tf.variable_scope('loss'):
			self.loss = tf.losses.mean_squared_error(self.y[:, 1], self.out[:, 1])  # TODO don't forget to consider year

		with tf.variable_scope('metrics'):
			pass  # TODO add some metrics

		with tf.variable_scope('step'):
			self.optimizer = tf.train.AdamOptimizer(self.config['learning_rate'])
			self.step = self.optimizer.minimize(self.loss, self.global_step_tensor)

		tf.add_to_collection('train', self.loss)
		tf.add_to_collection('train', self.step)

	def init_saver(self):
		self.saver = tf.train.Saver(max_to_keep=2)

	@staticmethod
	def conv_bn_relu(name, tmp, filter, kernel_size, strides, padding, training):
		with tf.variable_scope(name):
			tmp = tf.layers.conv2d(tmp, filters=filter, kernel_size=kernel_size, strides=strides, padding=padding,
								   kernel_initializer=tf.contrib.layers.xavier_initializer(), name='conv')
			tmp = tf.layers.batch_normalization(tmp, training=training, name='bn')
			tmp = tf.nn.relu(tmp, name='relu')
			return tmp

	@staticmethod
	def pool(name, tmp, pool_size, strides):
		with tf.variable_scope(name):
			tmp = tf.layers.max_pooling2d(tmp, pool_size=pool_size, strides=strides, name='pool')
			return tmp

	@staticmethod
	def dense_bn_relu_drop(name, tmp, units, training, rate):
		with tf.variable_scope(name):
			tmp = tf.layers.dense(tmp, units=units, kernel_initializer=tf.initializers.random_normal, name='dense')
			tmp = tf.layers.batch_normalization(tmp, training=training, name='bn')
			tmp = tf.nn.relu(tmp)
			tmp = tf.layers.dropout(tmp, rate=rate, training=training)
			return tmp
