import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re


class App(QWidget):
    def __init__(self):
        super().__init__()
        # Create some widgets
        self.setGeometry(500, 500, 300, 150)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = QPushButton(
            'Get style property', self)

        self.layout.addWidget(self.button)
        self.verticalSpacer = QSpacerItem(1, 1,
                                          QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout.addItem(self.verticalSpacer)
        self.lbl = QLabel(
            'Type in css property (ea. border, background, color)')
        self.layout.addWidget(self.lbl)

        self.editor = QLineEdit(
            'border', self)

        self.editor.setStyleSheet('''border: 2px solid red;
                                  border-radius: 5px;
                                  padding: 0 4px;
                                  background: blue;
                                  color: white;
                                  selection-background-color: red;
                                  selection-color: blue;
                                  ''')

        self.layout.addWidget(self.editor)

        self.button.clicked.connect(lambda: print(
            "returned", self.get_style(style=self.editor.text(), get_all=True)))

    def get_style(self, style: str, get_all: bool = False) -> list:
        """Returning a list of selected QSS properties and values

        Args:
            style (str): pass in property ea. color, border
            get_all (bool, optional): If set to True, and you pass inn ea. (style='border') it will return every property staring with border (ea. border and border-radius). Defaults to False.

        Returns:
            list: [list contaning the properies and values. - Turned to key/value pairs by using dict(output) ]
        """

        if get_all:
            style += ".*"

        # I'll bet ther is a better way to do this, but.... - It's just a consept.
        styleSearch = re.compile(r"(^|\s)(" + style + r")\:\s*(.*)\;")
        output = re.findall(styleSearch, self.editor.styleSheet())

        output = [el[1:] for el in output]  # 0 index not used.

        for i in range(len(output)):
            for j in range(2):
                print(output[i][j])

        # output = dict(output) #Turns list into a dict if you need key/value pairs.
        return output


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    gui.show()
    app.exec_()
