

import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 400

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.leditHide = QLineEdit()
        self.leditHide.setPlaceholderText("search Name - Hide the rest")
        self.layout.addWidget(self.leditHide)
        self.leditColor = QLineEdit()
        self.leditColor.setPlaceholderText("search Name - Color result green")
        self.layout.addWidget(self.leditColor)

        self.leditHide.textChanged.connect(
            lambda: self.filter(self.leditHide.text()))
        self.leditColor.textChanged.connect(
            lambda: self.filter(self.leditColor.text(), color=True))
        self.setLayout(self.layout)

        # Show window
        self.show()

    @pyqtSlot()
    def filter(self, txt, color=False):
        self.txt = txt
        # print(self.txt)
        # print(self.tableWidget.rowCount())
        # print(self.tableWidget.item(0, 0).text())

        if self.txt != "":
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0).text().lower().startswith(self.txt.lower()):
                    if color == True:
                        self.tableWidget.item(
                            i, 0).setBackground(QColor(0, 255, 0))
                        self.tableWidget.item(
                            i, 1).setBackground(QColor(0, 255, 0))
                    else:
                        self.tableWidget.showRow(i)

                else:
                    if color == True:
                        self.tableWidget.item(i, 0).setBackground(
                            QColor(255, 255, 255))
                        self.tableWidget.item(i, 1).setBackground(
                            QColor(255, 255, 255))
                    else:
                        self.tableWidget.hideRow(i)
        else:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.item(i, 0).setBackground(
                    QColor(255, 255, 255))
                self.tableWidget.item(i, 1).setBackground(
                    QColor(255, 255, 255))
                self.tableWidget.showRow(i)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    # Create table

    def createTable(self):
        self.tableWidget = QTableWidget()

        # Row count
        self.tableWidget.setRowCount(5)

        # Column count
        self.tableWidget.setColumnCount(2)

        headers = ("Name", "City")
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Ola"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Bergen"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Jan"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Oslo"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Stavanger"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Arne"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Trondheim"))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("Arvid"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("Tromsø"))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.tableWidget.clicked.connect(self.on_click)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
