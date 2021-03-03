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

real_state_stocks = pd.read_csv('..//Resources/Real_State_Stocks_Update.csv')
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