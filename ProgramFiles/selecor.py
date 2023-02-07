#GUI

#SELECT STATE
import config
import pandas as pd
import numpy as np
import datetime
import requests
import warnings
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import squarify
import plotly.offline as py
import plotly_express as px
import plotly.graph_objects as go
from IPython.display import Image
import jinja2
import seaborn as sns

warnings.filterwarnings('ignore')
def hi2():
    print("hi")
# age_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/AgeGroupDetails (1).csv')
# india_covid_19 = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india (1).csv')
# hospital_beds = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/HospitalBedsIndia.csv')
# individual_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/IndividualDetails.csv')
# ICMR_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/ICMRTestingDetails.csv')
# ICMR_labs = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/ICMRTestingLabs.csv')
# state_testing = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/StatewiseTestingDetails.csv')
# population = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_india_census2011.csv')
# world_population = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_by_country_2020.csv')
# confirmed_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_confirmed_global.csv')
# deaths_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_deaths_global.csv')
# recovered_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_recovered_global.csv')
# latest_data = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/04-04-2020.csv')
# age_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/AgeGroupDetails (1).csv')
# covid19India = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india (1).csv')
# covid19India['Date'] = pd.to_datetime(covid19India['Date'],dayfirst = True)
# ICMR_details['DateTime'] = pd.to_datetime(ICMR_details['DateTime'],dayfirst = True)
# ICMR_details = ICMR_details.dropna(subset=['TotalSamplesTested', 'TotalPositiveCases'])
# indiaCencus = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_india_census2011.csv')
# stateDetails = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/StatewiseTestingDetails.csv')
covid_df=pd.read_csv("C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india (1).csv")
# vaccine_df=pd.read_csv("C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_vaccine_statewise.csv")

age_details=config.age_details
india_covid_19=config.india_covid_19
hospital_beds=config.hospital_beds
individual_details=config.individual_details
ICMR_details=config.ICMR_details
ICMR_labs=config.ICMR_labs
state_testing=config.state_testing
population=config.population
world_population=config.world_population
confirmed_df=config.confirmed_df
deaths_df=config.deaths_df
recovered_df=config.recovered_df
latest_data=config.latest_data
age_details=config.age_details
covid19India=config.covid19India
ICMR_details=config.ICMR_details
indiaCencus=config.indiaCencus
stateDetails=config.stateDetails
# covid_df=config.covid_df
vaccine_df=config.vaccine_df

covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')
covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi3(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 481)
        Dialog.setStyleSheet("")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 430, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
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
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 170, 201, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 170, 201, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 360, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 71, 41))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 170, 71, 41))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 231, 41))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        #self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_4.setGeometry(QtCore.QRect(640, 30, 81, 31))
        #self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 281, 16))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(490, 80, 231, 31))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(490, 100, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(490, 70, 231, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(710, 80, 16, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(480, 80, 16, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_5.setText(_translate("Dialog", "EXIT"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.comboBox.setItemText(0, _translate("Dialog", "Andhra Pradesh"))
        self.comboBox.setItemText(1, _translate("Dialog", "Arunachal Pradesh"))
        self.comboBox.setItemText(2, _translate("Dialog", "Assam"))
        self.comboBox.setItemText(3, _translate("Dialog", "Bihar"))
        self.comboBox.setItemText(4, _translate("Dialog", "Chandigarh"))
        self.comboBox.setItemText(5, _translate("Dialog", "Chhattisgarh"))
        self.comboBox.setItemText(6, _translate("Dialog", "Goa"))
        self.comboBox.setItemText(7, _translate("Dialog", "Gujarat"))
        self.comboBox.setItemText(8, _translate("Dialog", "Haryana"))
        self.comboBox.setItemText(9, _translate("Dialog", "Himachal Pradesh"))
        self.comboBox.setItemText(10, _translate("Dialog", "Jammu & Kashmir"))
        self.comboBox.setItemText(11, _translate("Dialog", "Jharkhand"))
        self.comboBox.setItemText(12, _translate("Dialog", "Karnataka"))
        self.comboBox.setItemText(13, _translate("Dialog", "Kerala"))
        self.comboBox.setItemText(14, _translate("Dialog", "Ladakh"))
        self.comboBox.setItemText(15, _translate("Dialog", "Lakshadweep"))
        self.comboBox.setItemText(16, _translate("Dialog", "Madhya Pradesh"))
        self.comboBox.setItemText(17, _translate("Dialog", "Maharashtra"))
        self.comboBox.setItemText(18, _translate("Dialog", "Manipur"))
        self.comboBox.setItemText(19, _translate("Dialog", "Meghalaya"))
        self.comboBox.setItemText(20, _translate("Dialog", "Mizoram"))
        self.comboBox.setItemText(21, _translate("Dialog", "Nagaland"))
        self.comboBox.setItemText(22, _translate("Dialog", "Odisha"))
        self.comboBox.setItemText(23, _translate("Dialog", "Puducherry"))
        self.comboBox.setItemText(24, _translate("Dialog", "Punjab"))
        self.comboBox.setItemText(25, _translate("Dialog", "Rajasthan"))
        self.comboBox.setItemText(26, _translate("Dialog", "Sikkim"))
        self.comboBox.setItemText(27, _translate("Dialog", "Tamil Nadu"))
        self.comboBox.setItemText(28, _translate("Dialog", "Telangana"))
        self.comboBox.setItemText(29, _translate("Dialog", "Delhi"))
        self.comboBox.setItemText(30, _translate("Dialog", "Tripura"))
        self.comboBox.setItemText(31, _translate("Dialog", "Uttar Pradesh"))
        self.comboBox.setItemText(32, _translate("Dialog", "Uttarakhand"))
        self.comboBox.setItemText(33, _translate("Dialog", "West Bengal"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Andhra Pradesh"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Arunachal Pradesh"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Assam"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Bihar"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "Chandigarh"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "Chhattisgarh"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "Goa"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "Gujarat"))
        self.comboBox_3.setItemText(8, _translate("Dialog", "Haryana"))
        self.comboBox_3.setItemText(9, _translate("Dialog", "Himachal Pradesh"))
        self.comboBox_3.setItemText(10, _translate("Dialog", "Jammu & Kashmir"))
        self.comboBox_3.setItemText(11, _translate("Dialog", "Jharkhand"))
        self.comboBox_3.setItemText(12, _translate("Dialog", "Karnataka"))
        self.comboBox_3.setItemText(13, _translate("Dialog", "Kerala"))
        self.comboBox_3.setItemText(14, _translate("Dialog", "Ladakh"))
        self.comboBox_3.setItemText(15, _translate("Dialog", "Lakshadweep"))
        self.comboBox_3.setItemText(16, _translate("Dialog", "Madhya Pradesh"))
        self.comboBox_3.setItemText(17, _translate("Dialog", "Maharashtra"))
        self.comboBox_3.setItemText(18, _translate("Dialog", "Manipur"))
        self.comboBox_3.setItemText(19, _translate("Dialog", "Meghalaya"))
        self.comboBox_3.setItemText(20, _translate("Dialog", "Mizoram"))
        self.comboBox_3.setItemText(21, _translate("Dialog", "Nagaland"))
        self.comboBox_3.setItemText(22, _translate("Dialog", "Odisha"))
        self.comboBox_3.setItemText(23, _translate("Dialog", "Puducherry"))
        self.comboBox_3.setItemText(24, _translate("Dialog", "Punjab"))
        self.comboBox_3.setItemText(25, _translate("Dialog", "Rajasthan"))
        self.comboBox_3.setItemText(26, _translate("Dialog", "Sikkim"))
        self.comboBox_3.setItemText(27, _translate("Dialog", "Tamil Nadu"))
        self.comboBox_3.setItemText(28, _translate("Dialog", "Telangana"))
        self.comboBox_3.setItemText(29, _translate("Dialog", "Delhi"))
        self.comboBox_3.setItemText(30, _translate("Dialog", "Tripura"))
        self.comboBox_3.setItemText(31, _translate("Dialog", "Uttar Pradesh"))
        self.comboBox_3.setItemText(32, _translate("Dialog", "Uttarakhand"))
        self.comboBox_3.setItemText(33, _translate("Dialog", "West Bengal"))
        self.pushButton.setText(_translate("Dialog", "SUBMIT"))
        self.label_3.setText(_translate("Dialog", "STATE 1"))
        self.label_4.setText(_translate("Dialog", " STATE 2"))
        self.label_5.setText(_translate("Dialog", "COMPARING TWO STATES"))
        #self.pushButton_4.setText(_translate("Dialog", "BACK"))
        self.label_6.setText(_translate("Dialog", "Select Two different states for displaying Graph"))
        self.label_7.setText(_translate("Dialog", "NOTE:-DO NOT SELECT SAME STATES"))
        
        self.comboBox.activated.connect(self.clicked1)
        self.comboBox_3.activated.connect(self.clicked2)
        self.pushButton.clicked.connect(self.Compare_States)
        
    def clicked1(self):
        # finding the content of current item in combo box
        return self.comboBox.currentText()
        
    def clicked2(self):
        # finding the content of current item in combo box
        return self.comboBox_3.currentText()
    
    def Compare_States(self,SUBMIT):
        state1 = self.clicked1()
        state2 = self.clicked2()
        covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']
        statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"], index = "State/UnionTerritory", aggfunc = max)
        fig = plt.figure(figsize = (12, 6))
        ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin([state1, state2])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
        ax.set_title("States/UnionTerritories of India", size=16)
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi3(Dialog)
    Dialog.show()
    sys.exit(app.exec_())