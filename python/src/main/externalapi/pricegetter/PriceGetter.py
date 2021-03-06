# Initial imports
import os

import alpaca_trade_api as tradeapi
import pandas as pd
import requests

from python.src.main.lib.persistentdata.CSVDataLoader import CSVDataLoader
from python.src.main.lib.persistentdata.IndustryData import IndustryData


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


    # --------------------------------------------------------------------------
    # Tickers
    # --------------------------------------------------------------------------


    def get_tickers(self, ticker_type="Stocks", use_test_data=False, use_csv_input_data=False):
        """
        Get the list of tickers to use for consideration of a portfolio. This list drives the entire
        portoflio building process i.e. only these tickers will be analyzed for consideration in the
        portoflio.

        :param type: Type of tickers. Valid entries: "Stocks", "Cryptos", "StocksAndCryptos", "Industries"
        :param use_test_data: Use test data.
        :param use_csv_input_data: Use data from CSV files.
        :return: List of tickers to drive the portfolio building process.
        """
        if "Stocks" == ticker_type:
            return self.__get_stock_tickers(use_test_data, use_csv_input_data)
        elif "Cryptos" == ticker_type:
            return self.__get_crypto_tickers(use_test_data, use_csv_input_data)
        elif "StocksAndCryptos" == ticker_type:
            stock_ticker_list = []
            stock_ticker_list.append(self.__get_stock_tickers(use_test_data, use_csv_input_data))
            stock_ticker_list.append(self.__get_crypto_tickers(use_test_data, use_csv_input_data))
            return stock_ticker_list
        elif "Industries" == ticker_type:
            return self.__get_industry_tickers(use_test_data, use_csv_input_data)
        else:
            return []


    def __get_stock_tickers(self, use_test_data, use_csv_input_data):
        if use_test_data:
            stock_ticker_list = ["AAPL", "TSLA", "MSFT"]
        elif use_csv_input_data:
            # TODO Not implemented
            return []
        else:
            # Get all available stock tickers above simple market cap
            stock_ticker_str = requests.get(f'https://fmpcloud.io/api/v3/stock-screener?marketCapMoreThan=100000000&limit=100&apikey={self.__fmp_cloud_key}')
            stock_ticker_json = stock_ticker_str.json()
            stock_ticker_list = []
            for item in stock_ticker_json:
                stock_ticker_list.append(item['symbol'])
            return stock_ticker_list


    def __get_crypto_tickers(self, use_test_data, use_csv_input_data):
        if use_test_data:
            # TODO Not implemented
            return []
        elif use_csv_input_data:
            # TODO Not implemented
            return []
        else:
            # TODO Not implemented
            return []


    def __get_industry_tickers(self, use_test_data, use_csv_input_data):
        if use_test_data:
            # TODO Not implemented
            return []
        elif use_csv_input_data:
            industry_list_dict = IndustryData().get_data()
            return industry_list_dict.get_keys().as_list()
        else:
            # TODO Not implemented
            return []


    # --------------------------------------------------------------------------
    # Prices
    # --------------------------------------------------------------------------


    def get_prices(self, stock_info_container, trailing_n_days, ticker_type, use_test_data=False, use_csv_input_data=False):
        if "Stocks" == ticker_type:
            return self.__get_stock_price_data(stock_info_container, trailing_n_days, use_test_data, use_csv_input_data)
        elif "Cryptos" == ticker_type:
            # TODO Not implemented
            return None
        elif "StocksAndCryptos" == ticker_type:
            # TODO Not implemented
            return None
        elif "Industries" == ticker_type:
            return self.__get_industry_price_data(stock_info_container, use_test_data, use_csv_input_data)
        else:
            # TODO Return error
            return None


    def __get_stock_price_data(self, stock_info_container, trailing_n_days, use_test_data, use_csv_input_data):
        if use_test_data:
            # TODO Not implemented
            return None
        elif use_csv_input_data:
            return self.__get_stock_prices_from_csvdata(stock_info_container)
        else:
            return self.__get_stock_prices_from_datasource(stock_info_container, trailing_n_days)


    def __get_stock_prices_from_csvdata(self, stock_info_container):
        # TODO Not implemented
        return None


    def __get_stock_prices_from_datasource(self, stock_info_container, trailing_n_days):

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


    def __get_industry_price_data(self, stock_info_container, use_test_data, use_csv_input_data):
        if use_test_data:
            # TODO Not implemented
            return None
        elif use_csv_input_data:
            return self.__get_industry_price_data_from_csv()
        else:
            # TODO Not implemented
            return None


    def __get_industry_price_data_from_csv(self, stock_info_container):
        # TODO Should be driven by stock_info_container.get_all_tickers()
        # for ticker in stock_info_container.get_all_tickers():

        industry_data = IndustryData()
        return industry_data.industry_price_history__
