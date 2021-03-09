import os
from pathlib import Path

from python.src.main.lib.persistentdata.CSVDataLoader import CSVDataLoader


class IndustryData(CSVDataLoader):

    def __init__(self):

        self.__this_file_path = os.path.dirname(os.path.realpath(__file__))

        # Initialize industry list
        relative_csv_file_path = Path("data/industry_list.csv")
        super().__init__(relative_csv_file_path, self.__this_file_path, False)

        # Initialize private members
        self.__industry_list = None
        self.__industry_price_history = None
        self.__industry_multiples = None
        self.__industry_performance_metrics = None

        # Initialize additional industry data
        self.__initialize_industry_price_history()
        self.__initialize_industry_multiples()
        self.__initialize_industry_performance_metrics()


    # --------------------------------------------------------------------------
    # Accessors
    # --------------------------------------------------------------------------


    def get_industry_list(self):
        # Transform and cache
        if self.__industry_list is None:
            self.__industry_list = self.get_data_as_dict().keys().as_list()
        return self.__industry_list


    def get_industry_price_history(self):
        return self.__industry_price_history


    def get_industry_multiples(self):
        return self.__industry_multiples


    def get_industry_performance_metrics(self):
        return self.__industry_performance_metrics


    # --------------------------------------------------------------------------
    # Initialization Functions
    # --------------------------------------------------------------------------


    def __initialize_industry_price_history(self):
        self.__industry_price_history = {}
        self.__industry_price_history["Communication_Services"] = CSVDataLoader("data/industry_price_history/Communication_Services.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Consumer_Discretionary"] = CSVDataLoader("data/industry_price_history/Consumer_Discretionary.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Consumer_Staples"] = CSVDataLoader("data/industry_price_history/Consumer_Staples.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Energy"] = CSVDataLoader("data/industry_price_history/Energy.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Financials"] = CSVDataLoader("data/industry_price_history/Financials.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Health_Care"] = CSVDataLoader("data/industry_price_history/Health_Care.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Industrial"] = CSVDataLoader("data/industry_price_history/Industrial.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Information_Technology"] = CSVDataLoader("data/industry_price_history/Information_Technology.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["KEY"] = CSVDataLoader("data/industry_price_history/KEY.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Materials"] = CSVDataLoader("data/industry_price_history/Materials.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Real_State_Stocks_Update"] = CSVDataLoader("data/industry_price_history/Real_State_Stocks_Update.csv", self.__this_file_path, True).get_data_as_dataframe()
        self.__industry_price_history["Utilities"] = CSVDataLoader("data/industry_price_history/Utilities.csv", self.__this_file_path, True).get_data_as_dataframe()


    def __initialize_industry_multiples(self):
        self.__industry_multiples = CSVDataLoader("data/industry_multiples.csv", self.__this_file_path, False).get_data_as_dict()


    def __initialize_industry_performance_metrics(self):
        self.__industry_performance_metrics = CSVDataLoader("data/industry_performance_metrics.csv", self.__this_file_path, True).get_data_as_dataframe()
