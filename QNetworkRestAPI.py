from PyQt5.QtCore import Qt, QByteArray, QUrl
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply

import sys
import json


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.valueChanged.connect(self.doRequest)

        layout.addWidget(self.slider)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def doRequest(self):
        print(self.slider.value())

        data = QByteArray()

        data.append("'brightness':")
        data.append(str(self.slider.value()))

        #url = "https://httpbin.org/post"
        url = "https://postman-echo.com/post"
        req = QNetworkRequest(QUrl(url))
        req.setHeader(QNetworkRequest.ContentTypeHeader,
                      '"Content-Type": "application/json; charset=UTF-8"',)

        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.post(req, data)

    def handleResponse(self, reply):

        er = reply.error()
        if er == QNetworkReply.NoError:

            bytes_string = reply.readAll()
            json_array = json.loads(str(bytes_string, 'utf-8'))

            for key, value in json_array.items():
                print(key, value)

        else:
            print("Error occurred: ", er)
            print(reply.errorString())


app = QApplication([])
window = MainWindow()
app.exec_()
