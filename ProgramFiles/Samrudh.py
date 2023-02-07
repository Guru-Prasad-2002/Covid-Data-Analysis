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

warnings.filterwarnings('ignore')
def hi2():
    print("hi")

age_details=config.age_details.copy()
india_covid_19=config.india_covid_19.copy()
hospital_beds=config.hospital_beds.copy()
individual_details=config.individual_details.copy()
ICMR_details=config.ICMR_details.copy()
ICMR_labs=config.ICMR_labs.copy()
state_testing=config.state_testing.copy()
population=config.population.copy()
world_population=config.world_population.copy()
confirmed_df=config.confirmed_df.copy()
deaths_df=config.deaths_df.copy()
recovered_df=config.recovered_df.copy()
latest_data=config.latest_data.copy()
age_details=config.age_details.copy()
covid19India=config.covid19India.copy()
ICMR_details=config.ICMR_details.copy()
indiaCencus=config.indiaCencus.copy()
stateDetails=config.stateDetails.copy()
covid_df=config.covid_df.copy()
vaccine_df=config.vaccine_df.copy()

covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')
covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']

def Mortality_Recovery_Rate():
    statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"], index = "State/UnionTerritory", aggfunc = max)
    statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]
    statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]
    statewise = statewise.sort_values(by = "Confirmed", ascending = False)
    statewise.style.background_gradient(cmap = "cubehelix")
    print(statewise)

def Spike_in_Positive_Cases_India():
    dates = list(confirmed_df.columns[4:])
    dates = list(pd.to_datetime(dates))
    dates_india = dates[8:]
    df1 = confirmed_df.groupby('Country/Region').sum().reset_index()
    df2 = deaths_df.groupby('Country/Region').sum().reset_index()
    df3 = recovered_df.groupby('Country/Region').sum().reset_index()

    k = df1[df1['Country/Region']=='India'].loc[:,'1/30/20':]
    india_confirmed = k.values.tolist()[0] 

    k = df2[df2['Country/Region']=='India'].loc[:,'1/30/20':]
    india_deaths = k.values.tolist()[0] 

    k = df3[df3['Country/Region']=='India'].loc[:,'1/30/20':]
    india_recovered = k.values.tolist()[0] 

    plt.figure(figsize= (15,10))
    plt.xticks(rotation = 90 ,fontsize = 11)
    plt.yticks(fontsize = 10)
    plt.xlabel("Dates",fontsize = 20)
    plt.ylabel('Total cases',fontsize = 20)
    plt.title("Total Confirmed, Active, Death in India" , fontsize = 20)

    ax1 = plt.plot_date(y= india_confirmed,x= dates_india,label = 'Confirmed',linestyle ='-',color = 'b')
    ax2 = plt.plot_date(y= india_recovered,x= dates_india,label = 'Recovered',linestyle ='-',color = 'g')
    ax3 = plt.plot_date(y= india_deaths,x= dates_india,label = 'Death',linestyle ='-',color = 'r')
    plt.legend()
    plt.show()
def Spike_in_Positive_Cases_India2():
    covid19India['Date'] = pd.to_datetime(covid19India['Date'],dayfirst=True)
    df1=covid19India.groupby('Date').sum()
    df1.reset_index(inplace=True)
    plt.figure(figsize= (14,8))
    plt.xticks(rotation = 90 ,fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.xlabel("Dates",fontsize = 20)
    plt.ylabel('Total cases',fontsize = 20)
    plt.title("Total Confirmed, Active, Death in India" , fontsize = 20)

    ax1 = plt.plot_date(data=df1,y= 'Confirmed',x= 'Date',label = 'Confirmed',linestyle ='-',color = 'b')
    ax2 = plt.plot_date(data=df1,y= 'Cured',x= 'Date',label = 'Cured',linestyle ='-',color = 'g')
    ax3 = plt.plot_date(data=df1,y= 'Deaths',x= 'Date',label = 'Death',linestyle ='-',color = 'r')
    plt.legend()
    plt.show()