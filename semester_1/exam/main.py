import os

#os.system('pyuic5 main_ui.ui -o main_ui.py')
#os.system('pyuic5 add_product_ui.ui -o add_product_ui.py')
#os.system('pyuic5 view_product_ui.ui -o view_product_ui.py')
#os.system('pyuic5 add_country_ui.ui -o add_country_ui.py')
#os.system('pyuic5 view_country_ui.ui -o view_country_ui.py')

import sys
from PyQt5.QtWidgets import *
from app import App


def main():
	app = QApplication(sys.argv)
	w = App()
	w.show()
	app.exec_()


if __name__ == '__main__':
	main()
