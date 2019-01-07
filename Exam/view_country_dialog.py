from PyQt5.QtWidgets import *
from view_country_ui import Ui_ViewCountryDialog
from countries import Country, Country3, Country4
from world import World


class ViewCountryDialog(Ui_ViewCountryDialog):
	def __init__(self, world: World, qd: QDialog, country: Country):
		super().__init__()
		self.__qd = qd
		self.setupUi(self.__qd)
		self.__world = world
		self.__country = country
		self.__qd.setWindowTitle('{} (type {})'.format(country.name, country.type))

		self.fill_products()

	def fill_products(self):
		if isinstance(self.__country, Country3) or isinstance(self.__country, Country4):
			tmp = zip(['Extracting', 'Producing', 'Importing'],
					  [self.__country.resources, self.__country.producing, self.__country.importing],
					  [self.__world.raw_products, self.__world.end_products, self.__world.end_products])
		else:
			tmp = zip(['Extracting', 'Consuming'],
					  [self.__country.resources, self.__country.consuming],
					  [self.__world.raw_products, self.__world.end_products])
		for activity, id_counts, products in tmp:
			for id, count in id_counts:
				self.productsWidget.insertRow(0)
				self.productsWidget.setItem(0, 0, QTableWidgetItem(activity))
				self.productsWidget.setItem(0, 1, QTableWidgetItem(str(count)))
				self.productsWidget.setItem(0, 2, QTableWidgetItem(products[id].name))
