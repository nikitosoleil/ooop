from dialog import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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
