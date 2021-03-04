class AnalysisMethod:


    def __init__(self, analysis_method_name):
        # Constants
        self.__const_analysis_method = analysis_method_name


    def get_const_analysis_method_str(self):
        return self.__const_analysis_method


    def analyze(self, stock_info_container):
        raise NotImplementedError
