class CustomerMetrics:

    def __init__(self, investingDuration, investmentAmount, risk, investingExperience):
        self.__investing_duration = investingDuration
        self.__investment_amount = investmentAmount
        self.__risk = risk
        self.__investing_experience = investingExperience

    def get_investing_duration(self):
        return self.investing_duration

    def get_investment_amount(self):
        return self.investment_amount

    def get_risk(self):
        return self.risk

    def get_investing_experience(self):
        return self.investing_experience
