class StockFilter:


    def __init__(self, debug_level=0):
        self.__debug_level = debug_level


    def filter(self, stock_info_container):

        # Remove items with invalid financial or price data
        for stock_ticker in stock_info_container.get_all_tickers():
            if not (self.__has_valid_financial_metadata(stock_ticker, stock_info_container) and self.__has_valid_price_data(stock_ticker, stock_info_container)):
                stock_info_container.remove_ticker(stock_ticker)

        return stock_info_container


    def __has_valid_financial_metadata(self, stock_ticker, stock_info_container):

        stock_financial_metadata = stock_info_container.get_stock_financial_metadata(stock_ticker)

        # Validate object and size
        if stock_financial_metadata is None or len(stock_financial_metadata) == 0:
            return False

        # All conditions met
        return True


    def __has_valid_price_data(self, stock_ticker, stock_info_container):

        stock_price_history = stock_info_container.get_stock_price_history(stock_ticker)

        # Validate price history object
        if stock_price_history is None:
            return False

        # Validate number of price data points
        if len(stock_price_history.shape) != 2 or stock_price_history.shape[1] < 5:
            return False

        # All conditions met
        return True
