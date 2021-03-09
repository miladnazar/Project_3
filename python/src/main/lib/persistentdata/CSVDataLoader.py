import os
from python.src.main.lib.tools.CSVDataTool import CSVDataTool

class CSVDataLoader:

    def __init__(self, relative_csv_file_path, this_file_path):
        csv_data_tool = CSVDataTool()
        csv_file_path = os.path.join(this_file_path, relative_csv_file_path)
        self.__data_dataframe = csv_data_tool.load_csv_data_as_dataframe(csv_file_path, False)
        self.__data_dict = None

    def get_data_as_dataframe(self):
        return self.__data_dataframe

    def get_data_as_dict(self):
        # Transform and cache dictionary
        if self.__data_dict is None:
            self.__data_dict = self.__data_dataframe.to_dict()
        return self.__data_dict
