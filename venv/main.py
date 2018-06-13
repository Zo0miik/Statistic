# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from Model.StatsMetods import *

def main():
    app = QApplication(sys.argv)
    window = WindowApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()