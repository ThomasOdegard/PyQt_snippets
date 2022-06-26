import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton
from time import sleep
from picamera import PiCamera


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle('Save Image capture')

        layout = QVBoxLayout()
        self.setLayout(layout)

        snap_btn = QPushButton('Snap image')
        snap_btn.clicked.connect(self.saveFile)
        layout.addWidget(snap_btn)

        self.show()

    def saveFile(self):
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save Image as:", "image", "Jpeg Files (*.jpeg)", options=options)
        if fileName:
            # Todo: Find better way to close/save file if crash (ea. stream to QImage?).
            # This is how the picamera documentation does it.
            # Explicitly open a new file
            image_file = open(fileName, 'wb')
            camera = PiCamera()
            camera.start_preview()
            sleep(2)  # Let the camera boot up and fetch preview.
            camera.capture(image_file)
            # image_file.flush() has been called, but we need to close the file.
            image_file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
