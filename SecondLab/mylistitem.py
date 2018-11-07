from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mynote import MyNote
from help import *


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
