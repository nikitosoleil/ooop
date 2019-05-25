from PyQt5.QtWidgets import *
from view_product_ui import Ui_ViewProductDialog
from products import BaseProduct
from world import World


class ViewProductDialog(Ui_ViewProductDialog):
	def __init__(self, world: World, qd: QDialog, product: BaseProduct):
		super().__init__()
		self.__qd = qd
		self.setupUi(self.__qd)
		self.__world = world
		self.__product = product
		self.__qd.setWindowTitle('{} ({})'.format(product.name, product.type))

		balance = product.exported - product.imported
		self.stats.setText('Imported: {}, exported: {}, balance: {}'.format(product.imported, product.exported, balance))

		self.fill_products()

	def fill_products(self):
		if self.__product.type == 'Raw':
			for id, count in self.__product.usages:
				self.productsWidget.insertRow(0)
				self.productsWidget.setItem(0, 0, QTableWidgetItem(str(count)))
				self.productsWidget.setItem(0, 1, QTableWidgetItem(self.__world.end_products[id].name))
		else:
			for id, count in self.__product._requirements:
				self.productsWidget.insertRow(0)
				self.productsWidget.setItem(0, 0, QTableWidgetItem(str(count)))
				self.productsWidget.setItem(0, 1, QTableWidgetItem(self.__world.raw_products[id].name))
