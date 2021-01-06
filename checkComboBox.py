import sys
from PyQt5.QtWidgets import (QLineEdit, QWidget, QGridLayout, QMenu, QAction,
                             QComboBox, QPushButton, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.txtBox = QLineEdit()
        self.menu = QMenu()
        self.btn = QPushButton("Dropdown")
        self.cmbox = CheckableComboBox()
        self.btn2 = QPushButton("Test checked")

        self.Act1 = QAction("Action 1", self.menu)
        self.Act1.setCheckable(True)
        self.Act2 = QAction("Action 2", self.menu)
        self.Act2.setCheckable(True)

        self.menu.addAction(self.Act1)
        self.menu.addAction(self.Act2)
        self.btn.setMenu(self.menu)

        grid.addWidget(self.txtBox, 0, 0, 1, 3)
        grid.addWidget(self.btn, 1, 0)
        grid.addWidget(self.cmbox, 1, 1)
        grid.addWidget(self.btn2, 1, 2)

        for i in range(3, 5):
            self.cmbox.addItem("Action " + str(i))

        self.btn2.clicked.connect(self.test_checked)
        self.cmbox.view().pressed.connect(self.handle_item_pressed)  # WIP

        self.move(300, 150)
        self.setMinimumWidth(800)
        self.setWindowTitle('checkComboBox')
        self.show()

    def test_checked(self, attr1):
        print(self.Act1.isChecked())
        print(self.Act2.isChecked())
        print(self.cmbox.isChecked(0))
        print(self.cmbox.isChecked(1))

        self.txtBox.setText("Action 1 is: " + str(self.Act1.isChecked()) +
                            " and Action 2 is: " + str(self.Act2.isChecked()) +
                            " and Action 3 is: " + str(self.cmbox.isChecked(0)) +
                            " and Action 4 is: " + str(self.cmbox.isChecked(1)))

    # TODO - Fix for chkbox and not only text.
    def handle_item_pressed(self, index):
        item = self.cmbox.model().itemFromIndex(index)
        print(item.checkState())


class CheckableComboBox(QComboBox):
    def addItem(self, item, no_check=False):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1, 0)

        if no_check != False:
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable |
                          Qt.ItemIsEnabled)
        else:
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            # set an initial checkState to make the checkBox appear
            item.setCheckState(Qt.Unchecked)

    def isChecked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
