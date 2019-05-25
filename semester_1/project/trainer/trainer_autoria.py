from base.base_train import BaseTrain
import tensorflow as tf
from tqdm import tqdm


class AutoRiaTrainer(BaseTrain):
	def __init__(self, sess, model, config, logger, generator):
		super().__init__(sess, model, config, logger, generator)
		self.model.load(self.sess)
		self.logger = logger
		self.x, self.y, self.training = tf.get_collection('inputs')
		self.loss, self.step = tf.get_collection('train')

	def train(self):
		for cur_epoch in range(self.model.cur_epoch_tensor.eval(self.sess), self.config['num_epochs'] + 1, 1):
			self.train_epoch()
			self.test()
			self.sess.run(self.model.increment_cur_epoch_tensor)

	def train_epoch(self, epoch=None):
		losses = []
		for _ in tqdm(range(self.data_loader.train_num_iter)):
			loss = self.train_step()
			losses.append(loss)
		loss = sum(losses)/len(losses)
		summaries = {'train/loss': loss}
		self.logger.summarize(self.sess.run(self.model.global_step_tensor), summaries)
		self.model.save(self.sess)
		print('Epoch: {}, Loss: {}'.format(epoch, loss))

	def train_step(self):
		x, y = self.data_loader.get_train_batch()
		_, loss = self.sess.run([self.step, self.loss], feed_dict={self.x: x, self.y: y, self.training: True})
		return loss

	def test(self):
		losses = []
		for _ in tqdm(range(self.data_loader.test_num_iter)):
			loss = self.test_step()
			losses.append(loss[0])
			print(loss)
		loss = sum(losses) / len(losses)
		summaries = {'test/loss': loss}
		self.logger.summarize(self.sess.run(self.model.global_step_tensor), summaries)
		self.model.save(self.sess)
		print('Test loss: {}'.format(loss))

	def test_step(self):
		x, y = self.data_loader.get_test_batch()
		loss = self.sess.run([self.loss], feed_dict={self.x: x, self.y: y, self.training: False})
		return loss
