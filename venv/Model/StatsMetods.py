# -*- coding: utf-8 -*-

import sys
import cmath
import numpy as np
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDesktopWidget, QComboBox, QLabel, QLineEdit
from View.StatsDesign import SummaryWindow

# float32 == float
# float64 == double


# инициализируем константы
M = np.random.randint(100)
N = np.random.randint(100)
K = np.random.randint(100)
MIN_INT = np.random.randint(100000)
MAX_INT = np.random.randint(100000)

class WindowApp(QWidget):

    def __init__(self):
        super().__init__()
        self. InitUi()

    def InitUi(self):

        self.ui = SummaryWindow()
        self.ui.setupUi(self)
# создаем кнопки
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(380, 100, 180, 20))
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(380, 140, 180, 20))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 180, 180, 20))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 220, 180, 20))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 260, 180, 20))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 300, 180, 20))
        self.lineEdit_6 = QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 340, 180, 20))
        self.lineEdit_7 = QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 380, 180, 20))
# создаем комбобокс
        combo = QComboBox(self)
        combo.addItems(["одномерный(int)",
                        "двумерный(int)",
                        "трехмерный(int)",
                        "одномерный(float)",
                        "двумерный(float)",
                        "трехмерный(float)",
                        "одномерный(double)",
                        "двумерный(double)",
                        "трехмерный(double)",
                        ])

        combo.move(40, 50)
        combo.currentIndexChanged.connect(self.selectionchange)

        self.center()
        self.show()

    def onActivated(self, text):
        getattr(self, self.fun[text])()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Вы дейтсвительно хотите выйти?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectionchange(self, i):

        if i == 0:
            self.one_int_array()
        if i == 1:
            self.two_int_array()
        if i == 2:
            self.three_int_array()
        if i == 3:
            self.one_float_array()
        if i == 4:
            self.two_float_array()
        if i == 5:
            self.three_float_array()
        if i == 6:
            self.one_double_array()
        if i == 7:
            self.two_double_array()
        if i == 8:
            self.three_double_array()

    def one_int_array(self):
        matrix = np.random.uniform(0, 2, size=M).astype(np.int32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))


    def two_int_array(self):
        matrix = np.random.uniform(-2000, 1501, size=(M, N)).astype(np.int32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def three_int_array(self):
        matrix = np.random.uniform(-MIN_INT, MAX_INT, size=(M, N, K)).astype(np.int32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def one_float_array(self):
        matrix = np.random.uniform(0, 2, size=M).astype(np.float32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def two_float_array(self):
        matrix = np.random.uniform(-2000, 1501, size=(M, N)).astype(np.float32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def three_float_array(self):
        matrix = np.random.uniform(-MIN_INT, MAX_INT, size=(M, N, K)).astype(np.float32)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def one_double_array(self):
        matrix = np.random.uniform(0, 2, size=M).astype(np.float64)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def two_double_array(self):
        matrix = np.random.uniform(-2000, 1501, size=(M, N)).astype(np.float64)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))

    def three_double_array(self):
        matrix = np.random.uniform(-MIN_INT, MAX_INT, size=(M, N, K)).astype(np.float64)
        average_value = matrix.mean()
        dispersion = matrix.var()
        min_elem = matrix.min()
        max_elem = matrix.max()
        delta = max_elem + min_elem
        shape = matrix.shape
        size_array = matrix.size
        type_array = matrix.dtype
        self.lineEdit.setText(str(average_value))
        self.lineEdit_1.setText(str(dispersion))
        self.lineEdit_2.setText(str(min_elem))
        self.lineEdit_3.setText(str(max_elem))
        self.lineEdit_4.setText(str(delta))
        self.lineEdit_5.setText(str(shape))
        self.lineEdit_6.setText(str(size_array))
        self.lineEdit_7.setText(str(type_array))





