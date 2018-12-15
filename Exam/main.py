import random


class Main:
	def __init__(self):
		self.products = []
		self.countries = []
		self.n_raw_products = 0
		self.n_products = 0
		self.n_countries = 0


class Country:
	def __init__(self, main, name):
		self.main = main
		self.name = name
		self.resources = []
		self.consuming = []
		for _ in range(random.randint(0, self.main.n_raw_products)):
			self.resources.append(random.randint(1, self.main.n_products))
		for _ in range(random.randint(0, self.main.n_products)):
			self.consuming.append(random.randint(1, self.main.n_products))


class BaseProduct:
	def __init__(self, main, name, id):
		self.main = main
		self.name = name
		self.id = id


class RawProduct(BaseProduct):
	def __init__(self, main, name, id):
		super().__init__(main, name, id)


class Product(BaseProduct):
	def __init__(self, main, name, id):
		super().__init__(main, name, id)
		self.requirements = []
		for _ in range(self.main.n_products):
			self.requirements.append(random.randint(1, self.main.n_products))
		self.requirements = {i: self.requirements.count(i) for i in self.requirements}
