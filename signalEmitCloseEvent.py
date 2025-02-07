import sys

from PyQt5 import QtCore, QtWidgets


class SubWindow(QtWidgets.QWidget):
    # This is the sub window's signal
    submitAndCloseEvent = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.line_edit = QtWidgets.QLineEdit(
            placeholderText="Enter data you like to submit here")
        # self.btn = QtWidgets.QPushButton("Submit")
        layout.addWidget(self.line_edit)
        # layout.addWidget(self.btn)
        # self.btn.clicked.connect(self.confirm)

    # def confirm(self):
    #     self.submitAndCloseEvent.emit(self.line_edit.text())
    #     self.close()

    def closeEvent(self, event):
        self.submitAndCloseEvent.emit(self.line_edit.text())


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sub_window = None  # placeholder attribute for the sub window
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.label = QtWidgets.QLabel("Data from second window")
        self.btn = QtWidgets.QPushButton("Open second window")
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.show_sub_window)

    # <-- Here, we create *and connect* the sub window's signal to the main window's slot
    def show_sub_window(self):
        self.sub_window = SubWindow()
        self.sub_window.submitAndCloseEvent.connect(
            self.on_sub_window_submitAndClose)
        self.sub_window.show()

    # main window's slot
    def on_sub_window_submitAndClose(self, rec_data):
        self.label.setText(f"Current data received: {rec_data}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
