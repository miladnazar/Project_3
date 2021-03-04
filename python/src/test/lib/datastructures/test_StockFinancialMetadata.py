from unittest import TestCase
from main.lib.datastructures.StockFinancialMetadata import StockFinancialMetadata


class TestStockFinancialMetadata(TestCase):


    def test_combine_data_list_map(self):
        list_map_1 = self.__generate_data_list_map("AAPL", 0)
        list_map_2 = self.__generate_data_list_map("AAPL", 0)
        combined_list_map = list_map_1.combine_data_list_map(list_map_2)

        combined_list_map_data = combined_list_map.get_all_data()

        self.assertEqual(3, len(combined_list_map_data))
        self.assertEqual(4, len(combined_list_map_data[0]))

        self.__apply_assertion(combined_list_map_data, 0, [0, 0, 0])
        self.__apply_assertion(combined_list_map_data, 1, [1, 1, 1])
        self.__apply_assertion(combined_list_map_data, 2, [2, 2, 2])


    # --------------------------------------------------------------------------
    # Assertion Helpers
    # --------------------------------------------------------------------------


    def __apply_assertion(self, data_list_map, i, data_values):
        """
        Validate listmap contents.
        :param data_list_map: The listmap to be validated.
        :param i: List index.
        :param data_values: Values for all map fields.
        :return:
        """
        self.assertEqual(data_values[0], data_list_map[i]["field1"])
        self.assertEqual(data_values[1], data_list_map[i]["field2"])
        self.assertEqual(data_values[2], data_list_map[i]["field3"])


    # --------------------------------------------------------------------------
    # Generators
    # --------------------------------------------------------------------------


    def __generate_data_list_map(self, stock_ticker, offset):
        stock_financial_metadata = StockFinancialMetadata(stock_ticker, [
            self.__generate_data_map("12/31/2018", offset+0, offset+0, offset+0),
            self.__generate_data_map("12/31/2019", offset+1, offset+1, offset+1),
            self.__generate_data_map("12/31/2020", offset+2, offset+2, offset+2)
        ])
        return stock_financial_metadata


    def __generate_data_map(self, date, field1, field2, field3):
        return {
            "date": date,
            "field1": field1,
            "field2": field2,
            "field3": field3
       }
