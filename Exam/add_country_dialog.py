from PyQt5.QtWidgets import *
from add_country_ui import Ui_AddCountryDialog
from countries import Country1, Country2, Country3, Country4
from world import World


class AddCountryDialog(Ui_AddCountryDialog):
	def __init__(self, world: World, qd: QDialog):
		super().__init__()
		self.__qd = qd
		self.setupUi(self.__qd)
		self.__world = world

		self.__type = 1
		self.oneButton.clicked.connect(self.one)
		self.twoButton.clicked.connect(self.two)
		self.threeButton.clicked.connect(self.three)
		self.fourButton.clicked.connect(self.four)
		self.addRandomButton.clicked.connect(self.add)

		self.country = None

	def one(self):
		self.__type = 1

	def two(self):
		self.__type = 2

	def three(self):
		self.__type = 3

	def four(self):
		self.__type = 4

	def add(self):
		name = self.textEdit.toPlainText()
		if name:
			if self.__type == 1:
				Country = Country1
			elif self.__type == 2:
				Country = Country2
			elif self.__type == 3:
				Country = Country3
			else:
				Country = Country4
			self.country = Country(self.__world, name)
			self.__world.add_country(self.country)
			self.__qd.accept()
