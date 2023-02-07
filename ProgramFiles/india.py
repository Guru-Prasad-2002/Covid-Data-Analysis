#GUI

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from ProgramFiles.region_wise import *
from ProgramFiles.Samrudh import *

class Ui_Dialog4(object):
    def setupUi4(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 483)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 81, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 430, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 501, 321))
        self.groupBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 30, 201, 61))
        self.pushButton_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 100, 201, 61))
        self.pushButton_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 170, 201, 61))
        self.pushButton_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 250, 201, 61))
        self.pushButton_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 30, 201, 61))
        self.pushButton_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 110, 201, 61))
        self.pushButton_12.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(260, 10, 16, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 551, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 220, 181, 61))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(520, 160, 201, 21))
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(520, 180, 181, 21))
        self.label_5.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        
        self.pushButton_7.clicked.connect(self.central)
        self.pushButton_8.clicked.connect(self.north)
        self.pushButton_9.clicked.connect(self.west)
        self.pushButton_10.clicked.connect(self.east)
        self.pushButton_11.clicked.connect(self.south)
        self.pushButton_12.clicked.connect(self.northeast)
        self.pushButton_6.clicked.connect(quit)
        self.pushButton.clicked.connect(self.spike)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def spike(spike):
        Spike_in_Positive_Cases_India2()

    def central(central):
        Growth_trend_in_the_Central_region()
    def north(north):
        Growth_trend_in_the_northern_region()
    def west(west):
        Growth_trend_in_the_western_region()
    def east(east):
        Growth_trend_in_the_eastern_region()
    def south(south):
        Growth_trend_in_the_Southern_region()
    def northeast(northeast):
        Growth_trend_in_the_north_eastern_region()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.pushButton_6.setText(_translate("Dialog", "EXIT"))
        #self.pushButton_4.setText(_translate("Dialog", "BACK"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.groupBox.setTitle(_translate("Dialog", "REGION WISE STATES"))
        self.pushButton_7.setText(_translate("Dialog", "Central region"))
        self.pushButton_8.setText(_translate("Dialog", "Northern region"))
        self.pushButton_9.setText(_translate("Dialog", "Western region"))
        self.pushButton_10.setText(_translate("Dialog", "Eastern region"))
        self.pushButton_11.setText(_translate("Dialog", "Southern region"))
        self.pushButton_12.setText(_translate("Dialog", "North Eastern region"))
        self.label_3.setText(_translate("Dialog", "Select the Regions For Displaying the Graph of Growth trend in Confirmed cases in that Region."))
        self.pushButton.setText(_translate("Dialog", "POSITIVE CASES"))
        self.label_4.setText(_translate("Dialog", "To check spike in positive cases"))
        self.label_5.setText(_translate("Dialog", " in India,select Positive Cases"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi4(Dialog)
    Dialog.show()
    sys.exit(app.exec_())