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

def generate_portfolio(starting_investment, stock_price_history):

    # Reset the date as the index
    stock_price_history = stock_price_history.set_index(pd.DatetimeIndex(stock_price_history['Date'].values))
    #Remove the Date column
    stock_price_history.drop(columns=['Date'], axis=1, inplace=True)
    stock_price_history.dropna(axis=1, inplace=True)

    # Optimize the portfolio
    from pypfopt.efficient_frontier import EfficientFrontier
    from pypfopt import risk_models
    from pypfopt import expected_returns

    # Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
    mu = expected_returns.mean_historical_return(stock_price_history)
    S = risk_models.sample_cov(stock_price_history)

    # Optimize for the maximal Sharpe ratio 
    ef = EfficientFrontier(mu, S) # Creates the Efficient Frontier Object
    weights = ef.max_sharpe()

    cleaned_weights = ef.clean_weights()
    #print(cleaned_weights)
    ef.portfolio_performance(verbose=True)

    # Get the descret allocation of each share per stock
    from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

    latest_prices = get_latest_prices(stock_price_history)
    weights = cleaned_weights
    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=starting_investment)
    allocation, leftover = da.lp_portfolio()
    print("Discrete allocation:", allocation)
    print("Funds Remaining: $", leftover)
    return (allocation, leftover)


portfolio_val = 100000
print()
print()
print("Real Estate")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Real_State_Stocks_Update.csv'))
print()
print()
print("Communication Services")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Communication_Services.csv'))
print()
print()
print("Consumer Discretionary")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Consumer_Discretionary.csv'))
print()
print()
print("Consumer Staples")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Consumer_Staples.csv'))
print()
print()
print("Energy")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Energy.csv'))
print()
print()
print("Financials")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Financials.csv'))
print()
print()
print("Health Care")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Health_Care.csv'))
print()
print()
print("Industrial")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Industrial.csv'))
print()
print()
print("Information Technology")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Information_Technology.csv'))
print()
print()
print("Materials")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Materials.csv'))
print()
print()
print("Utilities")
print()
generate_portfolio(portfolio_val, pd.read_csv('Resources/Utilities.csv'))






