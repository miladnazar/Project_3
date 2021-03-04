from pathlib import Path
import pandas as pd
import numpy as np

class StockFinancialMetadata:


    def __init__(self, stock_ticker, data_list_map):
        """
        Construct the financial metadata data structure for one stock.
        Example: https://fmpcloud.io/api/v3/financial-statement-full-as-reported/AAPL?apikey=demo
        :param data_list_map: A list of financial mnetadata maps.
        """
        self.__stock_ticker = stock_ticker

        # List of historical financial data maps:  [ { financial_data_field -> financial_data_value } ]
        self.__data_list_map = data_list_map

        # Stock industries mapping
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.__stock_industries_filepath = os.path.join(dir_path, Path("data/stock_industries.csv"))
        self.__stock_industry_dictionary = self.__load_stock_industries(self.__stock_industries_filepath)


    def get_stock_ticker(self):
        return self.__stock_ticker


    def get_all_data(self):
        return self.__data_list_map


    def get_latest(self):
        return self.__data_list_map[0]


    def get_industry(self):
        # return self.__stock_industry_dictionary[self.__stock_ticker]
        return "Technology"  # TODO


    def get_assets(self):
        return None


    def get_liabilities(self):
        return None


    def get_ebidtaba(self):
        return None


    def combine_data_list_map(self, other):

        this_size = len(self.__data_list_map)
        other_size = len(other.__data_list_map)

        for i in range(0, other_size):
            other_data_map = other.__data_list_map[i]

            # Shortcut for new list entry
            if i >= this_size:
                self.__data_list_map.append(other_data_map)
                continue

            # Destructively combine the maps (TODO does not maintain data integrity)
            for key, value in other_data_map.items():
                self.__data_list_map[i][key] = value

        return self


    # --------------------------------------------------------------------------
    # Helpers
    # --------------------------------------------------------------------------


    # TODO fix dictionary to map symbol to industry
    @staticmethod
    def __load_stock_industries(stock_industries_filepath):
        stock_industries_df = pd.read_csv(stock_industries_filepath)
        return stock_industries_df.to_dict()
