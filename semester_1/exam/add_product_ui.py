# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_product_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        AddProductDialog.setObjectName("AddProductDialog")
        AddProductDialog.resize(320, 240)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddProductDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(AddProductDialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rawButton = QtWidgets.QRadioButton(AddProductDialog)
        self.rawButton.setChecked(True)
        self.rawButton.setObjectName("rawButton")
        self.buttonGroup = QtWidgets.QButtonGroup(AddProductDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rawButton)
        self.verticalLayout_3.addWidget(self.rawButton)
        self.endButton = QtWidgets.QRadioButton(AddProductDialog)
        self.endButton.setObjectName("endButton")
        self.buttonGroup.addButton(self.endButton)
        self.verticalLayout_3.addWidget(self.endButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.addRandomButton = QtWidgets.QPushButton(AddProductDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRandomButton.sizePolicy().hasHeightForWidth())
        self.addRandomButton.setSizePolicy(sizePolicy)
        self.addRandomButton.setObjectName("addRandomButton")
        self.horizontalLayout.addWidget(self.addRandomButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AddProductDialog)
        QtCore.QMetaObject.connectSlotsByName(AddProductDialog)

    def retranslateUi(self, AddProductDialog):
        _translate = QtCore.QCoreApplication.translate
        AddProductDialog.setWindowTitle(_translate("AddProductDialog", "Add product"))
        self.textEdit.setPlaceholderText(_translate("AddProductDialog", "Product name..."))
        self.rawButton.setText(_translate("AddProductDialog", "Raw"))
        self.endButton.setText(_translate("AddProductDialog", "End"))
        self.addRandomButton.setText(_translate("AddProductDialog", "Add product"))

