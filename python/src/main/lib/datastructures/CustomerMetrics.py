class CustomerMetrics:

    def __init__(self, risk, initial_investment, industries_preferences, investing_duration):
        self.__risk = risk
        self.__initial_investment = initial_investment
        self.__industries_preferences = industries_preferences
        self.__investing_duration = investing_duration

    def get_risk(self):
        return self.__risk

    def get_initial_investment(self):
        return self.__initial_investment

    def get_industries_preferences(self):
        return self.__industries_preferences

    def get_investing_duration(self):
        return self.__investing_duration
