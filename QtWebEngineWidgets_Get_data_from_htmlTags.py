import sys
from PyQt5.QtCore import QUrl, QRegExp
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def callback_function(html):
    # print(html)
    rx = QRegExp()
    rx.setPattern(
        "(src=['|\"])([a-zA-Z|\d|//|/.|:|_|/-]+[.][a-zA-Z|//|/?|/=|\d|/-]+)(['|\"]>)")
    links = []

    pos = rx.indexIn(html, 0)

    while pos != -1:
        links.append(rx.cap(2))
        pos += rx.matchedLength()
        pos = rx.indexIn(html, pos)

    print(links)


def on_load_finished():
    web.page().runJavaScript(
        "document.getElementsByTagName('html')[0].innerHTML", callback_function)


app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://doc.qt.io/qtforpython/PySide2/QtCore/QRegExp.html"))
web.show()
web.loadFinished.connect(on_load_finished)

sys.exit(app.exec_())
