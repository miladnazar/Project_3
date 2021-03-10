import pandas as pd


class StockInfoContainer:

    def __init__(self):
        self.__ticker_set = set()
        self.__portfolio = {}
        self.__expected_performance = None
        self.__stock_price_history = pd.DataFrame()


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

    def add_portfolio_to_portfolio(self, portfolio):
        for ticker in portfolio.keys():
            self.add_stock_to_portfolio(ticker, portfolio[ticker])

    def add_stock_to_portfolio(self, ticker, num_shares):
        self.__register_ticker(ticker)
        self.__portfolio[ticker] = num_shares

    def add_stock_price_history(self, stock_price_history):
        for stock_ticker in self.get_all_tickers():
            self.__register_ticker(stock_ticker)
        self.__stock_price_history = stock_price_history

    def set_portfolio_performance(self, expected_performance):
        self.__expected_performance = expected_performance


    # --------------------------------------------------------------------------
    # Getters - All stock data
    # --------------------------------------------------------------------------

    def get_all_tickers(self):
        return list(self.__ticker_set)

    def get_portfolio(self):
        return self.__portfolio

    def get_all_price_history(self):
        return self.__stock_price_history

    def get_expected_performance(self):
        return self.__expected_performance


    # --------------------------------------------------------------------------
    # Getters - Individual stock data
    # --------------------------------------------------------------------------

    def get_stock_num_shares(self, ticker):
        return self.__portfolio.get(ticker, None)

    def get_stock_price_history(self, ticker):
        return self.__stock_price_history.get(ticker, None)


    # --------------------------------------------------------------------------
    # Helper functions
    # --------------------------------------------------------------------------

    def __register_ticker(self, ticker):
        self.__ticker_set.add(ticker)

    def __deregister_ticker(self, ticker):
        self.__ticker_set.remove(ticker)
