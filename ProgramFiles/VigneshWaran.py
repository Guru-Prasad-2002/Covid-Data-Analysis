import pandas as pd
import numpy as np
import datetime
import requests
import warnings
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import squarify
import plotly.offline as py
import plotly_express as px
import plotly.graph_objects as go
from IPython.display import Image
warnings.filterwarnings('ignore')
def hi():
    print("hi")
age_details = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/AgeGroupDetails (1).csv')
india_covid_19 = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/covid_19_india (1).csv')
hospital_beds = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/HospitalBedsIndia.csv')
individual_details = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/IndividualDetails.csv')
ICMR_details = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/ICMRTestingDetails.csv')
ICMR_labs = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/ICMRTestingLabs.csv')
state_testing = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/StatewiseTestingDetails.csv')
population = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/population_india_census2011.csv')
world_population = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/population_by_country_2020.csv')
confirmed_df = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Secondary Datasets/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Secondary Datasets/time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Secondary Datasets/time_series_covid19_recovered_global.csv')
latest_data = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Secondary Datasets/04-04-2020.csv')
india_covid_19['Date'] = pd.to_datetime(india_covid_19['Date'],dayfirst = True)
ICMR_details['DateTime'] = pd.to_datetime(ICMR_details['DateTime'],dayfirst = True)
ICMR_details = ICMR_details.dropna(subset=['TotalSamplesTested', 'TotalPositiveCases'])
ageGroup = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/AgeGroupDetails (1).csv')
covid19India = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/covid_19_india (1).csv')
hospitalBeds = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/HospitalBedsIndia.csv')
icmrTestLabs = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/ICMRTestingLabs.csv')
indiDetails = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/IndividualDetails.csv')
indiaCencus = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Covid19 India.org/population_india_census2011.csv')
stateDetails = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/StatewiseTestingDetails.csv')

def ICMR_Test_Labs_Per_States_Bar_Graph():
    state=list(icmrTestLabs['state'].value_counts().index)
    count=list(icmrTestLabs['state'].value_counts())
    plt.figure(figsize=(14,8))
    sns.barplot(x=count,y=state,color=sns.color_palette('Set3')[10])
    plt.xlabel('Counts')
    plt.ylabel('States')
    plt.title('ICMR Test labs per States')
    plt.tight_layout()
    plt.show()