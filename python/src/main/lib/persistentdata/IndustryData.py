import os
from pathlib import Path

from python.src.main.lib.persistentdata.CSVDataLoader import CSVDataLoader


class IndustryData(CSVDataLoader):

    def __init__(self):

        self.__this_file_path = os.path.dirname(os.path.realpath(__file__))

        # Initialize industry list
        relative_csv_file_path = Path("data/industry_list.csv")
        super().__init__(relative_csv_file_path, self.__this_file_path)

        # Initialize additional industry data
        self.__initialize_industry_price_history()
        self.__initialize_industry_multiples()
        self.__initialize_industry_performance_metrics()


    def get_industry_list(self):
        return self.__data.keys().as_list()


    def __initialize_industry_price_history(self):
        self.industry_price_history__Communication_Services = CSVDataLoader("data/industry_price_history/Communication_Services.csv", self.__this_file_path).get_data()
        self.industry_price_history__Consumer_Discretionary = CSVDataLoader("data/industry_price_history/Consumer_Discretionary.csv", self.__this_file_path).get_data()
        self.industry_price_history__Consumer_Staples = CSVDataLoader("data/industry_price_history/Consumer_Staples.csv", self.__this_file_path).get_data()
        self.industry_price_history__Energy = CSVDataLoader("data/industry_price_history/Energy.csv", self.__this_file_path).get_data()
        self.industry_price_history__Financials = CSVDataLoader("data/industry_price_history/Financials.csv", self.__this_file_path).get_data()
        self.industry_price_history__Health_Care = CSVDataLoader("data/industry_price_history/Health_Care.csv", self.__this_file_path).get_data()
        self.industry_price_history__Industrial = CSVDataLoader("data/industry_price_history/Industrial.csv", self.__this_file_path).get_data()
        self.industry_price_history__Information_Technology = CSVDataLoader("data/industry_price_history/Information_Technology.csv", self.__this_file_path).get_data()
        self.industry_price_history__KEY = CSVDataLoader("data/industry_price_history/KEY.csv", self.__this_file_path).get_data()
        self.industry_price_history__Materials = CSVDataLoader("data/industry_price_history/Materials.csv", self.__this_file_path).get_data()
        self.industry_price_history__Real_State_Stocks_Update = CSVDataLoader("data/industry_price_history/Real_State_Stocks_Update.csv", self.__this_file_path).get_data()
        self.industry_price_history__Utilities = CSVDataLoader("data/industry_price_history/Utilities.csv", self.__this_file_path).get_data()


    def __initialize_industry_multiples(self):
        self.industry_multiples = CSVDataLoader("data/industry_multiples.csv", self.__this_file_path).get_data()


    def __initialize_industry_performance_metrics(self):
        self.industry_performance_data = CSVDataLoader("data/industry_performance_metrics.csv", self.__this_file_path).get_data()
