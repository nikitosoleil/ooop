from PyQt5.QtWidgets import *

from mainwindow import Ui_MainWindow
from abstractions import Dict, Set
from custom_list import CustomList
from builtin_list import BuiltinList
from hash_table import HashTable


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttons = dict()
        self.buttons['dict'] = [self.get_by_key_button, self.set_by_key_button, self.remove_by_key_button]
        self.buttons['set'] = [self.is_in_button, self.add_button, self.remove_button]
        self.buttons['all'] = self.buttons['dict'] + self.buttons['set']
        self.buttons['drivers'] = [self.custom_list_button, self.builtin_list_button, self.hash_table_button]

        for button in self.buttons['all']:
            button.setEnabled(False)
            button.hide()

        for button in self.buttons['drivers']:
            button.setEnabled(False)

        self.abstraction = None
        self.driver = None
        self.structure = None

        self.abstractions = {'set': Set, 'dict': Dict}
        self.drivers = {'custom_list': CustomList, 'builtin_list': BuiltinList, 'hash_table': HashTable}

        self.dict_button.clicked.connect(lambda: self.activate_abstraction('dict'))
        self.set_button.clicked.connect(lambda: self.activate_abstraction('set'))

        self.custom_list_button.clicked.connect(lambda: self.activate_driver('custom_list'))
        self.builtin_list_button.clicked.connect(lambda: self.activate_driver('builtin_list'))
        self.hash_table_button.clicked.connect(lambda: self.activate_driver('hash_table'))

        self.get_by_key_button.clicked.connect(self.get_by_key)
        self.set_by_key_button.clicked.connect(self.set_by_key)
        self.remove_by_key_button.clicked.connect(self.remove_by_key)

        self.is_in_button.clicked.connect(self.is_in)
        self.add_button.clicked.connect(self.add)
        self.remove_button.clicked.connect(self.remove)

    def activate_abstraction(self, abstraction: str):
        self.abstraction = abstraction
        for button in self.buttons['all']:
            button.hide()
        for button in self.buttons[abstraction]:
            button.show()
        for button in self.buttons['drivers']:
            button.setEnabled(True)
        self.update_structure()

    def activate_driver(self, driver: str):
        self.driver = driver
        for button in self.buttons['all']:
            button.setEnabled(True)
        self.update_structure()

    def update_structure(self):
        if self.abstraction is not None and self.driver is not None:
            self.structure = self.abstractions[self.abstraction](self.drivers[self.driver]())
            self.items_list.clear()

    def get_by_key(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a key: ')
        if ok:
            value, time = self.structure.get(key)
            self.print_time(time)
            mb = QMessageBox()
            mb.setWindowTitle('R2esult')
            if value is not None:
                mb.setText(str(value))
            else:
                mb.setText('There is no such key')
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()
        self.update_list()

    def set_by_key(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a key: ')
        if ok:
            value, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a value: ')
            if ok:
                _, time = self.structure.set(key, value)
                self.print_time(time)
        self.update_list()

    def remove_by_key(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a key: ')
        if ok:
            _, time = self.structure.remove(key)
            self.print_time(time)
        self.update_list()

    def is_in(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a value: ')
        if ok:
            result, time = self.structure.isin(key)
            self.print_time(time)
            mb = QMessageBox()
            mb.setWindowTitle('Result')
            if result is not None:
                mb.setText('Yes')
            else:
                mb.setText('No')
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()
        self.update_list()

    def add(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a value: ')
        if ok:
            _, time = self.structure.add(key)
            self.print_time(time)
        self.update_list()

    def remove(self):
        key, ok = QInputDialog.getInt(self, 'Integer input', 'Enter a value: ')
        if ok:
            _, time = self.structure.remove(key)
            self.print_time(time)
        self.update_list()

    def update_list(self):
        self.items_list.clear()
        if self.abstraction == 'set':
            for item in self.structure.items():
                self.items_list.insertItem(0, QListWidgetItem(str(item)))
        else:
            for key, value in self.structure.items():
                self.items_list.insertItem(0, QListWidgetItem(f'{key}: {value}'))

    def print_time(self, time):
        self.time_status.showMessage(f'Time taken: {time:.6f} seconds', 10000)
