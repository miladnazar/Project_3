from unittest import TestCase
from test.lib.test.TestDataBuilder import TestDataBuilder
from main.stockfilter.StockFilter import StockFilter


class TestStockFilter(TestCase):


    def test_filter(self):
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_portfolio()
        stock_filter = StockFilter()
        stock_filter.filter(container)
        self.assertIsNotNone(stock_filter.filter(container))
