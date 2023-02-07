#GUI

import config
import sys
sys.path.append('C:/Users/Rohith S/Desktop/PBL Files/PBL Files')
from ProgramFiles.Guru import *
from PyQt5 import QtCore, QtGui, QtWidgets


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


class Ui_Dialog6(object):
    def setupUi6(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 481)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 430, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        #self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        #self.pushButton_4.setGeometry(QtCore.QRect(640, 30, 81, 31))
        #self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(490, 80, 231, 31))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(710, 80, 16, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 170, 91, 41))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 360, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(480, 80, 16, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 81, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(490, 70, 231, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 261, 41))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(490, 100, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 170, 201, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 430, 361, 31))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.pushButton_5.clicked.connect(quit)
        self.pushButton.clicked.connect(self.Compare_India_With_Major_Countries)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_5.setText(_translate("Dialog", "EXIT"))
        #self.pushButton_4.setText(_translate("Dialog", "BACK"))
        self.label_7.setText(_translate("Dialog", "NOTE:-DO NOT SELECT SAME CONTRY"))
        self.label_4.setText(_translate("Dialog", "CONTRY2:-"))
        self.pushButton.setText(_translate("Dialog", "SUBMIT"))
        self.label_2.setText(_translate("Dialog", "Using python"))
        self.label_3.setText(_translate("Dialog", "CONTRY1:-"))
        self.comboBox.setItemText(0, _translate("Dialog", "Russia"))
        self.comboBox.setItemText(1, _translate("Dialog", "US"))
        self.comboBox.setItemText(2, _translate("Dialog", "Italy"))
        self.comboBox.setItemText(3, _translate("Dialog", "Spain"))
        self.comboBox.setItemText(4, _translate("Dialog", "France"))
        self.comboBox.setItemText(5, _translate("Dialog", "India"))
        self.comboBox.setItemText(6, _translate("Dialog", "China"))
        self.label_5.setText(_translate("Dialog", "COMPARING TWO CONTRIES"))
        self.label.setText(_translate("Dialog", "COVID-19 ANALYSIS"))
        self.label_6.setText(_translate("Dialog", "Select Two different CONTRIES for displaying Graph"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Russia"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "US"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Italy"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Spain"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "France"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "India"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "China"))
        self.label_8.setText(_translate("Dialog", "NOTE:- ONLY FEW CONTRIES(MAJOR CONTRIES) HAVE BEEN DISPLAYED"))

    def clickedcountry1(self):
        # finding the content of current item in combo box
        return self.comboBox.currentText()
        
    def clickedcountry2(self):
        # finding the content of current item in combo box
        return self.comboBox_2.currentText()
 
    def Compare_India_With_Major_Countries(self, SUBMIT):
        countries = ['Russia','US', 'Italy', 'Spain', 'France','India','China']
        dates = list(confirmed_df.columns[4:])
        dates = list(pd.to_datetime(dates))
        dates_india = dates[8:]
        df1 = confirmed_df.groupby('Country/Region').sum().reset_index()
        df2 = deaths_df.groupby('Country/Region').sum().reset_index()
        df3 = recovered_df.groupby('Country/Region').sum().reset_index()
        global_confirmed = []
        global_recovered = []
        global_deaths = []
        global_active = []
        
        a = self.clickedcountry1()
        b = self.clickedcountry2()

        countries=[a,b]
        for country in countries:
                k =df1[df1['Country/Region'] == country].loc[:,'1/30/20':]
                global_confirmed.append(k.values.tolist()[0]) 

                k =df2[df2['Country/Region'] == country].loc[:,'1/30/20':]
                global_deaths.append(k.values.tolist()[0]) 

                k =df3[df3['Country/Region'] == country].loc[:,'1/30/20':]
                global_deaths.append(k.values.tolist()[0])  

        plt.figure(figsize= (15,10))
        plt.xticks(rotation = 90 ,fontsize = 11)
        plt.yticks(fontsize = 10)
        plt.xlabel("Dates",fontsize = 20)
        plt.ylabel('Total cases',fontsize = 20)
        plt.title("Comparison with other Countries" , fontsize = 20)

        for i in range(len(countries)):
                plt.plot_date(y= global_confirmed[i],x= dates_india,label = countries[i],linestyle ='-')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi6(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
