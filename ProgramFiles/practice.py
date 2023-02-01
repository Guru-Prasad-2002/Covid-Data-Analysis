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

def Most_Active_cases_in_the_states_of_India(): 

    states_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()
    fig = plt.figure(figsize = (16, 9))
    plt.title('Top 5 states with most active cases in India', size = 25)
    ax = sns.barplot(data = states_active_cases.iloc[:5], x = "Active_Cases", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'red')
    plt.xlabel("Total active cases")
    plt.ylabel("States")
    plt.show()

def Most_Deaths_in_the_states_of_India(): 

    states_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths', 'Date']].sort_values(by = ['Deaths'], ascending = False).reset_index()
    fig = plt.figure(figsize = (18, 5))
    plt.title('Top 5 states with the most deaths', size = 25)
    ax = sns.barplot(data = states_deaths.iloc[:5], x = "Deaths", y = "State/UnionTerritory", linewidth = 2, edgecolor = 'black')
    plt.ylabel("Total death cases")
    plt.ylabel("States")
    plt.show()