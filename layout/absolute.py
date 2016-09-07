#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QtGui.QLabel("Tacey Wong",self)
        lbl1.move(15,10)
        lbl2 = QtGui.QLabel("Tacey Wong",self)
        lbl2.move(35,40)
        lbl3 = QtGui.QLabel("Tacey Wong",self)
        lbl3.move(55,70)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"绝对布局")
        self.setWindowIcon(QtGui.QIcon("../icons/X- Coordinate-96.png"))
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
