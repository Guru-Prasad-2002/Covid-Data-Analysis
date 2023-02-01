#GUI

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("C:/Users/Rohith S/Desktop/PBL Files/PBL Files")
from ProgramFiles.Guru import *

class Ui_Dialog5(object):
    def setupUi5(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 485)
        Dialog.setStyleSheet("")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 81, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 201, 61))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 220, 201, 61))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_3.setGeometry(QtCore.QRect(40, 300, 201, 61))
        #self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        #self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 371, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 371, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        #self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_4.setGeometry(QtCore.QRect(630, 30, 81, 31))
        #self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_5.setGeometry(QtCore.QRect(40, 380, 201, 61))
        #self.pushButton_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        #self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 430, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.gender1)
        self.pushButton_2.clicked.connect(self.gender2)
        self.pushButton_6.clicked.connect(quit)
        
    def gender1(gender1):
        Gender_Wise_Ignore_Missing_Data()
        
    def gender2(gender2):
        Gender_Wise_Include_Missing_Values()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.pushButton.setText(_translate("Dialog", "PIE CHART"))
        self.pushButton_2.setText(_translate("Dialog", "PIE CHART"))
        #self.pushButton_3.setText(_translate("Dialog", "ANY OTHER***"))
        self.label_3.setText(_translate("Dialog", "To See Pie Chart on CONFIRMED CASES Select, PIE CHART"))
        self.label_4.setText(_translate("Dialog", "To See Pie Chart on CONFIRMED CASES, PIE CHART"))
        #self.pushButton_4.setText(_translate("Dialog", "BACK"))
        #self.pushButton_5.setText(_translate("Dialog", "ANY OTHER***"))
        self.pushButton_6.setText(_translate("Dialog", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi5(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
