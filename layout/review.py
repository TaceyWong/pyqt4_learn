#!/usr/bin/env python
# encoding: utf-8

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        title = QtGui.QLabel(u"标题")
        author = QtGui.QLabel(u"作者")
        review = QtGui.QLabel(u"评论")

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle(u"网格布局-评论")
        self.setWindowIcon(QtGui.QIcon("../icons/Survey-96.png"))
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
