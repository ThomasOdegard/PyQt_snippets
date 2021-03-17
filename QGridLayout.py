import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Grid layout samples")
        self.resize(800, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        # # layout.addWidget(QWidget(), row: int, column: int, rowSpan: int, columnSpan: int, alignment: flag)
        layout.addWidget(QLabel("1"), 0, 0)
        layout.addWidget(QLabel("2"), 0, 1, 1, 3)
        layout.addWidget(QLabel("3"), 1, 0, 1, 2)
        layout.addWidget(QLabel("4"), 1, 2, 1, 2)
        layout.addWidget(QLabel("6"), 0, 3, 2, 1)
        layout.addWidget(QLabel("7 center"), 0, 4, 2, 1, Qt.AlignCenter)
        layout.addWidget(QLabel("8 leading"), 0, 5, 2, 1, Qt.AlignLeading)
        layout.addWidget(QLabel("9 justify"), 0, 6, 2, 1, Qt.AlignJustify)
        layout.addWidget(QLabel("10 bottom"), 0, 7, 2, 1, Qt.AlignBottom)

        layout.addWidget(QLabel("11 absolute"), 3, 0, 1, 2)
        layout.addWidget(QLabel("12 baseline"), 3, 2, 1, 2)
        layout.addWidget(QLabel("13 justify"), 3, 4, 1, 2)
        layout.addWidget(QLabel("14 right"), 3, 6, 1, 2)
        layout.addWidget(QLabel("11 absolute"), 3, 0, 1, 2, Qt.AlignAbsolute)
        layout.addWidget(QLabel("12 baseline"), 3, 2, 1, 2, Qt.AlignBaseline)
        layout.addWidget(QLabel("13 justify"), 3, 4, 1, 2, Qt.AlignJustify)
        layout.addWidget(QLabel("14 right"), 3, 6, 1, 2, Qt.AlignRight)


# Random coloring.
        qsrand(QTime.currentTime().msec())
        for label in self.findChildren(QLabel):
            color = QColor(qrand() % 256, qrand() % 256, qrand() % 256)
            label.setStyleSheet('.QLabel{{background: rgb({}, {}, {});}}'.format(
                color.red(), color.green(), color.blue()))


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec_())
