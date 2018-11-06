# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tagTreeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.tagTreeWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.tagTreeWidget.setAnimated(False)
        self.tagTreeWidget.setHeaderHidden(False)
        self.tagTreeWidget.setObjectName("tagTreeWidget")
        self.verticalLayout_3.addWidget(self.tagTreeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tagEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tagEdit.setFrame(True)
        self.tagEdit.setClearButtonEnabled(True)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout.addWidget(self.tagEdit)
        self.addTagButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTagButton.sizePolicy().hasHeightForWidth())
        self.addTagButton.setSizePolicy(sizePolicy)
        self.addTagButton.setMinimumSize(QtCore.QSize(28, 28))
        self.addTagButton.setMaximumSize(QtCore.QSize(28, 28))
        self.addTagButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTagButton.setIcon(icon1)
        self.addTagButton.setObjectName("addTagButton")
        self.horizontalLayout.addWidget(self.addTagButton)
        self.deleteTagButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteTagButton.setMinimumSize(QtCore.QSize(28, 0))
        self.deleteTagButton.setMaximumSize(QtCore.QSize(28, 16777215))
        self.deleteTagButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteTagButton.setIcon(icon2)
        self.deleteTagButton.setObjectName("deleteTagButton")
        self.horizontalLayout.addWidget(self.deleteTagButton)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.Notes = QtWidgets.QWidget()
        self.Notes.setObjectName("Notes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Notes)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.Notes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.notesListWidget = QtWidgets.QListWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.notesListWidget.sizePolicy().hasHeightForWidth())
        self.notesListWidget.setSizePolicy(sizePolicy)
        self.notesListWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.notesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.notesListWidget.setObjectName("notesListWidget")
        self.addButton = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(0, 33))
        self.addButton.setMaximumSize(QtCore.QSize(16777215, 33))
        self.addButton.setText("")
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.noteEdit = QtWidgets.QTextEdit(self.splitter)
        self.noteEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteEdit.sizePolicy().hasHeightForWidth())
        self.noteEdit.setSizePolicy(sizePolicy)
        self.noteEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.noteEdit.setBaseSize(QtCore.QSize(0, 0))
        self.noteEdit.setDocumentTitle("")
        self.noteEdit.setAcceptRichText(False)
        self.noteEdit.setObjectName("noteEdit")
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.Notes, "")
        self.Archive = QtWidgets.QWidget()
        self.Archive.setObjectName("Archive")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Archive)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.archiveListWidget = QtWidgets.QListWidget(self.Archive)
        self.archiveListWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.archiveListWidget.setObjectName("archiveListWidget")
        self.verticalLayout_4.addWidget(self.archiveListWidget)
        self.tabWidget.addTab(self.Archive, "")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuSort = QtWidgets.QMenu(self.menubar)
        self.menuSort.setObjectName("menuSort")
        self.menuEdit_date = QtWidgets.QMenu(self.menuSort)
        self.menuEdit_date.setObjectName("menuEdit_date")
        self.menuCreation_date = QtWidgets.QMenu(self.menuSort)
        self.menuCreation_date.setObjectName("menuCreation_date")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.editAscending = QtWidgets.QAction(MainWindow)
        self.editAscending.setObjectName("editAscending")
        self.editDescending = QtWidgets.QAction(MainWindow)
        self.editDescending.setObjectName("editDescending")
        self.creationAscending = QtWidgets.QAction(MainWindow)
        self.creationAscending.setObjectName("creationAscending")
        self.creationDescending = QtWidgets.QAction(MainWindow)
        self.creationDescending.setObjectName("creationDescending")
        self.actionBreeze = QtWidgets.QAction(MainWindow)
        self.actionBreeze.setObjectName("actionBreeze")
        self.actionBreezeDark = QtWidgets.QAction(MainWindow)
        self.actionBreezeDark.setObjectName("actionBreezeDark")
        self.actionQDarkStyle = QtWidgets.QAction(MainWindow)
        self.actionQDarkStyle.setObjectName("actionQDarkStyle")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuEdit_date.addAction(self.editAscending)
        self.menuEdit_date.addAction(self.editDescending)
        self.menuCreation_date.addAction(self.creationAscending)
        self.menuCreation_date.addAction(self.creationDescending)
        self.menuSort.addAction(self.menuEdit_date.menuAction())
        self.menuSort.addAction(self.menuCreation_date.menuAction())
        self.menuTheme.addAction(self.actionBreeze)
        self.menuTheme.addAction(self.actionBreezeDark)
        self.menuTheme.addAction(self.actionQDarkStyle)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSort.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notes"))
        self.tagTreeWidget.headerItem().setText(0, _translate("MainWindow", "Tags"))
        self.tagEdit.setToolTip(_translate("MainWindow", "Name of the new tag"))
        self.tagEdit.setPlaceholderText(_translate("MainWindow", "Your tag goes here..."))
        self.addTagButton.setToolTip(_translate("MainWindow", "Add a new sub-tag to the selected one"))
        self.deleteTagButton.setToolTip(_translate("MainWindow", "Delete selected tag, all of his children and all of the notes in archive associated with it"))
        self.addButton.setToolTip(_translate("MainWindow", "Add a new note"))
        self.noteEdit.setToolTip(_translate("MainWindow", "Text of the new note"))
        self.noteEdit.setPlaceholderText(_translate("MainWindow", "Your note goes here..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Notes), _translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Archive), _translate("MainWindow", "Archive"))
        self.menuSort.setTitle(_translate("MainWindow", "Sort"))
        self.menuEdit_date.setTitle(_translate("MainWindow", "Edit date"))
        self.menuCreation_date.setTitle(_translate("MainWindow", "Creation date"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.editAscending.setText(_translate("MainWindow", "Ascending"))
        self.editDescending.setText(_translate("MainWindow", "Descending"))
        self.creationAscending.setText(_translate("MainWindow", "Ascending"))
        self.creationDescending.setText(_translate("MainWindow", "Descending"))
        self.actionBreeze.setText(_translate("MainWindow", "Breeze"))
        self.actionBreezeDark.setText(_translate("MainWindow", "BreezeDark"))
        self.actionQDarkStyle.setText(_translate("MainWindow", "QDarkStyle"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
