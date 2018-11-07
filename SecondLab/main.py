import os

# os.system('pyuic5 window.ui -o window.py')
# os.system('pyuic5 dialog.ui -o dialog.py')

import sys
from PyQt5.QtWidgets import *
from myapp import MyApp


def main():
	app = QApplication(sys.argv)
	w = MyApp()
	w.show()
	app.exec_()


if __name__ == '__main__':
	main()
