# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import sys


class Example(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):

        self.btnDockUndockAll = QPushButton("Release all")
        self.btnDockUndockAll.clicked.connect(self.DockUndockAll)
        self.layout.addWidget(self.btnDockUndockAll)
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.verticalSpacer)

        self.viewAndTableLayout = QHBoxLayout()

        self.dockView = QDockWidget("Dockable 1")
        self.grview = QGraphicsView(self.dockView)
        self.dockView.setWidget(self.grview)
        self.viewAndTableLayout.addWidget(self.dockView)

        self.dockTable = QDockWidget("Docalble 2")
        self.table = QTableView()
        self.dockTable.setWidget(self.table)
        self.viewAndTableLayout.addWidget(self.dockTable)
        self.layout.addLayout(self.viewAndTableLayout)

        self.listAndTreeLayout = QVBoxLayout()
        self.dockList = QDockWidget("Dockable 3")
        self.list = QListView()
        self.dockList.setWidget(self.list)
        self.listAndTreeLayout.addWidget(self.dockList)

        self.dockTree = QDockWidget("Dockable 4")
        self.btnDockUndock = QPushButton("Undock Me")
        self.btnDockUndock.clicked.connect(self.DockUndock)
        self.dockTree.setWidget(self.btnDockUndock)
        self.tree = QTreeView()
        self.listAndTreeLayout.addWidget(self.dockTree)
        self.layout.addLayout(self.listAndTreeLayout)

    def DockUndock(self):

        if self.dockTree.isFloating():
            self.btnDockUndock.setText("Release the beast again")
            self.dockTree.setFloating(False)

        else:

            self.btnDockUndock.setText("Dock back in")
            self.dockTree.setFloating(True)

    def DockUndockAll(self):

        if self.dockTree.isFloating() or self.dockView.isFloating() or self.dockList.isFloating() or self.dockTable.isFloating():
            self.dockTree.setFloating(False)
            self.dockView.setFloating(False)
            self.dockTable.setFloating(False)
            self.dockList.setFloating(False)
            self.btnDockUndockAll.setText("Release all")
            self.btnDockUndock.setText("Release the beast again")

        else:
            self.dockTree.setFloating(True)
            self.dockView.setFloating(True)
            self.dockTable.setFloating(True)
            self.dockList.setFloating(True)
            self.btnDockUndockAll.setText("Dock all back in")
            self.btnDockUndock.setText("Dock back in")


app = QApplication(sys.argv)
ex = Example()
ex.show()
ex.raise_()
sys.exit(app.exec_())
