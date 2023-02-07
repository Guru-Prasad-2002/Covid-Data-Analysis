import pandas as pd
import numpy as np
import datetime
import seaborn as sns
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
from IPython.display import display, Markdown
warnings.filterwarnings('ignore')
def hi():
    print("hi")
age_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/AgeGroupDetails (1).csv')
india_covid_19 = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india (1).csv')
hospital_beds = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/HospitalBedsIndia.csv')
individual_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/IndividualDetails.csv')
ICMR_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/ICMRTestingDetails.csv')
ICMR_labs = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/ICMRTestingLabs.csv')
state_testing = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/StatewiseTestingDetails.csv')
population = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_india_census2011.csv')
world_population = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_by_country_2020.csv')
confirmed_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/time_series_covid19_recovered_global.csv')
latest_data = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Secondary Datasets/04-04-2020.csv')
age_details = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/AgeGroupDetails (1).csv')
covid19India = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india (1).csv')
covid19India['Date'] = pd.to_datetime(covid19India['Date'],dayfirst = True)
ICMR_details['DateTime'] = pd.to_datetime(ICMR_details['DateTime'],dayfirst = True)
ICMR_details = ICMR_details.dropna(subset=['TotalSamplesTested', 'TotalPositiveCases'])
indiaCencus = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Covid19 India.org/population_india_census2011.csv')
stateDetails = pd.read_csv('C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/StatewiseTestingDetails.csv')



def Age_Wise_Bar_Graph():
    plt.figure(figsize=(14,8))
    sns.barplot(data=ageGroup,x='AgeGroup',y='TotalCases',color=sns.color_palette('Set3')[0])
    plt.title('Age Group Distribution')
    plt.xlabel('Age Group')
    plt.ylabel('Total Cases')
    for i in range(ageGroup.shape[0]):
        count = ageGroup.iloc[i]['TotalCases']
        plt.text(i,count+1,ageGroup.iloc[i]['Percentage'],ha='center')
    plt.show()
def Age_Wise_Pie_Chart():
    labels = list(age_details['AgeGroup'])
    sizes = list(age_details['TotalCases'])

    explode = []

    for i in labels:
        explode.append(0.05)
        
    plt.figure(figsize= (15,10))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=9, explode =explode)
    centre_circle = plt.Circle((0,0),0.70,fc='white')

    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('India - Age Group wise Distribution',fontsize = 20)
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()
def Gender_Wise_Include_Missing_Values():
    labels = ['Missing', 'Male', 'Female']
    sizes = []
    sizes.append(individual_details['gender'].isnull().sum())
    sizes.append(list(individual_details['gender'].value_counts())[0])
    sizes.append(list(individual_details['gender'].value_counts())[1])

    explode = (0, 0.1, 0)
    colors = ['#ffcc99','#66b3ff','#ff9999']

    plt.figure(figsize= (15,10))
    plt.title('Percentage of Gender',fontsize = 20)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def Gender_Wise_Ignore_Missing_Data():
    labels = ['Male', 'Female']
    sizes = []
    sizes.append(list(individual_details['gender'].value_counts())[0])
    sizes.append(list(individual_details['gender'].value_counts())[1])

    explode = (0.1, 0)
    colors = ['#66b3ff','#ff9999']

    plt.figure(figsize= (15,10))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)

    plt.title('Percentage of Gender (Ignoring the Missing Values)',fontsize = 20)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
def Compare_India():
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
    
def Compare_India_With_Major_Countries():
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
    print("Enter the 1st country")
    a=str(input())
    print("Enter the 2nd country")
    b=str(input())
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
#Gender_Wise_Ignore_Missing_Data()
#Gender_Wise_Include_Missing_Values()

#Compare_India_With_Major_Countries()
#Compare_India()
print("Success")