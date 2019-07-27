# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import packages
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr
from bs4 import BeautifulSoup
import requests
import math

# This converts R objects to Python objects automatically
pandas2ri.activate()


# Create an empty Pandas DataFrame so when scraping the population data it can go somewhere
state_pop = pd.DataFrame(columns=['State', 'Pop', 'Year'])

# This St. Louis FED site has population from 2000 to 2017
# 2018 is in a different format, so this only scrapes through 2017
for year in range(2000, 2018):
    # Keeping track of the loop
    print(year)
    # This is the URL that has the data
    url = 'https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od=' + str(year) +'-01-01#'
    # Read in the url
    url_request = requests.get(url)
    # Make the soup
    pop_data = BeautifulSoup(url_request.content, features="lxml")
    
    # Turn the data into a table for parsing
    web_data_in_list = pop_data.prettify().splitlines()
    
    # The states appear 6 lines after this text
    states = [state_index for state_index in web_data_in_list if '''POP" target="_blank">''' in state_index]    
    
    # Create some empty lists
    state_name = []
    state_pop_num = []
    state_year = []
    
    # Loop through the data and find each state and save the data in the lists
    for state in states:
        # Get the element in the website table
        n = web_data_in_list.index(state)
        # The name of the state is on the next line after that text above
        state_name.append(web_data_in_list[n+1].lstrip())
        # The population is on the 6th line after the tect above
        state_pop_num.append(float(web_data_in_list[n+6].replace(",", ""))*1000)
        # I just want to repeat the year number 52 times for the data frame
        state_year = [str(year)]*52
    
    #Save the lists in a data frame
    state_df = pd.DataFrame({'State':state_name, 'Pop':state_pop_num, 'Year':state_year})
    
    # Appending the state population data together
    state_pop = state_pop.append(state_df, ignore_index = True)

# 2018 population data waas a little different    
year = 2018

# Get the 2018 data
url = 'https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od=#'
url_request = requests.get(url)
pop_data = BeautifulSoup(url_request.content, features="lxml")
    
# Same as above
web_data_in_list = pop_data.prettify().splitlines()
states = [state_index for state_index in web_data_in_list if '''POP" target="_blank">''' in state_index]    
states.remove('            <a href="/series/DSPOP" target="_blank">')

# Create lists
state_name = []
state_pop_num = []
state_year = []
    
# Loop through each states
for state in states:
    n = web_data_in_list.index(state)
    state_name.append(web_data_in_list[n+1].lstrip())
    state_pop_num.append(float(web_data_in_list[n+9].replace(",", ""))*1000)
    state_year = [str(year)]*51
    
# Create the 2018 Data Frame
state_df = pd.DataFrame({'State':state_name, 'Pop':state_pop_num, 'Year':state_year})
    
# Get all of the state population data together
state_pop = state_pop.append(state_df, ignore_index = True)

# Create a Python function from ts, ts creates a time series object in R
ts=robjects.r('ts')

# Import the entire R package Forecast
forecast=importr('forecast')

# Create empty data frame for the state forecases
state_forecasts = pd.DataFrame(columns=['State', 'Forecast'])

# Generate a Forecast for each state
for state in state_pop.State.unique():
    # grab the data and sort it
    data_for_forecast = state_pop.loc[state_pop['State'] == state].sort_values(['Year'], ascending = True)['Pop'].values
    # Generate time series object
    forecast_ts = ts(data_for_forecast)
    # Fit the forecast using the Auto Arima function from R
    fit = forecast.auto_arima(forecast_ts)
    # Generate the forecast using the forecast function in R
    forecast_output=forecast.forecast(fit,h=2,level=(95.0))
    # Get the 2020 forecast in a data frame
    temp_forecast = pd.DataFrame({'State':state, 'Forecast':pandas2ri.ri2py(forecast_output[3])}).loc[1]
    # Append all of the data frames together
    state_forecasts = state_forecasts.append(temp_forecast, ignore_index = True)
    # Print the forecast to make sure it works
    print(state_forecasts)

# Filter some of the data out
state_forecasts = state_forecasts[state_forecasts.State != 'FRB-St. Louis District States']
state_forecasts = state_forecasts[state_forecasts.State != 'District of Columbia']

# initialize each state with one electoral college seat
state_forecasts['Seats'] = 1
state_forecasts['A_n'] = 1
# Create each state's priority ranking 
state_forecasts['Priority'] = state_forecasts['Forecast']/math.sqrt(2)

# Get the initial number of seats
seats = sum(state_forecasts['Seats'])

# While there are seats left to be allocated
while seats < 435:
    # Get the state with the Max priority
    max_state = state_forecasts[state_forecasts['Priority'] == max(state_forecasts['Priority'])]
    # Get the rest of the states
    not_max_state = state_forecasts[state_forecasts['Priority'] != max(state_forecasts['Priority'])]

    # Change the number, priority, and number of seats
    max_state.loc[:,'A_n'] = max_state['A_n'] + 1
    max_state.loc[:,'Priority'] = math.sqrt(max_state['Seats'].unique()/(max_state['Seats'].unique()+2))*state_forecasts['Priority']
    max_state.loc[:,'Seats'] = max_state['Seats'] + 1
    
    # Append all of the data back together
    state_forecasts = max_state.append(not_max_state)

    #Add up the number of seats
    seats = sum(state_forecasts['Seats'])

# Write file to CSV to read into data viz software    
state_forecasts.to_csv("C:/users/palmer/desktop/State Forecasts.csv")
state_pop.to_csv("C:/users/palmer/desktop/State Population.csv")

