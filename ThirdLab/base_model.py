from abc import ABC, abstractmethod


class BaseModel(ABC):
	def __init__(self, dg):
		self._dg = dg

	@abstractmethod
	def fit(self, epochs, batch_size):
		pass

	@abstractmethod
	def predict(self):
		pass
