# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_product_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewProductDialog(object):
    def setupUi(self, ViewProductDialog):
        ViewProductDialog.setObjectName("ViewProductDialog")
        ViewProductDialog.resize(320, 320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ViewProductDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stats = QtWidgets.QLabel(ViewProductDialog)
        self.stats.setObjectName("stats")
        self.horizontalLayout_2.addWidget(self.stats)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.productsWidget = QtWidgets.QTableWidget(ViewProductDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productsWidget.sizePolicy().hasHeightForWidth())
        self.productsWidget.setSizePolicy(sizePolicy)
        self.productsWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.productsWidget.setObjectName("productsWidget")
        self.productsWidget.setColumnCount(2)
        self.productsWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productsWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productsWidget.setHorizontalHeaderItem(1, item)
        self.productsWidget.horizontalHeader().setDefaultSectionSize(70)
        self.productsWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.productsWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ViewProductDialog)
        QtCore.QMetaObject.connectSlotsByName(ViewProductDialog)

    def retranslateUi(self, ViewProductDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewProductDialog.setWindowTitle(_translate("ViewProductDialog", "Product details"))
        self.stats.setText(_translate("ViewProductDialog", "Stats"))
        item = self.productsWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewProductDialog", "Count"))
        item = self.productsWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewProductDialog", "Product name"))

