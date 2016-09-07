#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names =[u'清除',u'回退','',u'关闭',
                '7','8','9','/',
                '4','5','6','*',
                '1','2','3','-',
                '0','.','=','+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position , name  in zip(positions,names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button,*position)



        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"网格布局-计算器")
        self.setWindowIcon(QtGui.QIcon("../icons/Calculator-96.png"))
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
