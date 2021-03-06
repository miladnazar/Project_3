import os
from python.src.main.lib.tools.CSVDataTool import CSVDataTool

class CSVDataLoader:

    def __init__(self, relative_csv_file_path, this_file_path):
        csv_data_tool = CSVDataTool()
        csv_file_path = os.path.join(this_file_path, relative_csv_file_path)
        self.__data = csv_data_tool.load_csv_data(csv_file_path)

    def get_data(self):
        return self.__data
