#!/usr/bin/env python
# encoding: utf-8

__author__ = "Tacey Wong"

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage(u"准备")

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"状态栏")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
