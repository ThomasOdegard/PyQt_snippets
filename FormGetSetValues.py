import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 120)
        self.list_lines = []

        layout = QGridLayout()

        label = QLabel("1 + 1")
        self.lineEdit = QLineEdit()
        layout.addWidget(label, 0, 0)
        layout.addWidget(self.lineEdit, 0, 1)

        label_2 = QLabel("1 + 2")
        self.lineEdit_2 = QLineEdit()
        layout.addWidget(label_2, 1, 0)
        layout.addWidget(self.lineEdit_2, 1, 1)

        button = QPushButton("Write to list")
        button.clicked.connect(self.get_text)
        layout.addWidget(button, 2, 0, 1, 1, Qt.AlignLeft)
        layout.setRowMinimumHeight(2, 55)

        button2 = QPushButton("Get from list")
        button2.clicked.connect(self.set_text)
        layout.addWidget(button2, 2, 1, 1, 1, Qt.AlignRight)
        layout.setRowMinimumHeight(2, 55)

        self.setLayout(layout)

    def get_text(self):
        for _ in form.findChildren(QLineEdit):
            self.list_lines.append(_.text())
        print(self.list_lines)

    def set_text(self):
        for _, __ in enumerate(form.findChildren(QLineEdit)):
            __.setText(self.list_lines[_])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
