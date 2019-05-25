from abc import ABC
from random import randint
from collections import Counter


class BaseProduct(ABC):
	def __init__(self, world, name: str, id: int):
		self._world = world
		self._id = id
		self._name = name
		self._export, self._import = 0, 0
		self._type = ''
		self._usages = []
		self._requirements = []

	@property
	def id(self):
		return self._id

	@property
	def type(self):
		return self._type

	@property
	def name(self):
		return self._name

	@property
	def usages(self):
		return self._usages

	@property
	def requirements(self):
		return self._requirements

	@property
	def exported(self):
		return self._export

	@property
	def imported(self):
		return self._import

	def inc_export(self, delta: int):
		self._export += delta

	def inc_import(self, delta: int):
		self._import += delta


class RawProduct(BaseProduct):
	def __init__(self, world, name: str, id: int):
		super().__init__(world, name, id)
		self._type = 'Raw'


class EndProduct(BaseProduct):
	def __init__(self, world, name: str, id: int):
		super().__init__(world, name, id)
		self.init_random()
		self._type = 'End'

	def init_random(self):
		if self._world.n_raw_products:
			for _ in range(randint(0, self._world.n_raw_products - 1)):
				self._requirements.append(randint(0, self._world.n_raw_products - 1))
		self._requirements = list(Counter(self._requirements).items())
		for id, count in self._requirements:
			self._world.raw_products[id]._usages.append((self._id, count))

	@property
	def requirements(self):
		return self._requirements
