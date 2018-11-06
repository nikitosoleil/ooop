# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(500, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.noteEdit = QtWidgets.QTextEdit(Dialog)
        self.noteEdit.setObjectName("noteEdit")
        self.verticalLayout.addWidget(self.noteEdit)
        self.timeInfo = QtWidgets.QLabel(Dialog)
        self.timeInfo.setObjectName("timeInfo")
        self.verticalLayout.addWidget(self.timeInfo)
        self.tagInfo = QtWidgets.QLabel(Dialog)
        self.tagInfo.setObjectName("tagInfo")
        self.verticalLayout.addWidget(self.tagInfo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.archiveButton = QtWidgets.QPushButton(Dialog)
        self.archiveButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.archiveButton.setObjectName("archiveButton")
        self.horizontalLayout.addWidget(self.archiveButton)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit note"))
        self.timeInfo.setText(_translate("Dialog", "TextLabel"))
        self.tagInfo.setText(_translate("Dialog", "TextLabel"))
        self.deleteButton.setToolTip(_translate("Dialog", "Permanently delete note"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.archiveButton.setToolTip(_translate("Dialog", "Move note to archive"))
        self.archiveButton.setText(_translate("Dialog", "Archive"))
        self.saveButton.setToolTip(_translate("Dialog", "Save made changes"))
        self.saveButton.setText(_translate("Dialog", "Save"))

