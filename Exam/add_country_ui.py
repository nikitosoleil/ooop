# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_country_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddCountryDialog(object):
    def setupUi(self, AddCountryDialog):
        AddCountryDialog.setObjectName("AddCountryDialog")
        AddCountryDialog.resize(320, 240)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddCountryDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(AddCountryDialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.twoButton = QtWidgets.QRadioButton(AddCountryDialog)
        self.twoButton.setObjectName("twoButton")
        self.buttonGroup = QtWidgets.QButtonGroup(AddCountryDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.twoButton)
        self.gridLayout.addWidget(self.twoButton, 1, 0, 1, 1)
        self.oneButton = QtWidgets.QRadioButton(AddCountryDialog)
        self.oneButton.setChecked(True)
        self.oneButton.setObjectName("oneButton")
        self.buttonGroup.addButton(self.oneButton)
        self.gridLayout.addWidget(self.oneButton, 0, 0, 1, 1)
        self.threeButton = QtWidgets.QRadioButton(AddCountryDialog)
        self.threeButton.setObjectName("threeButton")
        self.buttonGroup.addButton(self.threeButton)
        self.gridLayout.addWidget(self.threeButton, 0, 1, 1, 1)
        self.fourButton = QtWidgets.QRadioButton(AddCountryDialog)
        self.fourButton.setObjectName("fourButton")
        self.buttonGroup.addButton(self.fourButton)
        self.gridLayout.addWidget(self.fourButton, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.addRandomButton = QtWidgets.QPushButton(AddCountryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRandomButton.sizePolicy().hasHeightForWidth())
        self.addRandomButton.setSizePolicy(sizePolicy)
        self.addRandomButton.setObjectName("addRandomButton")
        self.horizontalLayout.addWidget(self.addRandomButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddCountryDialog)
        QtCore.QMetaObject.connectSlotsByName(AddCountryDialog)

    def retranslateUi(self, AddCountryDialog):
        _translate = QtCore.QCoreApplication.translate
        AddCountryDialog.setWindowTitle(_translate("AddCountryDialog", "Add country"))
        self.textEdit.setPlaceholderText(_translate("AddCountryDialog", "Country name..."))
        self.twoButton.setText(_translate("AddCountryDialog", "Type 2"))
        self.oneButton.setText(_translate("AddCountryDialog", "Type 1"))
        self.threeButton.setText(_translate("AddCountryDialog", "Type 3"))
        self.fourButton.setText(_translate("AddCountryDialog", "Type 4"))
        self.addRandomButton.setText(_translate("AddCountryDialog", "Add country"))

