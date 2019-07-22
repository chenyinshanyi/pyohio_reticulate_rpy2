import numpy
import pandas as pd
import scipy
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import pandas2ri
pandas2ri.activate()

robjects.r("seq(from = as.Date('2018-01-15'), by = ('-2 months'), length = 12)")
robjects.r("as.character(seq(from = as.Date('2018-01-15'), by = ('-2 months'), length = 12))")

reds = robjects.r('''season <- c() 
                  set.seed(50) 
                  for(i in 1:10000) { 
                  reds_wins <- 41 
                  reds_losses <- 46 
                  for(i in 1:75){ 
                  game <- runif(1)
                  
                  if(game <= reds_wins/(reds_wins + reds_losses)) {
                  reds_wins = reds_wins + 1} else {
                  reds_losses = reds_losses + 1}
                  }
                  season <- c(season, reds_wins/(reds_wins + reds_losses))
                  }
                  mean(season > 90/162)''')



from bs4 import BeautifulSoup
import requests
import pandas as pd
from rpy2.robjects import pandas2ri
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

state_pop = pd.DataFrame(columns=['State', 'Pop', 'Year'])

for year in range(2000, 2018):
    print(year)
    url = 'https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od=' + str(year) +'-01-01#'
    url_request = requests.get(url)
    pop_data = BeautifulSoup(url_request.content, features="lxml")
    
    web_data_in_list = pop_data.prettify().splitlines()
    states = [state_index for state_index in web_data_in_list if '''POP" target="_blank">''' in state_index]    
    
    state_name = []
    state_pop_num = []
    state_year = []
    
    for state in states:
        n = web_data_in_list.index(state)
        state_name.append(web_data_in_list[n+1].lstrip())
        state_pop_num.append(float(web_data_in_list[n+6].replace(",", ""))*1000)
        state_year = [str(year)]*52
    
    state_df = pd.DataFrame({'State':state_name, 'Pop':state_pop_num, 'Year':state_year})
    
    state_pop = state_pop.append(state_df, ignore_index = True)

    
year = 2018

url = 'https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od=#'
url_request = requests.get(url)
pop_data = BeautifulSoup(url_request.content, features="lxml")
    
web_data_in_list = pop_data.prettify().splitlines()
states = [state_index for state_index in web_data_in_list if '''POP" target="_blank">''' in state_index]    
states.remove('            <a href="/series/DSPOP" target="_blank">')

state_name = []
state_pop_num = []
state_year = []
    
for state in states:
    n = web_data_in_list.index(state)
    state_name.append(web_data_in_list[n+1].lstrip())
    state_pop_num.append(float(web_data_in_list[n+6].replace(",", ""))*1000)
    state_year = [str(year)]*51
    
state_df = pd.DataFrame({'State':state_name, 'Pop':state_pop_num, 'Year':state_year})
    
state_pop = state_pop.append(state_df, ignore_index = True)

pandas2ri.activate()


alabama = state_pop.loc[state_pop['State'] == 'Alabama'].sort_values(['Year'], ascending = True)['Pop'].values

ts=robjects.r('ts')
forecast=importr('forecast')

alabama_ts = ts(alabama)
fit = forecast.auto_arima(alabama_ts)
forecast_output=forecast.forecast(fit,h=2,level=(95.0))


pandas2ri.ri2py(forecast)

forecast=pandas2ri.ri2py(forecast_output[3])
