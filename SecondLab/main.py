import os

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import Ui_MainWindow
from dialog import Ui_Dialog
import datetime
import pickle
from uuid import uuid4

storage_path = "./storage.pickle"


def current_time():
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


sort_mode = 0


class MyNote:
	def __init__(self, text, tag, created_at=None, edited_at=None):
		if not created_at:
			created_at = current_time()
		if not edited_at:
			edited_at = current_time()
		self.text = text
		self.created_at, self.edited_at = created_at, edited_at
		self.tag = tag


class MyListItem(QListWidgetItem):
	def __init__(self, note, parent_app, mode):
		super().__init__()
		self.note = note
		self.parent_app = parent_app
		self.mode = mode
		self.build_widget()
		self.add_note()

	def build_widget(self):
		self.widget = QWidget()
		self.textLabel = QLabel(self.note.text)
		self.deleteButton = QPushButton()
		self.archivateButton = QPushButton()
		self.restoreButton = QPushButton()

		icon = QIcon()
		icon.addPixmap(QPixmap("res/restore.png"), QIcon.Normal, QIcon.Off)
		self.restoreButton.setIcon(icon)
		icon = QIcon()
		icon.addPixmap(QPixmap("res/archive.png"), QIcon.Normal, QIcon.Off)
		self.archivateButton.setIcon(icon)
		icon = QIcon()
		icon.addPixmap(QPixmap("res/bin.png"), QIcon.Normal, QIcon.Off)
		self.deleteButton.setIcon(icon)

		self.deleteButton.setToolTip("Permanently delete note")
		self.archivateButton.setToolTip("Move note to archive")
		self.restoreButton.setToolTip("Restore note from archive to main tab")

		self.deleteButton.clicked.connect(self.delete_note_with_mb)
		self.archivateButton.clicked.connect(self.archive_note)
		self.restoreButton.clicked.connect(self.restore_note)

		self.textLabel.setWordWrap(True)
		self.textLabel.setMaximumHeight(60)
		self.deleteButton.setFixedWidth(30)
		self.archivateButton.setFixedWidth(30)
		self.restoreButton.setFixedWidth(30)

		h_layout = QHBoxLayout()
		v_layout = QVBoxLayout()
		v_layout.addWidget(self.textLabel)

		tmp = ("Edited: " if self.mode == "Notes" else "Archived: ")
		self.time_info = QLabel(tmp + str(self.note.edited_at) + "   Created: " + str(self.note.created_at))
		palette = self.time_info.palette()
		palette.setColor(QPalette.Text, Qt.gray)
		self.time_info.setPalette(palette)
		v_layout.addWidget(self.time_info)

		h_layout.addLayout(v_layout)
		v_layout = QVBoxLayout()
		v_layout.addWidget(self.deleteButton)
		v_layout.addWidget(self.archivateButton if self.mode == "Notes" else self.restoreButton)
		h_layout.addLayout(v_layout)

		self.widget.setLayout(h_layout)
		self.setSizeHint(self.widget.sizeHint())

	def __lt__(self, other):
		if sort_mode == 0:
			return self.note.created_at < other.note.created_at
		else:
			return self.note.edited_at < other.note.edited_at

	def add_note(self):
		if self.mode == "Notes":
			self.parent_app.notesListWidget.insertItem(0, self)
			self.parent_app.notesListWidget.setItemWidget(self, self.widget)
		else:
			self.parent_app.archiveListWidget.insertItem(0, self)
			self.parent_app.archiveListWidget.setItemWidget(self, self.widget)

	def delete_note_with_mb(self):
		mb = QMessageBox.question(self.parent_app, 'Confirmation', 'Are you sure want to delete this note?')
		if mb == QMessageBox.Yes:
			self.delete_note()
		return mb

	def delete_note(self):
		if self.mode == "Notes":
			self.parent_app.notesListWidget.takeItem(self.parent_app.notesListWidget.row(self))
		else:
			self.parent_app.archiveListWidget.takeItem(self.parent_app.archiveListWidget.row(self))

	def archive_note(self):
		self.delete_note()
		MyListItem(MyNote(self.note.text, self.note.tag, self.note.created_at, current_time()), self.parent_app, "Archive")

	def edit_note(self, new_text):
		self.delete_note()
		MyListItem(MyNote(new_text, self.note.tag, self.note.created_at, current_time()), self.parent_app, "Notes")

	def restore_note(self):
		self.delete_note()
		MyListItem(MyNote(self.note.text, self.note.tag, self.note.created_at, current_time()), self.parent_app, "Notes")


class MyDialog(Ui_Dialog):
	def __init__(self, item, qd):
		super().__init__()
		self.qd = qd
		self.setupUi(self.qd)
		self.item = item
		self.noteEdit.setPlainText(self.item.note.text)
		self.saveButton.clicked.connect(self.save_note)
		self.archiveButton.clicked.connect(self.archive_note)
		self.deleteButton.clicked.connect(self.delete_note)
		self.timeInfo.setText("Edited: " + str(self.item.note.edited_at) + "   Created: " + str(self.item.note.created_at))

		self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self.noteEdit)
		self.save_shortcut.activated.connect(self.save_note)

		tag_info = ""
		tag = self.item.note.tag
		while tag is not None:
			tag_info = tag.text + ", " + tag_info
			tag = tag.parent
		self.tagInfo.setText("Tags: " + tag_info[:-2])

	def save_note(self):
		self.item.edit_note(self.noteEdit.toPlainText())
		self.qd.accept()

	def archive_note(self):
		self.item.archive_note()
		self.qd.reject()

	def delete_note(self):
		mb = self.item.delete_note_with_mb()
		if mb == QMessageBox.Yes:
			self.qd.reject()


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
			my_tag = MyTagTree(uuid4(), tag_name, self.current_tag.my_tag)
			self.current_tag.my_tag.links.append(my_tag)
			self.current_tag.addChild(MyTreeItem(my_tag))
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


def main():
	app = QApplication(sys.argv)
	w = MyApp()
	w.show()
	app.exec_()


if __name__ == '__main__':
	main()
