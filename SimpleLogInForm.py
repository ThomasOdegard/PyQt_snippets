from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.layout = QVBoxLayout()
        self.te = QTextEdit()
        self.le1 = QLineEdit()
        self.le1.setPlaceholderText("Username")
        self.le2 = QLineEdit()
        self.le2.setPlaceholderText("Password")
        b1 = QPushButton("Login")
        b1.pressed.connect(self.login)
        b2 = QPushButton("Logout")
        b2.pressed.connect(self.logout)

        self.layout.addWidget(self.le1)
        self.layout.addWidget(self.le2)
        self.layout.addWidget(b1)
        self.layout.addWidget(b2)
        self.layout.addWidget(self.te)

        self.w = QWidget()
        self.w.setLayout(self.layout)

        self.setCentralWidget(self.w)

        self.show()
        self.te.hide()

        # self.le1.setText("name")
        # self.le2.setText("pass")

    def login(self):
        if self.le1.text() == "name" and self.le2.text() == "pass":
            print("You have been logged in")
            self.te.show()
        else:
            print("Username = name, Password = pass")

    def logout(self):
        print("You have been logged out")
        self.le1.setText("")
        self.le2.setText("")
        self.te.hide()


app = QApplication([])
window = MainWindow()
app.exec_()
