import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        # Used custom label, only to have access to the HTML link option. (Text Browser might be better?)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)

        self.label = QLabel(content)
        self.label.setOpenExternalLinks(True)

        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)

        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)


class CustomButtonPopup(QWidget):
    def __init__(self, txt):
        super().__init__()

    # todo: fix the hardcoded geometry values.

        self.resize(500, 300)
        self.btn = QToolButton(self)
        self.btn.setGeometry(QRect(10, 100, 100, 50))
        self.btn.setCheckable(True)
        self.btn.setText("Press me")

        self.txtFrame = QFrame(self)
        self.txtFrame.setGeometry(QRect(100, 30, 400, 300))
        self.txtFrame.setVisible(False)

        self.gridLayoutWidget = QWidget(self.txtFrame)
        self.gridLayoutWidget.setGeometry(QRect(100, 10, 280, 300))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)

        self.horizontalLayoutWidget = QWidget(self.gridLayoutWidget)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 280, 250))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)

        self.lblButtonText = ScrollLabel(self.horizontalLayoutWidget)
        self.lblButtonText.setText(txt)
        self.horizontalLayout.addWidget(self.lblButtonText)

        self.btn.clicked.connect(self.txtFrame.setVisible)
        self.btn.clicked.connect(self.draw_line)
        self.btn.clicked.connect(
            lambda: self.btn.setText("Close dialog") if self.btn.isChecked() else self.btn.setText("Press me"))

        self.setStyleSheet(
            "QFrame{border: 0px; font-size: 11px; color: green;} QLabel{background: rgba(255,255,255,0);} QLabel::hover{background: rgba(255,255,255,255);}")

    def draw_line(self):
        # button = self.sender()

        # fire the paintEvent again.
        self.update()

    def paintEvent(self, e):
        pass
        # def paint(self):
        painter = QPainter(self)
        pen = QPen(Qt.red)
        pen.setWidth(5)
        # pen.setCapStyle(Qt.FlatCap)
        # pen.setCapStyle(Qt.SquareCap)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        if self.txtFrame.isVisible():

            painter.drawPolyline(QPolygon(
                [QPoint(110, 120), QPoint(190, 30), QPoint(490, 30)]))
        # else:
            # painter.eraseRect(100, 10, 550, 440)
            # painter.eraseRect(0, 0, 0, 0)

    def mousePressEvent(self, e):
        # Close the dialog with mouse press on widget.
        if self.txtFrame.isVisible():
            self.btn.click()


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(800, 800)
        layout = QGridLayout()
        self.setLayout(layout)

        btn = CustomButtonPopup('<b><span style="color:#25257F; font-size:24px"><a href="https://www.visitoslo.com/en">Oslo</a></span></b><br><br><br> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        btn2 = CustomButtonPopup('<b><span style="color:#25257F; font-size:24px"><a href="https://www.visitbergen.com/en">Bergen</a></span></b><br><br><br> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        btn3 = CustomButtonPopup(
            '<b><span style="color:#25257F; font-size:24px"><a href="https://www.visittrondheim.no">Trondheim</a></span></b>')
        layout.addWidget(btn, 0, 1, 1, 1)
        layout.addWidget(btn2, 1, 1, 1, 1)
        layout.addWidget(btn3, 2, 1, 1, 1)


app = QApplication(sys.argv)
# ex = CustomButtonPopup()
ex = Window()
ex.show()
sys.exit(app.exec_())
