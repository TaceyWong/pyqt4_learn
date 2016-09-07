#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QtGui.QPushButton(u"是")
        cancelButton = QtGui.QPushButton(u"否")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"盒子布局")
        self.setWindowIcon(QtGui.QIcon("../icons/Cardboard-Box-96.png"))
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
