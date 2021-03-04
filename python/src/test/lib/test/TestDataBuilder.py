# Initial imports
import os
import alpaca_trade_api as tradeapi
import pandas as pd
import requests
from pathlib import Path
import json

from main.lib.datastructures.StockInfoContainer import StockInfoContainer
from main.lib.datastructures.CustomerMetrics import CustomerMetrics

class TestDataBuilder:


    def __init__(self, debug_level=0):
        self.debug_level = debug_level
        self.__fmp_cloud_key = 'd62b3ac01083146edd0acaa71d57074a'


    # --------------------------------------------------------------------------
    # Integration Test Helpers
    # --------------------------------------------------------------------------


    def build_customer_metrics(self):
        customer_metrics = CustomerMetrics("Long", 5000, "Medium", "Intermediate")
        return customer_metrics


    def build_container_stocktickers(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_ticker("AAPL")
        stock_info_container.add_ticker("BNGO")
        stock_info_container.add_ticker("CIIC")


    def build_container_raw_stockscores(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_stock_raw_score("AAPL", 0.95, "Price")
        stock_info_container.add_stock_raw_score("BNGO", 0.98, "Price")
        stock_info_container.add_stock_raw_score("AAPL", 0.85, "Valuation")
        stock_info_container.add_stock_raw_score("BNGO", 0.84, "Valuation")
        stock_info_container.add_stock_raw_score("CIIC", 0.30, "Price")
        return stock_info_container


    def build_container_portfolio(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_stock_to_portfolio("AAPL", 100)
        stock_info_container.add_stock_to_portfolio("BNGO", 100)
        stock_info_container.add_stock_to_portfolio("CIIC", 100)

    def build_container_price_history(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        self.__alpaca_api_key = "PKA0PKYDPIZRN5Q6EKE0"
        self.__alpaca_secret_key = "pNS3zeDdHxV4r4rctUHqanoshaTILhySqRVMvsD4"
        self.__alpaca = tradeapi.REST(self.__alpaca_api_key, self.__alpaca_secret_key, api_version="v2")
        self.__fmp_cloud_key = '31853220bc5708a36155ca7f0481a5e0'
        now = pd.Timestamp.now(tz="America/New_York")
        trailing_n_days = 100
        offset = pd.Timedelta(trailing_n_days, unit="days")
        start = now - offset
        timeframe = "1D"
        stock_closing_prices_df = pd.DataFrame()
        for stock_ticker in [ "AAPL", "BNGO", "CIIC" ]:
            data = self.__alpaca.get_barset([stock_ticker], timeframe, start=start.isoformat(), end=now.isoformat()).df
            stock_closing_prices_df[stock_ticker] = data[stock_ticker]["close"]
        stock_info_container.add_stock_price_history(stock_closing_prices_df)
        return stock_info_container


    def build_container_financial_metadata(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()

        for stock_ticker in ["AAPL", "BNGO", "CIIC"]:
            try:
                fmp_cloud_key = 'd62b3ac01083146edd0acaa71d57074a'
                stock_financial_metadata_str = requests.get(
                    f"https://fmpcloud.io/api/v3/financial-statement-full-as-reported/{stock_ticker}?apikey={fmp_cloud_key}")
                # TODO Other requests for auxilliary data?
            except:
                continue
            stock_financial_metadata_json = stock_financial_metadata_str.json()
            stock_financial_metadata = stock_financial_metadata_json  # self.__process_stock_financial_metadata_json(stock_financial_metadata_json)
            stock_info_container.add_stock_financial_metadata(stock_ticker, stock_financial_metadata)
        return stock_info_container


    # --------------------------------------------------------------------------
    # StockInfoContainer Helpers
    # --------------------------------------------------------------------------


    def build_simple_portfolio(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_stock_to_portfolio("AAPL", 102)
        stock_info_container.add_stock_to_portfolio("MSFT", 103)
        stock_info_container.add_stock_to_portfolio("TSLA", 104)
        return stock_info_container


    def build_simple_raw_scores(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_stock_raw_score("AAPL", 0.8, "price analysis")
        stock_info_container.add_stock_raw_score("MSFT", 0.6, "valuation analysis")
        stock_info_container.add_stock_raw_score("TSLA", 0.4, "other analysis")
        return stock_info_container


    def build_simple_composite_scores(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        stock_info_container.add_stock_composite_score("AAPL", 0.8)
        stock_info_container.add_stock_composite_score("MSFT", 0.6)
        stock_info_container.add_stock_composite_score("TSLA", 0.4)
        return stock_info_container


    def build_stock_price_data(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        expected_index = [
            pd.Timestamp("01-01-2021", tz="America/New_York"),
            pd.Timestamp("01-02-2021", tz="America/New_York"),
            pd.Timestamp("01-03-2021", tz="America/New_York")
        ]
        expected_stock_price_history = pd.DataFrame({"AAPL": [100.0, 101.0, 102.3], "MSFT": [56.0, 56.2, 59.3]}, index=expected_index)
        return (stock_info_container, expected_index, expected_stock_price_history)


    def build_financial_metadata(self, stock_info_container=None):
        if stock_info_container is None:
            stock_info_container = StockInfoContainer()
        file_path = Path("data/fmpcloud_sample_aapl.json")
        with open(file_path, "r") as json_file:
            expected_financial_metadata_str = json_file.read()
            expected_financial_metadata = json.loads(expected_financial_metadata_str)
            stock_info_container.add_stock_financial_metadata("AAPL", expected_financial_metadata)
        return (stock_info_container, expected_financial_metadata)
