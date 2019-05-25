from products import BaseProduct
from countries import Country


class World:
	def __init__(self):
		self.__n_raw_products = 0
		self.__raw_products = []
		self.__n_end_products = 0
		self.__end_products = []
		self.__countries = []

	def add_raw_product(self, product: BaseProduct):
		self.__n_raw_products += 1
		self.__raw_products.append(product)

	def add_end_product(self, product: BaseProduct):
		self.__n_end_products += 1
		self.__end_products.append(product)

	def add_country(self, country: Country):
		self.__countries.append(country)

	@property
	def raw_products(self):
		return self.__raw_products

	@property
	def end_products(self):
		return self.__end_products

	@property
	def n_raw_products(self):
		return self.__n_raw_products

	@property
	def n_end_products(self):
		return self.__n_end_products

	@property
	def countries(self):
		return self.__countries

	def simulate(self, years: int):
		'''
		Method to simulate one year of world activity
		'''
		for year in range(years):
			for country in self.__countries:
				country.tick()
