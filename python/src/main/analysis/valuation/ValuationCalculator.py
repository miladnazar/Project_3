import numpy as np
import random
from main.lib.datastructures.AnalysisMethod import AnalysisMethod


class IndustryInfo:

    def __init__(self, has_dividend, use_dcf, use_cap_rate_market_model, sum_of_the_parts_SoTP, comparables):
        self.has_dividend = has_dividend
        self.use_dcf = use_dcf
        self.use_cap_rate_market_model = use_cap_rate_market_model
        self.sum_of_the_parts_SoTP = sum_of_the_parts_SoTP
        self.comparables = comparables


class ValuationCalculator(AnalysisMethod):

    def __init__(self, debug_level=0):
        super().__init__("Valuation")
        self.__debug_level = 0
        # Source: https://www.valentiam.com/newsandinsights/ebitda-multiples-by-industry
        self.__industry_multiples = {
            "Healthcare information and technology": 24.81,
            "Airlines": 8.16,
            "Drugs, biotechnology": 13.29,
            "Hotels and casinos": 12.74,
            "Retail, general": 12.21,
            "Retail, food": 8.93,
            "Utilities, excluding water": 14.13,
            "Homebuilding": 10.95,
            "Medical equipment and supplies": 22.67,
            "Oil and gas, exploration and production": 4.89,
            "Telecom, equipment (phones & handheld devices)": 13.42,
            "Professional information services (big data)": 26.35,
            "Software, system & application": 24.00,
            "Wireless telecommunications services": 6.64
        }
        self.__industry_info = {
            "Consumer Discretionary":           IndustryInfo(False, True,  False, True,  True),
            "Consumer Staples":                 IndustryInfo(False, True,  False, True,  True),
            "Energy":                           IndustryInfo(False, True,  False, True,  False),
            "Financials":                       IndustryInfo(False, True,  False, False, True),
            "Health Care":                      IndustryInfo(False, True,  False, True,  False),
            "Industrials":                      IndustryInfo(False, True,  False, True,  False),
            "Information Technology":           IndustryInfo(False, True,  False, False, True),
            "Materials":                        IndustryInfo(False, True,  False, False, True),
            "Telecommunication Services":       IndustryInfo(False, True,  False, False, True),
            "Utilities":                        IndustryInfo(False, True,  False, False, False),
            "Real Estate Investment Trust":     IndustryInfo(True,  True,  True,  True,  False)
        }
        # Constants
        self.__const_analysis_method = "Valuation"


    def analyze(self, stock_info_container):

        # Grab price history data
        stock_price_history = stock_info_container.get_all_price_history()

        # Drive analysis by stock info container's ticker list
        for stock_ticker in stock_info_container.get_all_tickers():

            # Select valuation method
            stock_financial_metadata = stock_info_container.get_stock_financial_metadata(stock_ticker)
            analysis_submethod = self.__select_analysis_submethod(stock_financial_metadata)

            # Compute valuation and grab current price
            valuation = self.__compute_valuation(stock_financial_metadata, analysis_submethod)
            current_price = stock_price_history[stock_ticker].tail(1).iloc[0]

            # Compute score based on valuation and current price
            score = self.__compute_score(current_price, valuation)
            stock_info_container.add_stock_raw_score(stock_ticker, score, self.__const_analysis_method + "." + analysis_submethod)

        return stock_info_container


    def __select_analysis_submethod(self, stock_financial_metadata):
        industry = stock_financial_metadata.get_industry()
        if self.__industry_info[industry].has_dividend:
            return "DividendDiscountModel"
        elif self.__industry_info[industry].use_dcf:
            return "DCF"
        elif self.__industry_info[industry].use_cap_rate_market_model:  # Need cap rate; prefer real estate industry
            return "CapRateMarketModel"
        else:
            return "MarketValue"


    def __compute_valuation(self, stock_financial_metadata, analysis_submethod):
        industry = stock_financial_metadata.get_industry()

        if "DividendDiscountModel" == analysis_submethod:
            ticker = None
            r = None
            g = None
            return self.compute_value__dividend_discount_model(ticker, r, g)

        elif "DCF" == analysis_submethod:
            ebitda_projection = [1e6, 1.2e6, 1.25e6]  # TODO
            beta = stock_financial_metadata.get_beta()
            cost_of_equity = self.compute_cost_of_equity(beta)
            wacc = self.compute_wacc(cost_of_equity,
                equity=stock_financial_metadata.get_total_stockholders_equity(),
                debt=stock_financial_metadata.get_total_debt(),
                cost_of_debt=cost_of_equity)
            return self.compute_value__dcf(ebitda_projection, wacc)

        elif "CapRateMarketModel" == analysis_submethod:  # Need cap rate; prefer real estate industry
            industry_multiples = None
            market_cap = None
            capitalization_rate = None
            return self.compute_value__cap_rate_market_model(industry_multiples, market_cap, capitalization_rate)

        else:
            equity_value = None
            expected_ebitda = None
            ebitda = None
            return self.compute_market_value(equity_value, expected_ebitda, ebitda)


    def __compute_score(self, current_price, valuation):
        return 100.0 * (valuation - current_price) / current_price


    # --------------------------------------------------------------------------
    # Dividend Discount Model
    # --------------------------------------------------------------------------


    # TODO Correlate industries to changing dividends
    # def compute_value__dividend_discount_model(self,
    #                                            ticker,
    #                                             current_dividend,  # paymentsofdividends (pctfraction per share)
    #                                             cost_of_equity_capital__r=1.0,  # Cost of equity capital == interest rate  # 1.0
    #                                             g,  # Growth rate == eps growth  # dividendsperShareGrowth
    #
    #                                             # dividend_yield_fractional, # Dividend yield
    #                                             # npv, # Net present value
    #                                             # wacc, # Weighted cost of capital
    #                                             # eps, # Earnings per share
    #                                             # market_cap,
    #    ):
    #     dividend_next_year = current_dividend
    #     net_present_value = dividend_next_year / (r - g)
    #     return net_present_value


    # --------------------------------------------------------------------------
    # Market Relative Model
    # --------------------------------------------------------------------------
    
    def equity_value(
        market_value_of_equity,
        market_value_of_debt,
        cash
    ):
        return market_value_of_equity + market_value_of_debt - cash


    # Enterprise-Based Approach
    def compute_market_value(
            self,
            equity_value,
            expected_ebitda,
            ebitda):
        return (equity_value)/(ebitda) * expected_ebitda


    # def compute_value__relative_valuation_market_model(self,
    #     industry,
    #     ebitda
    #     ):
    #     return ebitda * self.__industry_multiples[industry]

    
    # --------------------------------------------------------------------------
    # DCF Model
    # Assuming the dividend doesnt grow: price = (DIV_1)/(1+R) + (DIV_2)/(1+R)...
    # Assuming dividend is expected to grow: price = (DIV)/(R-g)
    # --------------------------------------------------------------------------
    

    def compute_cost_of_equity(self,
        beta,
        risk_free_rate=0.2,
        market_rate_of_return=0.8):
        """
        Computes the opportunity cost of owning a particular stock in comparison to holding a diversified position in a broad market index.

        :param beta: Stock price beta from financial data.
        :param risk_free_rate: Current interest rate.
            Available through Quandl (https://www.quandl.com/data/USTREASURY-US-Treasury?utm_campaign=&utm_content=api-for-interest-rate-data&utm_medium=organic&utm_source=google)
        :param market_rate_of_return: Fixed average market rate of return.

        :return: The effective opportunity cost of equity.
        """
        return risk_free_rate + beta * (market_rate_of_return - risk_free_rate)


    # def compute_cost_of_debt(self,
    #                          total_debt,
    # ):
    #     return (debt / (market_value_of_debt + equity)) * cost_of_debt * 1 - corporate_tax_rate


    def compute_wacc(self,
                     cost_of_equity,
                     equity,
                     debt,
                     cost_of_debt,
                     corporate_tax_rate=0.21):
        """
        Compute the weighted-average cost of capital.

        :param cost_of_equity: Cost of owning equity.
        :param equity: Equity held by the company (totalStockholdersEquity).
        :param debt: Total outstanding debt held by the company (totalDebt).
        :param cost_of_debt: Opportunity cost of owning debt.
        :param corporate_tax_rate: Corporate tax rate, fixed value obtained from the IRS website.

        :return: Weighted-average cost of capital.
        """
        wacc = cost_of_equity * ( cost_of_equity / (equity + debt) )
        wacc += (debt / (equity + debt)) * cost_of_debt * (1 - corporate_tax_rate)
        return wacc


    def compute_value__dcf(self,
        ebitda_projection,
        wacc):
        """
        Compute the stock valuation using the Discounted Cashflow (DCF) model.

        :param ebitda_projection: 5-year forward EBITDA projection as a list of double-precision values.
            TODO Enforce 5-years and use a moving average
        :param wacc: Weighted average cost of capital.
            In the DCF model, WACC is used as the effective discount rate.
        :param cashflow_multiple: TODO

        :return: Stock valuation using the Discounted Cashflow (DCF) model.
        """
        year_count = len(ebitda_projection)
        net_present_value = 0
        for y in range(0, year_count):
            ebitda = ebitda_projection[y]
            net_present_value += ebitda / (1 + wacc) ** (y+1)
        
        return net_present_value
