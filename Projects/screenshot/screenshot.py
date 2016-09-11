# coding:utf-8

from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QGroupBox
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QSpinBox ,QSizePolicy
from PyQt4.QtGui import QVBoxLayout ,QDesktopServices ,QImageWriter

from PyQt4.QtCore import QRect ,QSize,QTimer,QDir ,QLatin1String
from PyQt4.QtCore import Qt,QStringList

from PyQt4.QtGui import QApplication


class ScreenShot(QWidget):
    def __init__(self):
        super(ScreenShot,self).__init__()

        self.initUI()

    def initUI(self):
        self.originalPixmap = QPixmap()

        self.screenshotLabel= QLabel("screenshotlabel",self)
        self.screenshotLabel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.screenshotLabel.setAlignment(Qt.AlignCenter)

        self.screenGeometry = QApplication.desktop().screenGeometry() #Qrect()
        print self.screenGeometry ,self.screenGeometry.width()
        self.screenshotLabel.setMinimumSize(self.screenGeometry.width()/8,self.screenGeometry.height()/8)

        mainlayout = QVBoxLayout(self)
        mainlayout.addWidget(self.screenshotLabel)

        self.optionsGroupBox = QGroupBox(u"选项",self)

        self.hideThisWindowCheckBox = QCheckBox(u"隐藏这个窗口", self.optionsGroupBox)
        self.optionsGroupBoxLayout = QGridLayout(self.optionsGroupBox)


        mainlayout.addWidget(self.optionsGroupBox)
        self.delaySpinBox = QSpinBox(self.optionsGroupBox)
        self.delaySpinBox.setSuffix(u"s")
        self.delaySpinBox.setMaximum(60)


        self.optionsGroupBoxLayout.addWidget(QLabel(u"截屏延时:", self), 0, 0)
        self.optionsGroupBoxLayout.addWidget(self.delaySpinBox, 0, 1)
        self.optionsGroupBoxLayout.addWidget(self.hideThisWindowCheckBox, 1, 0)


        buttonLayout = QHBoxLayout();

        self.newScreenshotButton = QPushButton(u"新截图",self)
        self.newScreenshotButton.clicked.connect(self.__newScreenshot)
        buttonLayout.addWidget(self.newScreenshotButton)

        saveScreenshotButton = QPushButton(u"保存截图", self)
        buttonLayout.addWidget(saveScreenshotButton)

        quitScreenshotButton = QPushButton(u"退出截图", self)
        quitScreenshotButton.setShortcut("Ctrl+Q")
        buttonLayout.addWidget(saveScreenshotButton)

        buttonLayout.addStretch()
        mainlayout.addLayout(buttonLayout)
        quitScreenshotButton.clicked.connect(self.close)

        saveScreenshotButton.clicked.connect(self.__saveScreenshot())
        self.delaySpinBox.valueChanged.connect(self.__updateCheckBox())
        self.delaySpinBox.setValue(5)
        self.setWindowTitle(u"截图")
        self.resize(300,200)


    def resizeEvent(self, QResizeEvent):
        scaledSize = self.originalPixmap.size()
        scaledSize.scale(self.screenshotLabel.size(), Qt.KeepAspectRatio)
        if (not self.screenshotLabel.pixmap() ) or (scaledSize != self.screenshotLabel.pixmap().size()):
            self.__updateScreenshotLabel()

    def __newScreenshot(self):
        if self.hideThisWindowCheckBox.isChecked():
            self.hide()

        self.newScreenshotButton.setDisabled(True)

        QTimer.singleShot(self.delaySpinBox.value() * 1000, self,self.__shootScreen())
    def __saveScreenshot(self):
        format = "png"
        initialPath = QDesktopServices.storageLocation(QDesktopServices.PicturesLocation)
        # initialPath = QStandardPaths::writableLocation(QStandardPaths::PicturesLocation);
        if initialPath.isEmpty():
            initialPath = QDir.currentPath()
        initialPath += "/untitled."+ format

        fileDialog = QtGui.QFileDialog(self, u"存储为", initialPath)
        fileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        fileDialog.setFileMode(QtGui.QFileDialog.AnyFile)
        fileDialog.setDirectory(initialPath)
        mimeTypes = QStringList()

        for bf in QImageWriter.supportedImageFormats():
            mimeTypes.append(QLatin1String(bf))

        # fileDialog.setMin setMimeTypeFilters(mimeTypes)
        # fileDialog.selectMimeTypeFilter("image/" + format);
        fileDialog.setDefaultSuffix(format);
        if fileDialog.accept():
            return

        fileName = fileDialog.selectedFiles().first();

        if not self.originalPixmap.save(fileName):
            QtGui.QMessageBox.Warning(self, u"保存错误",u"图像无法存储到 \"%s\"." %str(QDir.toNativeSeparators(fileName)))

    def __shootScreen(self):
        # screen = QtGuiApplication.primaryScreen()
        # window = windowHandle()



        # if window:
        #     screen = window.screen()

        # if not screen:
        #     return

        if self.delaySpinBox.value() != 0:
            QApplication.beep()

        self.originalPixmap = QPixmap.grabWindow(QApplication.desktop().winId())
        # self.originalPixmap = screen.grabWindow(0);
        self.__updateScreenshotLabel();

        self.newScreenshotButton.setDisabled(False);
        if self.hideThisWindowCheckBox.isChecked():
            self.show()
    def __updateCheckBox(self):
        print "sssss"
        if self.delaySpinBox.value() == 0 :
            self.hideThisWindowCheckBox.setDisabled(True)
            self.hideThisWindowCheckBox.setChecked(False)
        else:
            self.hideThisWindowCheckBox.setDisabled(False);

    def __updateScreenshotLabel(self):
        self.screenshotLabel.setPixmap(self.originalPixmap.scaled(self.screenshotLabel.size(),
                                                                          Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation))
