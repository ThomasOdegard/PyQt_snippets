import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        """Showing different ways to scale images/icons using QPixmap().scaled()
         and get current size 
        
        """

        self.setWindowTitle("PyQT show image")
        self.setGeometry(200, 200, 150, 150)
        layout = QGridLayout()
        self.setLayout(layout)

        self.lbl = QLabel()
        layout.addWidget(self.lbl, 1, 1)

        image = QPixmap("image.jpg")
        print(f"Original Height x Width: {image.height()}x{image.width()}")

        # self.lbl.setPixmap(image)

        # self.lbl.setPixmap(image.scaledToWidth(200))
        # print(self.lbl.pixmap().width())

        
        ## Image and scaling inline:
        # self.lbl.setPixmap(QPixmap("image.jpg").scaledToHeight(1080))
        # print(self.lbl.pixmap().size().height())

        # self.lbl.setPixmap(image.scaled(
        #     200, 1080, QtCore.Qt.KeepAspectRatio))

        # self.lbl.setPixmap(image.scaled(
        #     200, 1080, QtCore.Qt.IgnoreAspectRatio))

        self.lbl.setPixmap(QPixmap("image.jpg").scaled(
            200, 1080, QtCore.Qt.KeepAspectRatioByExpanding))

        print(self.lbl.pixmap().size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
