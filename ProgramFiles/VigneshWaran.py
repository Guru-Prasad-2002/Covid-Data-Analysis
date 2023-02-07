import config
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

# covid_df=pd.read_csv("C:/Users/guruj/Desktop/Covid_Data_Analysis/Primary Datasets/covid_19_india.csv")
# print(covid_df.head(5))

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
# icmrTestLabs=config.icmrTestLabs.copy()
vaccine_df=config.vaccine_df.copy()
covid_df=config.covid_df.copy()

print(id(covid_df))
print(id(config.covid_df))
print(covid_df.head(5))


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')
covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']

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