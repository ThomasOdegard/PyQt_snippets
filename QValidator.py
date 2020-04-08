from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtGui import QIntValidator, QValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout
import sys


#https://doc.qt.io/qt-5/qvalidator.html
#https://doc.qt.io/qt-5/qintvalidator.html

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.layout = QVBoxLayout()
        self.le1 = QLineEdit()
        self.b1 = QPushButton("Validate")
        self.le1.setPlaceholderText("value between 10 and 50")

        self.layout.addWidget(self.le1)
        self.layout.addWidget(self.b1)

        self.w = QWidget()
        self.w.setLayout(self.layout)
        self.setCentralWidget(self.w)
        self.show()

        # Accepts input values from 1 to 99999, but Acceptable is from 1 to 10000
        self.int_validator = QIntValidator(1, 10000, self.le1)

        # Set restricted range from 10 to 50 - Accepts input values from 1 to 99, but accetable is from 10 to 50
        self.int_validator.setRange(10, 50)

        self.le1.setValidator(self.int_validator)

        # Should not be called if the value is not valid
        self.le1.editingFinished.connect(self.isValid)
        # Should not be called if the value is not valid
        self.le1.returnPressed.connect(self.isValid)
        self.b1.pressed.connect(self.isValid)

    def isValid(self):

        valid, _text, _npos = QIntValidator.validate(
            self.int_validator, self.le1.text(), self.le1.cursorPosition())

        if valid == QValidator.Acceptable:
            print("Valid " + self.le1.text())

        elif valid == QValidator.Intermediate:
            print("Close, but not valid")

        elif valid == QValidator.Invalid:
            print("This is clearly not valid")


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
