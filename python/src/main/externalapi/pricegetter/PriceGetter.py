# Initial imports
import os

import alpaca_trade_api as tradeapi
import pandas as pd
import requests


class PriceGetter:


    def __init__(self, debug_level=0):

        self.__debug_level = debug_level

        # Set Alpaca API key and secret
        self.__alpaca_api_key = "PKA0PKYDPIZRN5Q6EKE0"
        self.__alpaca_secret_key = "pNS3zeDdHxV4r4rctUHqanoshaTILhySqRVMvsD4"

        # Create the Alpaca API object
        self.__alpaca = tradeapi.REST(self.__alpaca_api_key, self.__alpaca_secret_key, api_version="v2")

        # Fmp Cloud API Key
        self.__fmp_cloud_key = '31853220bc5708a36155ca7f0481a5e0'


    def get_tickers(self, use_test_data=False):
        stock_ticker_list = []
        if use_test_data:
            stock_ticker_list = [ "AAPL", "TSLA", "MSFT" ]
        else:
            # Get all available stock tickers above simple market cap
            stock_ticker_str = requests.get(f'https://fmpcloud.io/api/v3/stock-screener?marketCapMoreThan=100000000&limit=100&apikey={self.__fmp_cloud_key}')
            stock_ticker_json = stock_ticker_str.json()
            for item in stock_ticker_json:
                stock_ticker_list.append(item['symbol'])

        return stock_ticker_list


    def get_prices(self, stock_info_container, trailing_n_days):

        # Build dates to capture trailing n days
        now = pd.Timestamp.now(tz="America/New_York")
        offset = pd.Timedelta(trailing_n_days, unit="days")
        start = now - offset

        # Set timeframe to '1D' for Alpaca API
        timeframe = "1D"

        # Get stock prices
        stock_closing_prices_df = pd.DataFrame()
        for stock_ticker in stock_info_container.get_all_tickers():

            # Get current closing prices and append to dataset
            data = self.__alpaca.get_barset([stock_ticker], timeframe, start=start.isoformat(), end=now.isoformat()).df
            stock_closing_prices_df[stock_ticker] = data[stock_ticker]["close"]

        stock_info_container.add_stock_price_history(stock_closing_prices_df)
        return stock_info_container
