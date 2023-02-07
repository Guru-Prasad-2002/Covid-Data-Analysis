#GUI
#STATE

import sys
import os
sys.path.append('C:/Users/guruj/Desktop/Covid_Data_Analysis')
from ProgramFiles.VigneshWaran import *
from ProgramFiles.Gender import*
from ProgramFiles.india import *
from ProgramFiles.Gui import *
from ProgramFiles.region_wise import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ProgramFiles.Gui import *
from ProgramFiles.covidtest import *

class Ui_Dialog2(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 481)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 31, 81, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 110, 201, 61))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        #self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_4.setGeometry(QtCore.QRect(630, 31, 81, 31))
        #self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 451, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 1, 301, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 61, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 430, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 721, 241))
        self.groupBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 221, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 201, 61))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 140, 201, 61))
        self.pushButton_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.label_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 191, 20))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 20, 231, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 201, 61))
        self.pushButton_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 140, 201, 61))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.label_6.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 191, 20))
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(480, 20, 231, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 70, 201, 61))
        self.pushButton_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 140, 201, 61))
        self.pushButton_9.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.label_8.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 211, 20))
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        
        self.pushButton.clicked.connect(self.bar1)
        self.pushButton_2.clicked.connect(self.mdeath)
        self.pushButton_7.clicked.connect(self.ldeath)
        self.pushButton_5.clicked.connect(self.mactive)
        self.pushButton_3.clicked.connect(self.lactive)
        self.pushButton_8.clicked.connect(self.mvaccination)
        self.pushButton_9.clicked.connect(self.lvaccination)
        self.pushButton_6.clicked.connect(quit)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def bar1(bar1):
        ICMR_Test_Labs_Per_States_Bar_Graph()
        
    def mdeath(mdeath):
        states_with_most_deaths()
        
    def ldeath(ldeath):
        states_with_least_deaths()
        
    def mactive(mactive):
        states_with_most_active_cases()
        
    def lactive(lactive):
        states_with_least_active_cases()
        
    def mvaccination(mvaccination):
        vaccination_for_top5_states()
        
    def lvaccination(lvaccination):
        vaccination_for_bottom5_states()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.pushButton.setText(_translate("Dialog", "BAR GRAPH"))
        #self.pushButton_4.setText(_translate("Dialog", "BACK"))
        self.label_3.setText(_translate("Dialog", "To See Bar Graph on ICMR Test Labs Per States BarGraph Select, BAR GRAPH"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.pushButton_6.setText(_translate("Dialog", "EXIT"))
        self.groupBox.setTitle(_translate("Dialog", "STATE WISE ANALYSIS"))
        self.groupBox_2.setTitle(_translate("Dialog", "DEATHS DUE TO COVID"))
        self.pushButton_2.setText(_translate("Dialog", "MOST DEATH"))#2 mdeath
        self.pushButton_7.setText(_translate("Dialog", "LEAST DEATH"))#7 ldeath
        self.label_4.setText(_translate("Dialog", "SHOWS STATS OF TOP 5 STATES WITH"))
        self.label_5.setText(_translate("Dialog", "MOST DEATH AND LEAST DEATH"))
        self.groupBox_3.setTitle(_translate("Dialog", "ACTIVE COVID CASES"))
        self.pushButton_5.setText(_translate("Dialog", "MOST ACTIVE CASES"))#5 mactive
        self.pushButton_3.setText(_translate("Dialog", "LEAST ACTIVE CASES"))#3 lactive
        self.label_6.setText(_translate("Dialog", "SHOWS STATS OF TOP 5 STATES WITH MOST"))
        self.label_7.setText(_translate("Dialog", "CASES AND LEAST ACTIVE CASES"))
        self.groupBox_4.setTitle(_translate("Dialog", "VACCINATION"))
        self.pushButton_8.setText(_translate("Dialog", "TOP 5 STATES"))
        self.pushButton_9.setText(_translate("Dialog", "BOTTOM 5 STATES"))
        self.label_8.setText(_translate("Dialog", "SHOWS STATS OF TOP 5 STATES WITH MOST"))
        self.label_9.setText(_translate("Dialog", "VACCINATION AND LEAST VACCINATION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())