from PyQt5.QtWidgets import *
from add_product_ui import Ui_AddProductDialog
from products import EndProduct, RawProduct
from world import World


class AddProductDialog(Ui_AddProductDialog):
	def __init__(self, world: World, qd: QDialog):
		super().__init__()
		self.__qd = qd
		self.setupUi(self.__qd)
		self.__world = world

		self.__type = 'Raw'
		self.endButton.clicked.connect(self.end)
		self.rawButton.clicked.connect(self.raw)
		self.addRandomButton.clicked.connect(self.add)

		self.product = None

	def end(self):
		self.__type = 'End'

	def raw(self):
		self.__type = 'Raw'

	def add(self):
		name = self.textEdit.toPlainText()
		if name:
			if self.__type == 'Raw':
				self.product = RawProduct(self.__world, name, self.__world.n_raw_products)
				self.__world.add_raw_product(self.product)
			else:
				self.product = EndProduct(self.__world, name, self.__world.n_end_products)
				self.__world.add_end_product(self.product)
			self.__qd.accept()
