# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_country_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewCountryDialog(object):
    def setupUi(self, ViewCountryDialog):
        ViewCountryDialog.setObjectName("ViewCountryDialog")
        ViewCountryDialog.resize(480, 320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ViewCountryDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.productsWidget = QtWidgets.QTableWidget(ViewCountryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productsWidget.sizePolicy().hasHeightForWidth())
        self.productsWidget.setSizePolicy(sizePolicy)
        self.productsWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.productsWidget.setObjectName("productsWidget")
        self.productsWidget.setColumnCount(3)
        self.productsWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productsWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsWidget.setHorizontalHeaderItem(2, item)
        self.productsWidget.horizontalHeader().setDefaultSectionSize(90)
        self.productsWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.productsWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ViewCountryDialog)
        QtCore.QMetaObject.connectSlotsByName(ViewCountryDialog)

    def retranslateUi(self, ViewCountryDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewCountryDialog.setWindowTitle(_translate("ViewCountryDialog", "Country details"))
        item = self.productsWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewCountryDialog", "Activity"))
        item = self.productsWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewCountryDialog", "Count"))
        item = self.productsWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewCountryDialog", "Product name"))

