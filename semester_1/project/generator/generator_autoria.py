import pandas as pd
import numpy as np
from skimage.io import imread
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


class AutoRiaGenerator:
	def __init__(self, config):
		self.config = config
		self.table = pd.read_csv(r'../data/autoria/processed_table.csv')
		self.path = '../data/autoria/processed'
		self.x = self.table.iloc[:, 1].values.reshape(-1, 1)
		self.y = self.table.iloc[:, 2:4].values
		self.iterator_train, self.iterator_test = 0, 0
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.1)
		self.batch_size = self.config['batch_size']
		self.train_len = self.x_train.shape[0]
		self.test_len = self.x_test.shape[0]
		self.train_num_iter = self.train_len // self.batch_size
		self.test_num_iter = self.test_len // self.batch_size

	def get_test_batch(self):
		if self.iterator_test + self.batch_size > self.test_len:
			self.iterator_test = 0
			self.x_test, self.y_test = shuffle(self.x_test, self.y_test)
		to = min(self.test_len, self.iterator_test + self.batch_size)
		batch_x = []
		for ad_id in self.x_test[self.iterator_test:to, 0]:
			image = imread(self.path + '/' + str(ad_id) + '.jpg')
			if image.shape != (240, 320, 3):
				print(ad_id)
			# data augmentation was here
			batch_x.append(image)
		batch_y = self.y_test[self.iterator_test:to]
		self.iterator_test = to
		return np.asarray(batch_x), np.asarray(batch_y)

	def get_train_batch(self):
		if self.iterator_train + self.batch_size > self.train_len:
			self.iterator_train = 0
			self.x_train, self.y_train = shuffle(self.x_train, self.y_train)
		to = min(self.train_len, self.iterator_train + self.batch_size)
		batch_x = []
		for ad_id in self.x_train[self.iterator_train:to, 0]:
			image = imread(self.path + '/' + str(ad_id) + '.jpg')
			if image.shape != (240, 320, 3):
				print(ad_id)
			# data augmentation was here
			batch_x.append(image)
		batch_y = self.y_train[self.iterator_train:to]
		self.iterator_train = to
		return np.asarray(batch_x), np.asarray(batch_y)


def test():
	from utils.config import get_config
	config = get_config('../configs/config_autoria.json')
	generator = AutoRiaGenerator(config)
	_ = generator.get_train_batch()
	generator.get_train_batch()
	print(_[0].shape, _[1].shape)
	import matplotlib.pyplot as plt
	print(_[1][0])
	plt.imshow(_[0][0])
	plt.show()


if __name__ == '__main__':
	test()
