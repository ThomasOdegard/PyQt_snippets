import sys
from math import floor, ceil, sin, pi

from PyQt5.QtChart import QLineSeries, QChart, QChartView, QCategoryAxis
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)

        self.setWindowTitle("Rectifier")

        self.chartView = QChartView()
        self.chart = self.chartView.chart()
        self.series = QLineSeries()
        self.series2 = QLineSeries()
        self.series2.setColor(QColor('red'))

        # for i in range(-90, 90):  # rectifier
        #     x = i * pi / 50
        #     print('x', x)
        #     y = sin(x)
        #     print('y', abs(y))
        #     self.series.append(x, abs(y))

        x = [None] * 400
        for n in range(-200, 200):
            t = n/100
            if t >= -2 and t <= -1:
                x[n] = 0
            elif t >= -1 and t <= 1:
                x[n] = 1
            elif t >= 1 and t <= 2:
                x[n] = 0
            self.series2.append(t, x[n])

        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)

        self.chart.legend().hide()

        def format_axis(axis, min_value, max_value, step):
            for s in axis.categoriesLabels():
                axis.remove(s)
            axis.setStartValue(min_value)
            for i in range(ceil(min_value / step), floor(max_value / step) + 1):
                v = i * step
                axis.append('%s' % v, v)
            axis.setRange(min_value, max_value)
            grid_pen = QPen(QColor('silver'))
            grid_pen.setDashPattern([1, 1, 1, 1, 0, 0, 0, 0])
            #grid_pen.setDashPattern([1, 1, 0, 0])
            axis.setGridLinePen(grid_pen)

        self.chart.createDefaultAxes()

        self.chart.axisX().setRange(-5, 5)
        self.chart.axisX().setGridLineVisible(False)
        self.chartAxisX = QCategoryAxis(
            labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue, startValue=0.0)
        self.chart.setAxisX(self.chartAxisX)
        format_axis(self.chartAxisX, -5, 5, 1)

        self.chart.axisY().setRange(-0.1, 1.3)
        self.chartAxisY = QCategoryAxis(
            labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue, startValue=0.0)
        self.chart.setAxisY(self.chartAxisY)
        format_axis(self.chartAxisY, -0.1, 1.3, 1)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.chartView, 1, 1)
        self.chartView.show()
        self.setLayout(self.layout)


App = QApplication(sys.argv)
window = Widget()
window.show()
sys.exit(App.exec_())
