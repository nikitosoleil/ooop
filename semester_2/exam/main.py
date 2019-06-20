import os
import sys

os.system('pyuic5 mainwindow.ui -o mainwindow.py')

from PyQt5.QtWidgets import *

from app import App


def main():
    app = QApplication(sys.argv)
    w = App()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
