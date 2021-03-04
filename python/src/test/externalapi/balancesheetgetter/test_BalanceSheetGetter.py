from unittest import TestCase
from main.lib.datastructures.StockInfoContainer import StockInfoContainer
from main.externalapi.balancesheetgetter.BalanceSheetGetter import BalanceSheetGetter


class TestBalanceSheetGetter(TestCase):

    def test_load_financial_info(self):

        # Build test data
        container = StockInfoContainer()
        stock_ticker_list = ["AAPL", "BNGO"]
        container.add_ticker_list(stock_ticker_list)  # TODO Ensure MSFT, TSLA and other large stocks work...

        # Execute financial data loader
        balance_sheet_getter = BalanceSheetGetter()
        balance_sheet_getter.load_financial_info(container)

        # Assertions
        actual_financial_metadata = container.get_stock_financial_metadata("AAPL")
        actual_financial_metadata_datamap = actual_financial_metadata.get_latest()
        self.assertIsNotNone(actual_financial_metadata_datamap["incometaxreconciliationtaxcreditsresearch"])
        actual_financial_metadata = container.get_stock_financial_metadata("BNGO")
        actual_financial_metadata_datamap = actual_financial_metadata.get_latest()
        self.assertIsNotNone(actual_financial_metadata_datamap["netincomeloss"])
