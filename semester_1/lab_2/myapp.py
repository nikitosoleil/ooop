import pickle
import os
from uuid import uuid4
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import Ui_MainWindow
from mytag import MyTagTree, MyTreeItem
from mynote import MyNote
from mylistitem import MyListItem
from mydialog import MyDialog
import re

storage_path = "./storage.pickle"


class MyApp(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.addButton.clicked.connect(self.add_item)
		self.notesListWidget.itemDoubleClicked.connect(self.open_note)

		self.editAscending.triggered.connect(self.edit_ascending)
		self.editDescending.triggered.connect(self.edit_descending)
		self.creationAscending.triggered.connect(self.creation_ascending)
		self.creationDescending.triggered.connect(self.creation_descending)

		self.addTagButton.clicked.connect(self.add_tag)
		self.deleteTagButton.clicked.connect(self.delete_tag)
		self.tagTreeWidget.itemClicked.connect(self.tag_clicked)
		self.tagTreeWidget.insertTopLevelItem(0, MyTreeItem(MyTagTree(uuid4(), "All", None)))
		self.current_tag = self.tagTreeWidget.topLevelItem(0)

		self.tagEdit

		self.load()

		self.actionBreeze.triggered.connect(self.breeze_style)
		self.actionBreezeDark.triggered.connect(self.breeze_dark_style)
		self.actionQDarkStyle.triggered.connect(self.qdark_style)

		self.actionSave.triggered.connect(self.dump)
		self.actionExport.triggered.connect(self.export)

		self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
		self.save_shortcut.activated.connect(self.dump)
		self.export_shortcut = QShortcut(QKeySequence("Ctrl+E"), self)
		self.export_shortcut.activated.connect(self.export)

	def export(self):
		if len(self.notesListWidget.selectedItems()) != 0:
			output = ""
			for item in self.notesListWidget.selectedItems():
				output += "Note:\n" + item.note.text + "\n"
				output += "Edited at: " + item.note.edited_at + "\n"
				output += "Created at: " + item.note.created_at + "\n"
				tag = item.note.tag
				tag_str = ""
				while tag is not None:
					tag_str = tag.text + ", " + tag_str
					tag = tag.parent
				output += "Tag: " + tag_str[:-2] + "\n\n"
			filepath, _ = QFileDialog.getSaveFileName(self, "Select file", ".", "Text files (*.txt)")
			if filepath:
				with open(filepath, "w") as file:
					file.write(output)
		else:
			QMessageBox.warning(self, "Unable", "Please, select some notes to export")

	def breeze_style(self):
		toggle_stylesheet('./breeze/light.qss')

	def breeze_dark_style(self):
		toggle_stylesheet('./breeze/dark.qss')

	def qdark_style(self):
		toggle_stylesheet('./qdarkstyle/style.qss')

	def tag_clicked(self, tag_item):
		self.current_tag = tag_item
		for listWidget in [self.notesListWidget, self.archiveListWidget]:
			for i in range(listWidget.count()):
				tag = listWidget.item(i).note.tag
				display = False
				while tag is not None:
					if tag.uuid == tag_item.my_tag.uuid:
						display = True
					tag = tag.parent
				listWidget.item(i).setHidden(not display)

	def add_tag(self):
		tag_name = self.tagEdit.text()
		if tag_name:
			if re.match("^\w+$", tag_name):
				my_tag = MyTagTree(uuid4(), tag_name, self.current_tag.my_tag)
				self.current_tag.my_tag.links.append(my_tag)
				self.current_tag.addChild(MyTreeItem(my_tag))
			else:
				QMessageBox.warning(self, 'Invalid', 'Invalid tag name')
		self.tagEdit.clear()

	def delete_tag(self):
		if self.current_tag.parent() is not None:

			can = True

			for i in range(self.notesListWidget.count()):
				tag = self.notesListWidget.item(i).note.tag
				while tag:
					if tag.uuid == self.current_tag.my_tag.uuid:
						can = False
					tag = tag.parent

			if can:
				mb = QMessageBox.question(self, 'Confirmation', 'Are you sure want to delete this tag?\n'
																'All of the notes in archive associated with it will be lost')
				if mb == QMessageBox.Yes:
					tmp = self.current_tag
					self.current_tag = self.current_tag.parent()
					self.current_tag.removeChild(tmp)
					for i in range(len(self.current_tag.my_tag.links)):
						if tmp.my_tag.uuid == self.current_tag.my_tag.links[i].uuid:
							self.current_tag.my_tag.links.pop(i)
							break

					to_remove = []
					for i in range(self.archiveListWidget.count()):
						tag = self.archiveListWidget.item(i).note.tag
						remove = False
						while tag:
							if tag.uuid == self.current_tag.my_tag.uuid:
								remove = True
							tag = tag.parent
						if remove:
							to_remove.append(i)
					for i in to_remove:
						self.archiveListWidget.takeItem(i)
			else:
				mb = QMessageBox.critical(self, "Unable", "Unable to remove selected tag: notes with this tag are still present")

	def edit_ascending(self):
		global sort_mode
		sort_mode = 1
		for listWidget in [self.notesListWidget, self.archiveListWidget]:
			listWidget.sortItems(Qt.AscendingOrder)

	def edit_descending(self):
		global sort_mode
		sort_mode = 1
		for listWidget in [self.notesListWidget, self.archiveListWidget]:
			listWidget.sortItems(Qt.DescendingOrder)

	def creation_ascending(self):
		global sort_mode
		sort_mode = 0
		for listWidget in [self.notesListWidget, self.archiveListWidget]:
			listWidget.sortItems(Qt.AscendingOrder)

	def creation_descending(self):
		global sort_mode
		sort_mode = 0
		for listWidget in [self.notesListWidget, self.archiveListWidget]:
			listWidget.sortItems(Qt.DescendingOrder)

	def load(self):
		notes_list = []
		archive_list = []
		tag_tree = MyTagTree(uuid4(), "All", None)
		try:
			if os.path.isfile(storage_path):
				with open(storage_path, 'rb') as file:
					tag_tree, notes_list, archive_list = pickle.load(file)
				self.tagTreeWidget.topLevelItem(0).my_tag.uuid = tag_tree.uuid
		except:
			pass

		def __load(current_tag, current_tag_tree_item):
			for i in range(len(current_tag.links)):
				my_tag = MyTagTree(current_tag.links[i].uuid, current_tag.links[i].text, current_tag)
				current_tag_tree_item.my_tag.links.append(my_tag)
				current_tag_tree_item.addChild(MyTreeItem(my_tag))
				__load(current_tag.links[i], current_tag_tree_item.child(i))

		__load(tag_tree, self.tagTreeWidget.topLevelItem(0))

		for note in reversed(notes_list):
			MyListItem(note, self, "Notes")
		for note in reversed(archive_list):
			MyListItem(note, self, "Archive")

	def dump(self):
		notes_list = []
		archive_list = []
		tag_tree = self.tagTreeWidget.topLevelItem(0).my_tag

		for some_list, listWidget in zip([notes_list, archive_list], [self.notesListWidget, self.archiveListWidget]):
			for i in range(listWidget.count()):
				some_list.append(listWidget.item(i).note)
		with open(storage_path, 'wb') as file:
			pickle.dump((tag_tree, notes_list, archive_list), file)

	def add_item(self):
		note = self.noteEdit.toPlainText()
		if note:
			MyListItem(MyNote(note, self.current_tag.my_tag), self, "Notes")
		self.noteEdit.clear()

	def open_note(self, item):
		qd = QDialog()
		tmp = MyDialog(item, qd)
		qd.exec_()

	def __del__(self):
		self.dump()


def toggle_stylesheet(path):
	app = QApplication.instance()
	file = QFile(path)
	file.open(QFile.ReadOnly | QFile.Text)
	stream = QTextStream(file)
	app.setStyleSheet(stream.readAll())
