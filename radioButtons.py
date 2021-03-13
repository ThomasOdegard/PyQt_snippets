
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.best_town = ""
        self.population = ""
        self.area = ""
        self.web = ""
        self.urlLink = ""

        self.towns = [
            ("Oslo", ("Population: 634,293 (2014)", "Area: 455 km²",
                      "https://www.visitoslo.com/en")),
            ("Bergen", ("Population: 271,949 (2014)",
                        "Area: 445 km²", "https://en.visitbergen.com")),
            ("Trondheim", ("Population: 182,035 (2014)",
                           "Area: 321.8 km²", "https://www.visittrondheim.no")),
            ("Stavanger", ("Population: 130,754 (2014)", "Area: 71.35 km²",
                           "https://www.regionstavanger-ryfylke.com")),

        ]

        self.lblTown = QLabel(
            'Best Town to live in :) <b><br><span style="color:#00000000; font-size:24px">_</span></b>')
        self.lblTown.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lblTown, 0, 0, 1, len(self.towns))

        self.webLink = QLabel(self)
        self.webLink.setOpenExternalLinks(True)
        self.webLink.setText(self.urlLink)
        self.webLink.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.webLink, 2, 0, 1, len(self.towns))

        for pos, (town, (population, area, web)) in enumerate(self.towns):
            radiobutton = QRadioButton(town)
            radiobutton.town = town
            radiobutton.population = population
            radiobutton.area = area
            radiobutton.web = web
            radiobutton.setObjectName("rbtn"+town)
            radiobutton.toggled.connect(self.onClicked)
            layout.addWidget(radiobutton, 1, pos)
        # # Will set the last generated radiobutton to selected
        # radiobutton.setChecked(True)

        # Finding specific radiobutton by object name and setting checked state to True.
        self.capital = self.findChild(QRadioButton, "rbtnOslo")
        self.capital.setChecked(True)

        # # How it would look without loop trugh list.
        # radiobutton = QRadioButton("Oslo")
        # radiobutton.town = "Oslo"
        # radiobutton.population = "population info"
        # radiobutton.area = "area info"
        # radiobutton.web = "web site"
        # radiobutton.setObjectName("rbtnOslo")
        # radiobutton.toggled.connect(self.onClicked)
        # layout.addWidget(radiobutton, 1, 0)
        # # If setChecked line is abow the radiobutton.toggle.connect() , it will not trigger the onClicked at startup.
        # radiobutton.setChecked(True)

        btn_choose_town = QPushButton("I choose this town")
        btn_choose_town.clicked.connect(self.checking)
        layout.addWidget(btn_choose_town, 3, 0, 1, len(self.towns))

        self.le_choose_town = QLineEdit()
        self.le_choose_town.setPlaceholderText(
            "Type name and/or press enter to accept choice")
        self.le_choose_town.installEventFilter(self)
        layout.addWidget(self.le_choose_town, 4, 0, 1, len(self.towns))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            for town, (_) in self.towns:
                print("Le: ", self.le_choose_town.text())
                if self.le_choose_town.text() == town:
                    btn = self.findChild(QRadioButton, "rbtn" + town)
                    btn.setChecked(True)
                self.checking()

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.best_town = radioButton.town
            self.population = radioButton.population
            self.web = radioButton.web
            self.area = radioButton.area

            # self.webLink.setText(self.web)

            print(
                f"Info about {self.best_town}. {self.population}, {self.area}. Read more about {self.best_town} at {self.web}")
        self.urlLink = f"<a href={self.web}>Click this link to go to {self.best_town}</a>"
        self.webLink.setText(self.urlLink)

    def checking(self):
        color = "#00007F"
        info = "<br>"
        print("You have selected", self.best_town,
              "as the best town to live in")

        if self.best_town == "Bergen":
            self.best_town += "☔"

        if self.capital.isChecked():
            color = "#007F00"
            info = "<br>And the best of all, you have selected the capital 😍"
            self.best_town += "🏛"

        self.lblTown.setText(
            f'You have desided, the best town to live in is: <b><br><span style="color:{color}; font-size:24px">{self.best_town}</span></b>{info}')


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
