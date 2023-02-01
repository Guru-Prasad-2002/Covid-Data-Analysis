import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

covid_df = pd.read_csv('C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/covid_19_india (1).csv')
vaccine_df = pd.read_csv("C:/Users/Rohith S/Desktop/PBL Files/PBL Files/Primary Datasets/covid_vaccine_statewise.csv")
covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')
covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']

def Growth_trend_in_the_Central_region():
    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Madhya Pradesh','Uttar Pradesh','Chhattisgarh','Uttarakhand'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("Central India", size=16)
    plt.show()

def Growth_trend_in_the_northern_region():
    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Rajasthan','Delhi','Haryana','Chandigarh','Himachal Pradesh','Jammu and Kashmir','Ladakh'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("Northern India", size=16)
    plt.show()

def Growth_trend_in_the_western_region():

    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Goa','Gujarat','Dadra and Nagar Haveli and Daman and Diu'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("Western India", size=16)
    plt.show()

def Growth_trend_in_the_eastern_region():

    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Bihar','Jharkhand','Odisha','West Bengal','Andaman and Nicobar Islands'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("Eastern India", size=16)
    plt.show()

def Growth_trend_in_the_Southern_region():
    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Andhra Pradesh','Karnataka','Kerela','Tamil Nadu','Telengana','Puducherry','Lakshadweep'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("Southern India", size=16)
    plt.show()


def Growth_trend_in_the_north_eastern_region(): 
    fig = plt.figure(figsize = (12, 6))
    ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Arunachal Pradesh','Assam','Manipur','Meghalaya','Mizoram','Nagaland','Tripura','Sikkim'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
    ax.set_title("North-eastern states of India", size=16)
    plt.show()