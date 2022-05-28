import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class combodemo(QWidget):
    def __init__(self, parent=None):
        super(combodemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")
        self.setGeometry(QRect(100, 100, 300, 150))

        self.cb.setEditable(True)
        self.cb.setCurrentIndex(-1)
        self.cb.lineEdit().setPlaceholderText("--Select Programming language--")

    def selectionchange(self, i):

        if i != -1:
            print("Current index", i, "selection changed ", self.cb.currentText())
            self.cb.model().item(i).setEnabled(False)


def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
