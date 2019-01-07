from abc import ABC
from random import randint, sample
from collections import Counter


class Country(ABC):
	def __init__(self, world, name):
		self._world = world
		self._resources = []
		self._consuming = []
		self._name = name
		self._type = 0
		self.init_random()

	def init_random(self):
		if self._world.n_raw_products:
			for _ in range(randint(0, self._world.n_raw_products - 1)):
				self._resources.append(randint(0, self._world.n_raw_products - 1))
		self._resources = list(Counter(self._resources).items())

		if self._world.n_end_products:
			for _ in range(randint(0, self._world.n_end_products - 1)):
				self._consuming.append(randint(0, self._world.n_end_products - 1))
		self._consuming = list(Counter(self._consuming).items())

	@property
	def name(self):
		return self._name

	@property
	def type(self):
		return self._type

	@property
	def resources(self):
		return self._resources

	@property
	def consuming(self):
		return self._consuming

	def tick(self):
		'''
		Method to simulate one year of country activity
		'''
		pass

	@staticmethod
	def random_count(mean: int) -> int:
		'''
		Function to sample produced/consumed amount of product in current year

		:param mean: mean of the distribution
		:return: sampled amount
		'''
		return randint(mean // 2, (3 * mean + 1) // 2)


class Country1(Country):
	# Exports every raw product and imports everything needed
	def __init__(self, world, name):
		super().__init__(world, name)
		self._type = 1

	def tick(self):
		for id, mean in self._resources:
			count = Country.random_count(mean)
			self._world.raw_products[id].inc_export(count)

		for id, mean in self._consuming:
			count = Country.random_count(mean)
			self._world.end_products[id].inc_import(count)


class Country2(Country):
	# Produces everything needed on its own, exports all extra raw products, imports all missing raw products
	def __init__(self, world, name):
		super().__init__(world, name)
		self._type = 2

	def tick(self):
		balance = [0] * self._world.n_raw_products

		for id, mean in self._resources:
			count = Country.random_count(mean)
			balance[id] += count

		for id, mean in self._consuming:
			count = Country.random_count(mean)
			for req_id, req_count in self._world.end_products[id].requirements:
				balance[req_id] -= req_count * count

		for id, bal in enumerate(balance):
			if bal < 0:
				self._world.raw_products[id].inc_import(-bal)
			else:
				self._world.raw_products[id].inc_export(bal)


class Country3(Country):
	# Same as previous except it produces on its own only a subset of "traditional" products, which is also partially exported
	__producing_portion = 0.5  # (number of traditional products) / (number of consumed products)
	__exporting_rate = 1  # (number of traditional products exported) / (number of traditional products consumed)

	def __init__(self, world, name):
		super().__init__(world, name)
		self.__producing = []
		self.__importing = []
		self.init_random_new()
		self._type = 3

	@property
	def producing(self):
		return self.__producing

	@property
	def importing(self):
		return self.__importing

	def init_random_new(self):
		self.__producing = sample(self._consuming, int(Country3.__producing_portion * len(self._consuming)))
		self.__importing = [product for product in self._consuming if product not in self.__producing]

	def tick(self):
		balance = [0] * self._world.n_raw_products

		for id, mean in self._resources:
			count = Country.random_count(mean)
			balance[id] += count

		for id, mean in self.__producing:
			count_consumed = Country.random_count(mean)
			count_exported = Country.random_count(mean * Country3.__exporting_rate)
			for req_id, req_count in self._world.end_products[id].requirements:
				balance[req_id] -= req_count * (count_consumed + count_exported)
			self._world.end_products[id].inc_export(count_exported)

		for id, mean in self.__importing:
			count = Country.random_count(mean)
			self._world.end_products[id].inc_import(count)

		for id, bal in enumerate(balance):
			if bal < 0:
				self._world.raw_products[id].inc_import(-bal)
			else:
				self._world.raw_products[id].inc_export(bal)


class Country4(Country):
	# Same as the previous but instead of random traditional products there are most popular ones
	__producing_portion = 0.5  # (number of products to produce) / (number of all products with negative balance)
	__exporting_rate = 1  # (number of traditional products exported) / (number of traditional products consumed)

	def __init__(self, world, name):
		super().__init__(world, name)
		self.__producing = []
		self.__importing = self._consuming
		self._type = 4

	@property
	def producing(self):
		return self.__producing

	@property
	def importing(self):
		return self.__importing

	def tick(self):
		neg_bal = [i for i, product in enumerate(self._world.end_products) for _ in range(product.imported - product.exported) if
				   product.exported < product.imported]
		self.__producing = list(Counter(sample(neg_bal, int(Country4.__producing_portion * len(neg_bal)))).items())
		tmp = dict(self.__producing)
		self.__importing = [(id, mean - (tmp[id] if id in tmp else 0)) for id, mean in self._consuming if id not in tmp or mean > tmp[id]]

		balance = [0] * self._world.n_raw_products

		for id, mean in self._resources:
			count = Country.random_count(mean)
			balance[id] += count

		for id, mean in self.__producing:
			count_consumed = Country.random_count(mean)
			count_exported = Country.random_count(mean * Country4.__exporting_rate)
			for req_id, req_count in self._world.end_products[id].requirements:
				balance[req_id] -= req_count * (count_consumed + count_exported)
			self._world.end_products[id].inc_export(count_exported)

		for id, mean in self.__importing:
			count = Country.random_count(mean)
			self._world.end_products[id].inc_import(count)

		for id, bal in enumerate(balance):
			if bal < 0:
				self._world.raw_products[id].inc_import(-bal)
			else:
				self._world.raw_products[id].inc_export(bal)
