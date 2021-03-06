import pandas as pd

class CSVDataTool:
    """
    CSV utility functions.
    """

    def load_csv_data(self, csv_file_path):
        dataframe = pd.read_csv(csv_file_path)
        return dataframe.to_dict()
