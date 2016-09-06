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
        QtGui.QToolTip.setFont(QtGui.QFont("SansSerif",10))

        self.setToolTip(u"这是<b>QWidget</b>组件")
        btn = QtGui.QPushButton(u"按钮",self)
        btn.setToolTip(u"这是<b>按钮</b>组件")
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"ToolTips")
        self.show()

def main():
        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()
