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

        self.resize(250,150)
        self.center()

        self.setWindowTitle(u"窗口居中")
        self.show()

    def center(self):
        #得到一个矩形区域
        qr = self.frameGeometry()
        #提供桌面信息,包括屏幕尺寸
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
