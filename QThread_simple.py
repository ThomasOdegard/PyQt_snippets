from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time  # delay.

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0
        self.text = ""
        self.thread = MyThread()

        layout = QVBoxLayout()

        b1 = QPushButton("Start me")
        b1.pressed.connect(self.thread.start)
        b2 = QPushButton("Stop me")
        b2.pressed.connect(self.thread.stop)

        layout.addWidget(b1)
        layout.addWidget(b2)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()


class MyThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False

    def run(self):
        doNot = []
        while self.exiting == False:
            print("Im running....")
            time.sleep(0.01)

    def stop(self):
        # ! todo: Send heller melding til system tray at tilkoblingen er brutt.
        self.terminate()
        print("terminateing...")


app = QApplication([])
window = MainWindow()
app.exec_()
