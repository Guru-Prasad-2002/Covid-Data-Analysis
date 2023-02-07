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
covid_df=config.covid_df
vaccine_df=config.vaccine_df

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