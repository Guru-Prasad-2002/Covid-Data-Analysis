#MAIN GUI

import sys
sys.path.append('C:/Users/Rohith S/Desktop/PBL Files/PBL Files')
from ProgramFiles.Guru import * 
from ProgramFiles.Samrudh import * 
from ProgramFiles.Nakul import *
from ProgramFiles.VigneshWaran import *
from ProgramFiles.Gui2 import *
from ProgramFiles.Gui import *
from ProgramFiles.Gender import *
from ProgramFiles.Gui3 import *
from ProgramFiles.indiaselect import *
from ProgramFiles.india import *
from ProgramFiles.selecor import *
#Ui_Dialog()
#Age_Wise_Bar_Graph()
#Age_Wise_Pie_Chart()
#ICMR_Test_Labs_Per_States_Bar_Graph()
#Spike_in_Positive_Cases_India()
#Spike_in_Positive_Cases_India2()
#Mortality_Recovery_Rate()   (Runs is terminal)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog0(object):
        
    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog1()
        self.ui.setupUi1(self.window)
        self.window.show()
        #Dialog.hide()
        
    def openwindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog2()
        self.ui.setupUi2(self.window)
        self.window.show()
        #Dialog.hide()
        
    def openwindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog3()
        self.ui.setupUi3(self.window)
        self.window.show()
        #Dialog.hide()
        
    def openwindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog4()
        self.ui.setupUi4(self.window)
        self.window.show()
        #Dialog.hide()
        
    def openwindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog5()
        self.ui.setupUi5(self.window)
        self.window.show()
        #Dialog.hide()
        
    def openwindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog6()
        self.ui.setupUi6(self.window)
        self.window.show()
        #Dialog.hide()
        
    def setupUi0(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 482)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
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
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 80, 361, 391))
        self.groupBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 251, 61))
        self.pushButton.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 310, 251, 61))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 251, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 100, 251, 61))
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 170, 251, 61))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 430, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 130, 241, 51))
        self.pushButton_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 240, 251, 51))
        self.pushButton_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 100, 301, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 210, 301, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton.clicked.connect(self.openwindow3)
        self.pushButton_3.clicked.connect(self.openwindow)
        self.pushButton_4.clicked.connect(self.openwindow1)
        self.pushButton_6.clicked.connect(self.openwindow2)
        self.pushButton_2.clicked.connect(self.openwindow4)
        self.pushButton_5.clicked.connect(quit)
        self.pushButton_7.clicked.connect(self.openwindow5)
        self.pushButton_8.clicked.connect(self.comparecontries)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def comparecontries(comparecontries):
            Compare_India()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.groupBox.setTitle(_translate("Dialog", "SELECT INPUT"))
        self.pushButton.setText(_translate("Dialog", "INDIA"))
        self.pushButton_3.setText(_translate("Dialog", "AGE WISE ANALYSIS"))
        self.pushButton_2.setText(_translate("Dialog", "GENDER WISE ANALYSIS"))
        self.pushButton_6.setText(_translate("Dialog", "COMPARE TWO STATES"))
        self.pushButton_4.setText(_translate("Dialog", "STATE WISE ANALYSIS"))
        self.pushButton_5.setText(_translate("Dialog", "EXIT"))
        self.pushButton_7.setText(_translate("Dialog", "COMPARE TWO CONTRIES"))
        self.pushButton_8.setText(_translate("Dialog", "COMPARE INDIA WITH OTHER CONTRIES"))
        self.label_3.setText(_translate("Dialog", "IF YOU WANT TO COMPARE TWO MAJOR CONTRIES"))
        self.label_4.setText(_translate("Dialog", "IF YOU WANT TO COMPARE ALL THE CONTRIES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog0()
    ui.setupUi0(Dialog)
    Dialog.show()
    sys.exit(app.exec_())