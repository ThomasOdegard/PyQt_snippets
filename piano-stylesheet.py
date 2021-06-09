from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setStyleSheet(u"QPushButton:!pressed{background-color: white;"
                           "color:black;"
                           "border-color: rgb(139, 139, 139);"
                           "border-width: 4px;"
                           "border-style: inset;"
                           "}"

                           "QPushButton:pressed{background-color: blue;"
                           "color: white"
                           "}"

                           "QFrame > QPushButton:!pressed{background-color: black;"
                           "color: white;"
                           "border-color: rgb(90, 90, 90);"
                           "border-style: outset;"
                           "border-top: none;"
                           "}"

                           "QFrame > QPushButton:pressed {background-color: darkgreen;"
                           "color: black}"
                           )
        self.centralwidget = QWidget(self)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(10, 40, 60, 260))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(80, 40, 60, 260))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(150, 40, 60, 260))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(220, 40, 60, 260))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(290, 40, 60, 260))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(430, 40, 60, 260))
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QRect(360, 40, 60, 260))
        self.frame = QFrame(self.centralwidget)
        # self.frame.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.frame.setGeometry(QRect(10, 10, 450, 190))
        self.minor_5 = QPushButton(self.frame)
        self.minor_5.setGeometry(QRect(395, 30, 40, 160))
        self.minor_1 = QPushButton(self.frame)
        self.minor_1.setGeometry(QRect(45, 30, 40, 160))
        self.minor_4 = QPushButton(self.frame)
        self.minor_4.setGeometry(QRect(325, 30, 40, 160))
        self.minor_2 = QPushButton(self.frame)
        self.minor_2.setGeometry(QRect(115, 30, 40, 160))
        self.minor_3 = QPushButton(self.frame)
        self.minor_3.setGeometry(QRect(255, 30, 40, 160))

        self.pushButton.setText("C")
        self.pushButton_2.setText("D")
        self.pushButton_3.setText("E")
        self.pushButton_4.setText("F")
        self.pushButton_5.setText("G")
        self.pushButton_6.setText("B")
        self.pushButton_1.setText("A")
        self.minor_1.setText("C#\nDb")
        self.minor_2.setText("D#\nEb")
        self.minor_3.setText("F#\nGb")
        self.minor_4.setText("G#\nAb")
        self.minor_5.setText("A#\nBb")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = Ui_MainWindow()
    myWindow.show()
    app.exec_()
