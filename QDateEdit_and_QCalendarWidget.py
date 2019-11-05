from PyQt5.QtCore import QDate, pyqtSlot
from PyQt5.QtWidgets import *


class MainGUI(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        self.label_start = QLabel("Start date", self)
        self.label_start.setStyleSheet("background-color: yellow")
        self.dateed_start = QDateEdit(self)
        self.dateed_start.setDate(QDate(2019, 10, 5))
        # self.dateed_start.setDate(QDate.currentDate())
        self.dateed_start.setCalendarPopup(True)

        self.label_end = QLabel("End date", self)
        self.label_end.setStyleSheet("background-color: yellow")
        self.dateed_end = QDateEdit(self)
        # self.dateed_end.setDate(QDate(2017, 1, 3))
        self.dateed_end.setDate(QDate.currentDate())
        self.dateed_end.setCalendarPopup(True)

        self._btn_getdate = QPushButton("Get all dates", self)
        self._btn_clear = QPushButton("Clear", self)

        hbox1.addWidget(self.label_start)
        hbox1.addWidget(self.dateed_start)

        hbox1.addWidget(self.label_end)
        hbox1.addWidget(self.dateed_end)
        hbox1.addStretch()

        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        self.cal = QCalendarWidget(self)
        self.cal.setVerticalHeaderFormat(0)
        # print(self.cal.sizeHint())
        # self.cal.resize(self.cal.sizeHint())
        # self.cal.setFixedSize(200, 200)  # w, h
        self.cal.setFixedSize(self.cal.sizeHint())  # w, h
        hbox2.addWidget(self.cal)
        hbox2.addWidget(self._btn_getdate)
        hbox2.addWidget(self._btn_clear)
        vbox.addLayout(hbox2)

        self.qtxt = QTextEdit(self)
        vbox.addWidget(self.qtxt)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 650)


class MyMain(MainGUI):
    def __init__(self):
        super().__init__()

        self._btn_getdate.clicked.connect(self.__btn_getdate_clicked)
        self._btn_clear.clicked.connect(self.__btn_clear_clicked)
        self.cal.clicked.connect(self.__cal_clicked)
        self.cal.selectionChanged.connect(self.__cal_selectionchanged)

    @pyqtSlot()
    def __btn_getdate_clicked(self):
        self.__btn_clear_clicked()
        self.qtxt.append("\n========== QDateEdit - Start Date ===========")
        self.qtxt.append(str(self.dateed_start.date()))
        self.qtxt.append(self.dateed_start.date().toString())

        ddate = str(self.dateed_start.date().toPyDate())
        ddate_tmp = ddate.split("-")
        ddate2 = "".join(ddate_tmp)
        self.qtxt.append(ddate)
        self.qtxt.append(ddate2)

        self.qtxt.append("\n=========== QDateEdit - End Date ===========")
        # self.qtxt.append(str(self.dateed_end.date()))
        self.qtxt.append(self.dateed_end.date().toString())
        self.qtxt.append(str(self.dateed_end.date().toPyDate()))

        self.qtxt.append("\n========== QCalendarWidget ==============")

        date = self.cal.selectedDate()
        date = str(date.toPyDate())
        self.qtxt.append("Day = " + date.split("-")[2])
        self.qtxt.append("Month = " + str(self.cal.monthShown()))
        self.qtxt.append("Year = " + str(self.cal.yearShown()))

        self.qtxt.append("\n================= done ===============\n\n")

    @pyqtSlot()
    def __btn_clear_clicked(self):
        self.qtxt.setText("")

    @pyqtSlot(QDate)
    def __cal_clicked(self, ddate):
        # self.__btn_clear_clicked()
        self.qtxt.append("============ calendar clicked ==============")
        self.qtxt.append(ddate.toString())
        tmp_date = str(ddate.toPyDate())
        tmp2 = tmp_date.split("-")
        ddate2 = "".join(tmp2)
        self.qtxt.append(tmp_date)
        self.qtxt.append(ddate2)
        self.qtxt.append("Day = " + tmp2[2])
        self.qtxt.append("Month = " + str(self.cal.monthShown()))
        self.qtxt.append("Year = " + str(self.cal.yearShown()))
        self.cal.showToday()
        # self.qtxt.append("\n")
        self.qtxt.append("\n============== done ==================\n")

    @pyqtSlot()
    def __cal_selectionchanged(self):
        self.__btn_clear_clicked()
        self.qtxt.append("========= calendar selection changed ==========")
        ddate = self.cal.selectedDate()
        # print(ddate)
        self.qtxt.append(ddate.toString())
        self.qtxt.append(str(ddate.toPyDate()))
        # self.qtxt.append("\n")
        self.qtxt.append("\n=============== done =================\n")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myWindow = MyMain()

    myWindow.show()
    app.exec_()
