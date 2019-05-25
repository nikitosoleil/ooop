from PyQt5.QtWidgets import *


class MyTagTree:
	def __init__(self, uuid, text, parent):
		self.uuid = uuid
		self.text = text
		self.parent = parent
		self.links = []


class MyTreeItem(QTreeWidgetItem):
	def __init__(self, my_tag):
		super().__init__([my_tag.text])
		self.my_tag = my_tag
