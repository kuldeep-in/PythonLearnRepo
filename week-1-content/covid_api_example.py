"""
A short example of the Numpy, Pandas and Matplotlib libraries in Python.
------------------------------------------------------------------------

Fetches, manipulates and plots the historic COVID-19 data for the UK from the UK Government's open-source API.

Author: Ethan Jones :)

References:
- https://github.com/ejones18/uk_covid_case_visualisation
"""

import math
import datetime

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from uk_covid19 import Cov19API

all_nations = [
    "areaType=nation"
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
}

api_request = Cov19API( #Create API request for COVID UK data.
    filters=all_nations,
    structure=cases_and_deaths
)

covid_df = api_request.get_dataframe()
covid_df["date"] = covid_df["date"].apply(lambda x : datetime.datetime.strptime(x, "%Y-%m-%d")) #Convert dates in date column to datetime objects not strings.

english_data = covid_df.loc[covid_df["areaName"] == "England"] # Split data into date for England and Wales.
welsh_data = covid_df.loc[covid_df["areaName"] == "Wales"]

max_english_cases_a_day = english_data["newCasesByPublishDate"].max() #Find max cases in a day for both countries.
max_welsh_cases_a_day = welsh_data["newCasesByPublishDate"].max()

print(f">> Max cases in a day for England: {max_english_cases_a_day}")
print(f">> Max cases in a day for Wales: {max_welsh_cases_a_day}")

english_data_2022 = english_data.loc[english_data["date"] >= datetime.datetime(2022, 1, 1)] #Filter data for 2022 data.
welsh_data_2022 = welsh_data.loc[welsh_data["date"] >= datetime.datetime(2022, 1, 1)]

english_data_2022_filtered = english_data_2022.loc[english_data_2022["newCasesByPublishDate"] != 0] #Remove rows that have 0 new cases - case reporting not available.
welsh_data_2022_filtered = welsh_data_2022.loc[welsh_data_2022["newCasesByPublishDate"] != 0]

english_data_2022_arr = english_data_2022_filtered["newCasesByPublishDate"].values #Convert day-by-day case columns to np.arrays.
welsh_data_2022_arr = welsh_data_2022_filtered["newCasesByPublishDate"].values

english_data_2022_std = np.std(english_data_2022_arr) #Find standard deviation of each country's day-by-day case data.
welsh_data_2022_std = np.std(welsh_data_2022_arr)

print(f">> Standard deviation of England's day-by-day data: {english_data_2022_std}")
print(f">> Standard deviation of Wales' day-by-day data: {welsh_data_2022_std}")

plt.plot(english_data_2022_filtered["date"], english_data_2022_filtered["newCasesByPublishDate"],"go", label="England") #Plots day-by-day cases of both countries.
plt.plot(welsh_data_2022_filtered["date"], welsh_data_2022_filtered["newCasesByPublishDate"],"bo", label="Wales")
plt.xlabel("Date")
plt.ylabel("Daily cases")
plt.title("COVID-19 cases per day")
plt.legend()
plt.show()