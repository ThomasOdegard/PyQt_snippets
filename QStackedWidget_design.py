import sys
import os

from PySide2.QtCore import QFile, QObject, QEvent, Slot, Qt
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QCheckBox, QPlainTextEdit, qApp, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QTextEdit, QLabel, QTabWidget, QWidget, QStackedWidget
from PySide2.QtUiTools import QUiLoader
from functools import partial


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.window.show()
        self.stacked = self.window.findChild(QStackedWidget, 'stackedWidget')
        self.setup()

    def setup(self):

        # Could use other widgets then QPushButton, but then I have to use mouse event to get trigger signal...
        self.btnHome = self.window.findChild(QPushButton, 'btnHome')
        self.btnHome.clicked.connect(partial(self.setWidget, 0, "btnHome"))

        self.btnDBase = self.window.findChild(QPushButton, 'btnDBase')
        self.btnDBase.clicked.connect(partial(self.setWidget, 1, "btnDBase"))

        self.btnDownload = self.window.findChild(QPushButton, 'btnDownload')
        self.btnDownload.clicked.connect(
            partial(self.setWidget, 2, "btnDownload"))

        self.btnSetting = self.window.findChild(QPushButton, 'btnSetting')
        self.btnSetting.clicked.connect(
            partial(self.setWidget, 3, "btnSetting"))

        self.btnSave = self.window.findChild(QPushButton, 'btnSave')
        self.btnSave.clicked.connect(self.save)
        # self.btnSave.setEnabled(False)

    def style(self):
        self.btnHome.setStyleSheet("background-color:rgba(0, 0, 0, 0)")
        self.btnSetting.setStyleSheet("background-color:rgba(0, 0, 0, 0)")
        self.btnDownload.setStyleSheet("background-color:rgba(0, 0, 0, 0)")
        self.btnDBase.setStyleSheet("background-color:rgba(0, 0, 0, 0)")


# Adding custom style, or else the focus is lost if any other button on the window is pushed and the color is lost.
    def setWidget(self, page, btn):
        self.window.findChild(
            QStackedWidget, 'stackedWidget').setCurrentIndex(page)
        self.style() #Reset style.
        style = 'self.%s.setStyleSheet("background-color:  rgb(208, 232, 218); border: none; ")' % btn
        eval(style)

    def save(self):
        print("Hi from Save")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('QStackedWidget_design.ui')

    sys.exit(app.exec_())
