import pandas as pd                           

import numpy as np                             

import matplotlib.pyplot as plt     

import seaborn as sns                          

import plotly.express as px

import jinja2

from plotly.subplots import make_subplots

from datetime import datetime

pd.set_option("display.max_rows", 1000)      # to display all rows and columns 
pd.set_option("display.max_columns", 1000)

covid_df=pd.read_csv("C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india.csv")
vaccine_df=pd.read_csv("C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_vaccine_statewise.csv")

# covid_df = pd.read_csv("C:/Users/Rohith S/Desktop/PBL Files/PBL Files/testfolder/covid_19_india (1).csv")

# print(covid_df.head(10))
# covid_df.info()             #ran without print
# print(covid_df.describe())

# vaccine_df = pd.read_csv("C:/Users/Rohith S/Desktop/PBL Files/PBL Files/testfolder/covid_vaccine_statewise.csv")

# print(vaccine_df.head(7))

#Data cleaning from below 

covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)

#print(covid_df.head())  #returns 5 by default if no value is specified to head

# covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')
# print(covid_df.head())

# **Active cases**

covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']
# print(covid_df.tail())

# statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"], index = "State/UnionTerritory", aggfunc = max)

# statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]

# statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]

# statewise = statewise.sort_values(by = "Confirmed", ascending = False)

# statewise.style.background_gradient(cmap = "cubehelix")
# print(statewise)

# **Most Active cases in the states of India** 

def states_with_most_active_cases():

    states_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()
    fig = plt.figure(figsize = (16, 9))
    plt.title('Top 5 states with most active cases in India', size = 25)
    ax = sns.barplot(data = states_active_cases.iloc[:5], x = "Active_Cases", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'red')
    plt.xlabel("Total active cases")
    plt.ylabel("States")
    plt.show()

def states_with_least_active_cases():
    states_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()
    fig = plt.figure(figsize = (16, 9))
    plt.title('states with least active cases in India', size = 25)
    ax = sns.barplot(data = states_active_cases.iloc[31:36], x = "Active_Cases", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'red')
    plt.xlabel("Total active cases")
    plt.ylabel("States")
    plt.show()

# **Most Deaths in the states of India** 

def states_with_most_deaths():

    states_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths', 'Date']].sort_values(by = ['Deaths'], ascending = False).reset_index()
    fig = plt.figure(figsize = (18, 5))
    plt.title('Top 5 states with the most deaths', size = 25)
    ax = sns.barplot(data = states_deaths.iloc[:5], x = "Deaths", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'black')
    plt.ylabel("Total death cases")
    plt.ylabel("States")
    plt.show()

def states_with_least_deaths():

    states_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths', 'Date']].sort_values(by = ['Deaths'], ascending = False).reset_index()
    fig = plt.figure(figsize = (18, 5))
    plt.title('States with the least deaths', size = 25)
    ax = sns.barplot(data = states_deaths.iloc[31:36], x = "Deaths", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'black')
    plt.ylabel("Total death cases")
    plt.ylabel("States")
    plt.show()


# **Growth trend** 

# *Growth trend for any two states*

# state1 = input('Enter State/UnionTerritory 1: ')
# state2 = input('Enter State:UnionTerritory 2: ')
# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin([state1, state2])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("States/UnionTerritories of India", size=16)
# plt.show()

# Growth trend in the north-eastern region 

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Arunachal Pradesh','Assam','Manipur','Meghalaya','Mizoram','Nagaland','Tripura','Sikkim'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("North-eastern states of India", size=16)
# plt.show()

# Growth trend in the Southern region

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Andhra Pradesh','Karnataka','Kerela','Tamil Nadu','Telengana','Puducherry','Lakshadweep'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("Southern India", size=16)
# plt.show()

# Growth trend in the Central region

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Madhya Pradesh','Uttar Pradesh','Chhattisgarh','Uttarakhand'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("Central India", size=16)
# plt.show()

# Growth trend in the northern region

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Rajasthan','Delhi','Haryana','Chandigarh','Himachal Pradesh','Jammu and Kashmir','Ladakh'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("Northern India", size=16)
# plt.show()

# Growth trend in the western region

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Goa','Gujarat','Dadra and Nagar Haveli and Daman and Diu'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("Western India", size=16)
# plt.show()

# Growth trend in the eastern region

# fig = plt.figure(figsize = (12, 6))
# ax = sns.lineplot(data = covid_df[covid_df['State/UnionTerritory'].isin(['Bihar','Jharkhand','Odisha','West Bengal','Andaman and Nicobar Islands'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
# ax.set_title("Eastern India", size=16)
# plt.show()

# **Vaccine data set from below** 

# print(vaccine_df.head())

vaccine_df.rename(columns = {'Updated On' : 'Vaccine_Date'}, inplace = True)
# print(vaccine_df.head(10))

# vaccine_df.info()

# print(vaccine_df.isnull().sum()) # calculates sum of all the missing values for each column

vaccination = vaccine_df.drop(columns = ['Sputnik V (Doses Administered)', 'AEFI', '18-44 Years (Doses Administered)', '45-60 Years (Doses Administered)', '60+ Years (Doses Administered)'], axis = 1)
# print(vaccination.head())


# **Remove rows where state is India** 

vaccine = vaccine_df[vaccine_df.State!= 'India'] # only taking rows where state is not equal to india
# print(vaccine)

vaccine.rename(columns = {"Total Individuals Vaccinated": "Total"}, inplace = True)
# print(vaccine.head())

# **Vaccination in the states of India**

# max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
# max_vac = max_vac.sort_values('Total', ascending = False)[:36]
# print(max_vac)

def vaccination_for_top5_states():
    max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
    max_vac = max_vac.sort_values('Total', ascending = False)[0:5]
    fig = plt.figure(figsize = (10,5))
    plt.title("States with the most vaccination", size = 20)
    y = sns.barplot (data = max_vac.iloc[:10],x= max_vac. Total, y= max_vac.index, linewidth=2, edgecolor = 'black')
    plt.xlabel ("Vaccination")
    plt.ylabel("States")
    plt.show()

def vaccination_for_bottom5_states():
    max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
    max_vac = max_vac.sort_values('Total', ascending = False)[31:36]
    fig = plt.figure(figsize = (10,5))
    plt.title("States with the least vaccination", size = 20)
    y = sns.barplot (data = max_vac.iloc[:10],x= max_vac. Total, y= max_vac.index, linewidth=2, edgecolor = 'black')
    plt.xlabel ("Vaccination")
    plt.ylabel("States")
    plt.show()


#states_with_most_deaths()
#states_with_least_deaths()
#states_with_most_active_cases()
#states_with_least_active_cases()
#vaccination_for_top5_states()
#vaccination_for_bottom5_states()

