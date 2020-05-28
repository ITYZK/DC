#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from mainWindow import Ui_YZK
from PyQt5 import QtWidgets


class DC:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        form = QtWidgets.QMainWindow()
        self.w = Ui_YZK()
        self.w.setupUi(form)
        form.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    dc = DC()

