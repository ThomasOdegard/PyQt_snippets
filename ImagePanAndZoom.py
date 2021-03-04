import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class PhotoViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._image = QtWidgets.QGraphicsPixmapItem()
        self._scene = QtWidgets.QGraphicsScene(self)
        self._scene.addItem(self._image)
        self._empty = True
        self._zoom = 0
        self.setScene(self._scene)

        # Center of zoom placed where mouse pinter is.
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        # hide scrollbars
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitImageToView(self):
        rect = QtCore.QRectF(self._image.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._image.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._image.setPixmap(QtGui.QPixmap())
        self.fitImageToView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                zoom_factor = 1.25
                self._zoom += 1
            else:
                zoom_factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(zoom_factor, zoom_factor)
            elif self._zoom == 0:
                self.fitImageToView()
            else:
                self._zoom = 0

    def zoomImage(self, zoom_level):
        if self.hasPhoto():
            if zoom_level == "in":
                factor = 1.25
                self._zoom += 1
            elif zoom_level == 'out':
                factor = 0.8
                self._zoom -= 1
            self.scale(factor, factor)

    def toggleDragMode(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._image.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.viewer = PhotoViewer(self)
        # 'Load image' button
        self.btnLoad = QtWidgets.QPushButton(self)
        self.btnLoad.setText('Load image')
        self.btnLoad.clicked.connect(self.loadImage)
        self.btnZoomIn = QtWidgets.QPushButton(self)
        self.btnZoomIn.setText('Zoom in')
        self.btnZoomIn.clicked.connect(lambda: self.viewer.zoomImage("in"))
        self.btnZoomOut = QtWidgets.QPushButton(self)
        self.btnZoomOut.setText('Zoom out')
        self.btnZoomOut.clicked.connect(lambda: self.viewer.zoomImage("out"))

        HBlayout = QtWidgets.QHBoxLayout(self)
        VBlayout = QtWidgets.QVBoxLayout(self)

        HBlayout.addWidget(self.viewer)
        VBlayout.addWidget(self.btnLoad)
        VBlayout.addWidget(self.btnZoomIn)
        VBlayout.addWidget(self.btnZoomOut)
        self.verticalSpacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        VBlayout.addItem(self.verticalSpacer)
        HBlayout.addLayout(VBlayout)

    def loadImage(self):
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(imagePath)
        self.viewer.setPhoto(pixmap)
        # self.viewer.setPhoto(QtGui.QPixmap('image.jpg'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 600)
    window.show()
    sys.exit(app.exec_())
