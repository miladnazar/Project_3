class EfficientFrontierPerformance:

    def __init__(self, expected_annual_return, annual_volatility, sharpe_ratio):
        self.__performance_data = {
            "Expected annual return": expected_annual_return,
            "Annual volatility": annual_volatility,
            "Sharpe Ratio": sharpe_ratio
        }

    def get_performance_data(self):
        return self.__performance_data
