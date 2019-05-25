import sys

sys.path.extend(['..'])

import tensorflow as tf
import os

from generator.generator_autoria import AutoRiaGenerator
from model.model_autoria import AutoRiaModel
from trainer.trainer_autoria import AutoRiaTrainer

from utils.config import get_config
from utils.logger import DefinedSummarizer


def main():
	# with tf.device('/gpu:0'):
	config = get_config('../configs/config_autoria.json')
	for path in [config['summary'], config['checkpoint']]:
		if not os.path.exists(path):
			os.makedirs(path)

	sess = tf.Session()
	generator = AutoRiaGenerator(config)
	model = AutoRiaModel(config)
	logger = DefinedSummarizer(sess, summary_dir=config['summary'], scalar_tags=['train/loss', 'test/loss'])
	trainer = AutoRiaTrainer(sess, model, config, logger, generator)
	sess.run(tf.initialize_all_variables())
	trainer.train()


if __name__ == '__main__':
	main()
