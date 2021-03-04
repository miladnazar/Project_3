from unittest import TestCase
from main.lib.datastructures.StockFinancialMetadata import StockFinancialMetadata

class TestStockFinancialMetadata(TestCase):
    def test_get_industry(self):
        expected_metadata_list_map = {}
        metadata = StockFinancialMetadata("AAPL", expected_metadata_list_map)
        metadata.get_industry()
        self.fail()
