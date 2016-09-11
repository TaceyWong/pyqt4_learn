# coding:utf-8

import sys
from PyQt4.QtGui import QDesktopWidget
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QPoint
from screenshot import ScreenShot
app =  QApplication(sys.argv)
screenshot = ScreenShot()
screenshot.move(QApplication.desktop().availableGeometry(screenshot).topLeft() + QPoint(20, 20))
screenshot.show()
sys.exit(app.exec_())