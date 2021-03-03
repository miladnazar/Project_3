import pandas as pd
import numpy as np
import requests
import math
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from sklearn.model_selection import train_test_split

real_state_stocks = pd.read_csv('Resources/Real_State_Stocks_Update.csv')
# Reset the date as the index
real_state_stocks = real_state_stocks.set_index(pd.DatetimeIndex(real_state_stocks['Date'].values))
#Remove the Date column
real_state_stocks.drop(columns=['Date'], axis=1, inplace=True)
real_state_stocks.drop(columns=['SPGSLG'], axis=1, inplace=True)

# Optimize the portfolio
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu = expected_returns.mean_historical_return(real_state_stocks)
S = risk_models.sample_cov(real_state_stocks)

# Optimize for the maximal Sharpe ratio 
ef = EfficientFrontier(mu, S) # Creates the Efficient Frontier Object
weights = ef.max_sharpe()

cleaned_weights = ef.clean_weights()
#print(cleaned_weights)
ef.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

portfolio_val = 100000
latest_prices = get_latest_prices(real_state_stocks)
weights = cleaned_weights
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=portfolio_val)
allocation, leftover = da.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)



comm_srvc_stocks = pd.read_csv('Resources/Communication_Services.csv')
# Reset the date as the index
comm_srvc_stocks = comm_srvc_stocks.set_index(pd.DatetimeIndex(comm_srvc_stocks['Date'].values))
#Remove the Date column
comm_srvc_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_1 = expected_returns.mean_historical_return(comm_srvc_stocks)
S_1 = risk_models.sample_cov(comm_srvc_stocks)

# Optimize for the miximal Shrpe ratio 
ef_1 = EfficientFrontier(mu_1, S_1) # Creates the Efficient Frontier Object
weights_1 = ef_1.max_sharpe()

cleaned_weights_1 = ef_1.clean_weights()
#print(cleaned_weights_1)
ef_1.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

portfolio_val_1 = 100000
latest_prices_1 = get_latest_prices(comm_srvc_stocks)
weights_1 = cleaned_weights_1
da_1 = DiscreteAllocation(weights_1, latest_prices_1, total_portfolio_value=portfolio_val_1)
allocation, leftover = da_1.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

energy_stocks = pd.read_csv('Resources/Energy.csv')
# Reset the date as the index
energy_stocks = energy_stocks.set_index(pd.DatetimeIndex(energy_stocks['Date'].values))
#Remove the Date column
energy_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_2 = expected_returns.mean_historical_return(energy_stocks)
S_2 = risk_models.sample_cov(energy_stocks)

# Optimize for the miximal Shrpe ratio 
ef_2 = EfficientFrontier(mu_2, S_2) # Creates the Efficient Frontier Object
weights_2 = ef_2.max_sharpe()

cleaned_weights_2 = ef_2.clean_weights()
#print(cleaned_weights_2)
ef_2.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_2 = 100000
latest_prices_2 = get_latest_prices(energy_stocks)
weights_2 = cleaned_weights_2
da_2 = DiscreteAllocation(weights_2, latest_prices_2, total_portfolio_value=portfolio_val_2)
allocation, leftover = da_2.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

healthcare_stocks = pd.read_csv('Resources/Health_Care.csv')
# Reset the date as the index
healthcare_stocks = healthcare_stocks.set_index(pd.DatetimeIndex(healthcare_stocks['Date'].values))
#Remove the Date column
healthcare_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_3 = expected_returns.mean_historical_return(healthcare_stocks)
S_3 = risk_models.sample_cov(healthcare_stocks)

# Optimize for the miximal Shrpe ratio 
ef_3 = EfficientFrontier(mu_3, S_3) # Creates the Efficient Frontier Object
weights_3 = ef_3.max_sharpe()

cleaned_weights_3 = ef_3.clean_weights()
#print(cleaned_weights_3)
ef_3.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_3 = 100000
latest_prices_3 = get_latest_prices(healthcare_stocks)
weights_3 = cleaned_weights_3
da_3 = DiscreteAllocation(weights_3, latest_prices_3, total_portfolio_value=portfolio_val_3)
allocation, leftover = da_3.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)


financials_stocks = pd.read_csv('Resources/Financials.csv')
# Reset the date as the index
financials_stocks = financials_stocks.set_index(pd.DatetimeIndex(financials_stocks['Date'].values))
#Remove the Date column
financials_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Get the assets /tickers
assets_4 = financials_stocks.columns
# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_4 = expected_returns.mean_historical_return(financials_stocks)
S_4 = risk_models.sample_cov(financials_stocks)

# Optimize for the miximal Shrpe ratio 
ef_4 = EfficientFrontier(mu_4, S_4) # Creates the Efficient Frontier Object
weights_4 = ef_4.max_sharpe()

cleaned_weights_4 = ef_4.clean_weights()
#print(cleaned_weights_4)
ef_4.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_4 = 100000
latest_prices_4 = get_latest_prices(financials_stocks)
weights_4 = cleaned_weights_4
da_4 = DiscreteAllocation(weights_4, latest_prices_4, total_portfolio_value=portfolio_val_4)
allocation, leftover = da_4.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)


IT_stocks = pd.read_csv('Resources/Information_Technology.csv')
# Reset the date as the index
IT_stocks = IT_stocks.set_index(pd.DatetimeIndex(IT_stocks['Date'].values))
#Remove the Date column
IT_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_5 = expected_returns.mean_historical_return(IT_stocks)
S_5 = risk_models.sample_cov(IT_stocks)

# Optimize for the miximal Shrpe ratio 
ef_5 = EfficientFrontier(mu_5, S_5) # Creates the Efficient Frontier Object
weights_5 = ef_5.max_sharpe()

cleaned_weights_5 = ef_5.clean_weights()
#print(cleaned_weights_5)
ef_5.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_5 = 100000
latest_prices_5 = get_latest_prices(IT_stocks)
weights_5 = cleaned_weights_5
da_5 = DiscreteAllocation(weights_5, latest_prices_5, total_portfolio_value=portfolio_val_5)
allocation, leftover = da_5.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

materials_stocks = pd.read_csv('Resources/Materials.csv')
# Reset the date as the index
materials_stocks = materials_stocks.set_index(pd.DatetimeIndex(materials_stocks['Date'].values))
#Remove the Date column
materials_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_6 = expected_returns.mean_historical_return(materials_stocks)
S_6 = risk_models.sample_cov(materials_stocks)

# Optimize for the miximal Shrpe ratio 
ef_6 = EfficientFrontier(mu_6, S_6) # Creates the Efficient Frontier Object
weights_6 = ef_6.max_sharpe()

cleaned_weights_6 = ef_6.clean_weights()
#print(cleaned_weights_6)
ef_6.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_6 = 100000
latest_prices_6 = get_latest_prices(materials_stocks)
weights_6 = cleaned_weights_6
da_6 = DiscreteAllocation(weights_6, latest_prices_6, total_portfolio_value=portfolio_val_6)
allocation, leftover = da_6.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

utilities_stocks = pd.read_csv('Resources/Utilities.csv')
# Reset the date as the index
utilities_stocks = utilities_stocks.set_index(pd.DatetimeIndex(utilities_stocks['Date'].values))
#Remove the Date column
utilities_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_7 = expected_returns.mean_historical_return(utilities_stocks)
S_7 = risk_models.sample_cov(utilities_stocks)

# Optimize for the miximal Shrpe ratio 
ef_7 = EfficientFrontier(mu_7, S_7) # Creates the Efficient Frontier Object
weights_7 = ef_7.max_sharpe()

cleaned_weights_7 = ef_7.clean_weights()
#print(cleaned_weights_7)
ef_7.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_7 = 100000
latest_prices_7 = get_latest_prices(utilities_stocks)
weights_7 = cleaned_weights_7
da_7 = DiscreteAllocation(weights_7, latest_prices_7, total_portfolio_value=portfolio_val_7)
allocation, leftover = da_7.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

industrial_stocks = pd.read_csv('Resources/Industrial.csv')
# Reset the date as the index
industrial_stocks = industrial_stocks.set_index(pd.DatetimeIndex(industrial_stocks['Date'].values))
#Remove the Date column
industrial_stocks.drop(columns=['Date'], axis=1, inplace=True)

# Get the assets /tickers
assets_8 = industrial_stocks.columns
# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_8 = expected_returns.mean_historical_return(industrial_stocks)
S_8 = risk_models.sample_cov(industrial_stocks)

# Optimize for the miximal Shrpe ratio 
ef_8 = EfficientFrontier(mu_8, S_8) # Creates the Efficient Frontier Object
weights_8 = ef_8.max_sharpe()

cleaned_weights_8 = ef_8.clean_weights()
#print(cleaned_weights_8)
ef_8.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_8 = 100000
latest_prices_8 = get_latest_prices(industrial_stocks)
weights_8 = cleaned_weights_8
da_8 = DiscreteAllocation(weights_8, latest_prices_8, total_portfolio_value=portfolio_val_8)
allocation, leftover = da_8.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)


consumer_staples_stocks = pd.read_csv('Resources/Consumer_Staples.csv')
# Reset the date as the index
consumer_staples_stocks = consumer_staples_stocks.set_index(pd.DatetimeIndex(consumer_staples_stocks['Date'].values))
#Remove the Date column
consumer_staples_stocks.drop(columns=['Date'], axis=1, inplace=True)


# Get the assets /tickers
assets_9 = consumer_staples_stocks.columns
# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_9 = expected_returns.mean_historical_return(consumer_staples_stocks)
S_9 = risk_models.sample_cov(consumer_staples_stocks)

# Optimize for the miximal Shrpe ratio 
ef_9 = EfficientFrontier(mu_9, S_9) # Creates the Efficient Frontier Object
weights_9 = ef_9.max_sharpe()

cleaned_weights_9 = ef_9.clean_weights()
#print(cleaned_weights_9)
ef_9.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
portfolio_val_9 = 100000
latest_prices_9 = get_latest_prices(consumer_staples_stocks)
weights_9 = cleaned_weights_9
da_9 = DiscreteAllocation(weights_9, latest_prices_9, total_portfolio_value=portfolio_val_9)
allocation, leftover = da_9.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)

consumer_discretionary_stocks = pd.read_csv('Resources/Consumer_Discretionary.csv')
# Reset the date as the index
consumer_discretionary_stocks = consumer_discretionary_stocks.set_index(pd.DatetimeIndex(consumer_discretionary_stocks['Date'].values))
#Remove the Date column
consumer_discretionary_stocks.drop(columns=['Date'], axis=1, inplace=True)


# Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
mu_10 = expected_returns.mean_historical_return(consumer_discretionary_stocks)
S_10 = risk_models.sample_cov(consumer_discretionary_stocks)

# Optimize for the miximal Shrpe ratio 
ef_10 = EfficientFrontier(mu_10, S_10) # Creates the Efficient Frontier Object
weights_10 = ef_10.max_sharpe()

cleaned_weights_10 = ef_10.clean_weights()
#print(cleaned_weights_10)
ef_10.portfolio_performance(verbose=True)

# Get the descret allocation of each share per stock
# How can we make this a function so the customer put their investment amount
# Also how can we make a function so the customer put their investment industry
#def portfolio_val_10():
    
#    return 
portfolio_val_10 = 100000
latest_prices_10 = get_latest_prices(consumer_discretionary_stocks)
weights_10 = cleaned_weights_10
da_10 = DiscreteAllocation(weights_10, latest_prices_10, total_portfolio_value=portfolio_val_10)
allocation, leftover = da_10.lp_portfolio()
print("Discrete allocation:", allocation)
print("Funds Remaining: $", leftover)