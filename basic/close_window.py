#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    def initUI(self):
        qbtn = QtGui.QPushButton(u"退出",self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"退出按钮")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
