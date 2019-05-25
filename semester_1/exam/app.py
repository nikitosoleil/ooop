from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main_ui import Ui_Main
from world import World
from add_product_dialog import AddProductDialog
from view_product_dialog import ViewProductDialog
from add_country_dialog import AddCountryDialog
from view_country_dialog import ViewCountryDialog


class Item(QTableWidgetItem):
	def __init__(self, label, content):
		super().__init__(str(label))
		self.__content= content

	@property
	def content(self):
		return self.__content


class App(QMainWindow, Ui_Main):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.__world = World()

		self.addProductButton.clicked.connect(self.add_product)
		self.addCountryButton.clicked.connect(self.add_country)

		self.productsWidget.itemDoubleClicked.connect(self.view_product)
		self.countriesWidget.itemDoubleClicked.connect(self.view_country)
		self.simulateButton.clicked.connect(self.simulate)

	def view_product(self, item):
		qd = QDialog()
		vpd = ViewProductDialog(self.__world, qd, item.content)
		qd.exec_()

	def view_country(self, item):
		qd = QDialog()
		vpd = ViewCountryDialog(self.__world, qd, item.content)
		qd.exec_()

	def add_product(self):
		qd = QDialog()
		apd = AddProductDialog(self.__world, qd)
		qd.exec_()
		product = apd.product
		if product:
			self.productsWidget.insertRow(0)
			self.productsWidget.setItem(0, 0, Item(product.type, product))
			self.productsWidget.setItem(0, 1, Item(product.name, product))

	def add_country(self):
		qd = QDialog()
		apd = AddCountryDialog(self.__world, qd)
		qd.exec_()
		country = apd.country
		if country:
			self.countriesWidget.insertRow(0)
			self.countriesWidget.setItem(0, 0, Item(country.type, country))
			self.countriesWidget.setItem(0, 1, Item(country.name, country))

	def simulate(self):
		years = int(self.yearsBox.text())
		print(years)
		self.__world.simulate(years)
