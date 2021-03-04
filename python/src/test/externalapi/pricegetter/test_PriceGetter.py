from unittest import TestCase
from main.externalapi.pricegetter import PriceGetter
from main.lib.datastructures.StockInfoContainer import StockInfoContainer

class TestPriceGetter(TestCase):


    def test_get_tickers(self):
        price_getter = PriceGetter()
        ticker_list = price_getter.get_tickers()
        self.assertTrue(len(ticker_list) > 50)


    def test_get_prices(self):
        price_getter = PriceGetter()
        container = StockInfoContainer()
        container.add_ticker_list(["AAPL", "BNGO", "CIIC"])
        price_getter.get_prices(container, trailing_n_days=100)
        stock_prices = container.get_all_price_history()
        self.assertTrue("AAPL" in set(stock_prices.columns))
        self.assertTrue("BNGO" in set(stock_prices.columns))
        self.assertTrue("CIIC" in set(stock_prices.columns))
        self.assertGreater(60, stock_prices.shape[1])
