class EfficientFrontierPerformance:

    def __init__(self, expected_annual_return, annual_volatility, sharpe_ratio):
        self.__performance_data = {
            "Expected annual return": expected_annual_return,
            "Annual volatility": annual_volatility,
            "Sharpe Ratio": sharpe_ratio
        }

    def get_performance_data(self):
        return self.__performance_data

    def get_string(self):
        return f"%s: %f0.2\%  %s: %f0.2\%  %s: %f0.2".format("Expected annual return", self.__performance_data["Expected annual return"],
                                "Annual volatility", self.__performance_data["Annual volatility"],
                                "Sharpe Ratio", self.__performance_data["Sharpe Ratio"])

        # out_string = ""
        # for key, value in self.__performance_data.items():
        #     out_string += "  " + key + ": " + str(value)
        # return out_string
