
class StockScore:

    def __init__(self, ticker, score, analysis_source):
        self.__ticker = ticker
        self.__score = score
        self.__analysis_source = analysis_source

    def get_ticker(self):
        return self.__ticker

    def get_score(self):
        return self.__score

    def get_analysis_source(self):
        return self.__analysis_source
