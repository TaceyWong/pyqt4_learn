#!/usr/bin/env python
# encoding: utf-8

__author__ = "Tacey Wong"

import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250,250)
    w.move(300,300)
    w.setWindowTitle(u"Simple 示例")
    w.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
