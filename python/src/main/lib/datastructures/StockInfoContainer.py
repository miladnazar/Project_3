import pandas as pd

from main.lib.datastructures.StockFinancialMetadata import StockFinancialMetadata
from ..datastructures.StockScore import StockScore


class StockInfoContainer:

    def __init__(self):
        self.__ticker_set = set()
        self.__stock_raw_score_map = {}
        self.__stock_composite_score_map = {}
        self.__portfolio = {}
        self.__stock_price_history = pd.DataFrame()

        # Dictionary of { stock_ticker -> StockFinancialMetadata }
        self.__financial_metadata = {}

    # --------------------------------------------------------------------------
    # Add stock info
    # --------------------------------------------------------------------------

    def add_ticker(self, ticker):
        self.__register_ticker(ticker)

    def remove_ticker(self, ticker):
        self.__deregister_ticker(ticker)

    def add_ticker_list(self, ticker_list):
        for ticker in ticker_list:
            self.__register_ticker(ticker)

    def add_stock_raw_score(self, ticker, score, analysis_source):
        """
        Add StockInfo for a stock with a score metric.
        :param ticker:
        :param analysis_source:
        :param score:
        :return:
        """
        self.__register_ticker(ticker)
        if not (ticker in self.__stock_raw_score_map):
            self.__stock_raw_score_map[ticker] = []
        self.__stock_raw_score_map[ticker].append(StockScore(ticker, score, analysis_source))

    def add_stock_composite_score(self, ticker, composite_score):
        self.__register_ticker(ticker)
        self.__stock_composite_score_map[ticker] = StockScore(ticker, composite_score, "Composite")

    def add_stock_to_portfolio(self, ticker, num_shares):
        self.__register_ticker(ticker)
        self.__portfolio[ticker] = num_shares

    def add_stock_price_history(self, stock_price_history):
        for stock_ticker in self.get_all_tickers():
            self.__register_ticker(stock_ticker)
        self.__stock_price_history = stock_price_history

    def add_stock_financial_metadata(self, ticker, stock_financial_metadata_listmap):
        self.__register_ticker(ticker)
        self.__financial_metadata[ticker] = StockFinancialMetadata(ticker, stock_financial_metadata_listmap)

    # --------------------------------------------------------------------------
    # Getters - All stock data
    # --------------------------------------------------------------------------

    def get_all_tickers(self):
        return list(self.__ticker_set)

    def get_all_raw_scores_single_level(self):
        """
        Expose stock score objects in a flat list.
        :return:
        """
        values_nested_list = self.__stock_raw_score_map.values()
        return [item for sublist in values_nested_list for item in sublist]

    def get_all_composite_scores_single_level(self):
        return list(self.__stock_composite_score_map.values())

    def get_portfolio(self):
        return self.__portfolio

    def get_all_price_history(self):
        return self.__stock_price_history

    def get_all_financial_metadata(self):
        return self.__financial_metadata

    # --------------------------------------------------------------------------
    # Getters - Individual stock data
    # --------------------------------------------------------------------------

    def get_stock_raw_score_list(self, ticker):
        return self.__stock_raw_score_map.get(ticker, None)

    def get_stock_composite_score(self, ticker):
        return self.__stock_composite_score_map.get(ticker, None)

    def get_stock_num_shares(self, ticker):
        return self.__portfolio.get(ticker, None)

    def get_stock_price_history(self, ticker):
        return self.__stock_price_history.get(ticker, None)

    def get_stock_financial_metadata(self, ticker):
        return self.__financial_metadata.get(ticker, None)

    # --------------------------------------------------------------------------
    # Helper functions
    # --------------------------------------------------------------------------

    def __register_ticker(self, ticker):
        self.__ticker_set.add(ticker)

    def __deregister_ticker(self, ticker):
        self.__ticker_set.remove(ticker)
