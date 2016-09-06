#!/usr/bin/env python
# encoding: utf-8

__author__ = "Tacey Wong"

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,250)
        self.setWindowTitle(u"Icon 示例")
        self.setWindowIcon(QtGui.QIcon("web.png"))

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

