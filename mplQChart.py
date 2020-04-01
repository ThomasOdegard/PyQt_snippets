import sys

from PyQt5 import QtCore, QtGui, uic, QtWidgets, QtChart
#from functools import partial
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


class Main(QtWidgets.QMainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        uic.loadUi("mplQChart_window.ui", self)

        # - Init buttons.
        self.btn_plot_mpl.clicked.connect(self.changefig)
        self.btn_remove_mpl.clicked.connect(self.stop)
        self.btn_exit_mpl.clicked.connect(sys.exit)

        self.btn_plot_qchart.clicked.connect(self.add_graph)
        self.btn_remove_qchart.clicked.connect(self.stop)
        self.btn_exit_qchart.clicked.connect(sys.exit)

        # Add Matplotlib figure to first tab.
        fig = Figure()
        self.addmpl(fig)
        self.changefig()

        # Add QChart to second tab.
        self.chartview = QtChart.QChartView()
        self.Qchartvl.addWidget(self.chartview)
        self.add_graph()

    def stop(self):
        print("stop graph")


# ---------------------------- Matplotlib TAB 1---------------------------------------------


    def changefig(self):
        self.rmmpl()
        fig1 = Figure()
        ax1f1 = fig1.add_subplot(111)
        ax1f1.plot(np.random.rand(5))
        self.addmpl(fig1)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()

    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()


# ------------------------QChart - TAB 2 --------------------------------------------


    def add_graph(self):
        series = QtChart.QLineSeries()

        for i in range(10):
            series << QtCore.QPointF(i, np.random.uniform(0, 10))

        chart = QtChart.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        axisX = QtChart.QValueAxis()
        chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QtChart.QValueAxis()
        chart.addAxis(axisY, QtCore.Qt.AlignLeft)
        series.attachAxis(axisY)

        self.chartview.setChart(chart)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())
