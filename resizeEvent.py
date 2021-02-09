from PyQt5 import QtWidgets
import sys


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.current_width = 0
        self.current_height = 0
        # self.showMaximized()
        self.show()

    def resizeEvent(self, event):
        # Shows you the size of the widget without the frame.
        print(".width and .height: ", self.width(), "x", self.height())

        # Same as above.
        print(".geometry: ", self.geometry().width(),
              "x", self.geometry().height())

       # Shows you the size of the window including the frame and border.
        print(".frameGeometry: ", self.frameGeometry().width(),
              "x", self.frameGeometry().height())

        # Shows you the available geometry
        print(".availableGeometry: ", QtWidgets.QApplication.desktop().availableGeometry().width(),
              "x ", QtWidgets.QApplication.desktop().availableGeometry().height())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Window()
    sys.exit(app.exec_())
