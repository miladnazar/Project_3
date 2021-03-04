import numpy as np


class PortfolioBuilderTool:


    def __init__(self, debug_level=0):
        self.__debug_level = debug_level
        self.__weighting = {
            "PriceForecasting.ARMA": 10.0,
            "PriceForecasting.ARIMA": 10.0,
            "Valuation.DividendDiscountModel": 0.5,
            "Valuation.DCF": 0.00001,
            "Valuation.CapRateMarketModel": 0.5,
            "Valuation.MarketValue": 0.5
        }


    def compute_composite_scores(self, customer_metrics, stock_info_container):

        # Number of raw scores used to compute composite
        portfolio_composite_score_counts = {}

        # Sum the weighted scores
        for stock_score in stock_info_container.get_all_raw_scores_single_level():

            stock_ticker = stock_score.get_ticker()
            raw_score = stock_score.get_score()
            analysis_source = stock_score.get_analysis_source()
            w = self.__get_weighting(analysis_source)

            # Initialize dictionaries
            if stock_info_container.get_stock_composite_score(stock_ticker) is None:
                stock_info_container.add_stock_composite_score(stock_ticker, 0.0)
            if not (stock_ticker in portfolio_composite_score_counts):
                portfolio_composite_score_counts[stock_ticker] = 0

            # Add scores
            current_composite_score = stock_info_container.get_stock_composite_score(stock_ticker).get_score()
            new_score = current_composite_score + w * raw_score
            stock_info_container.add_stock_composite_score(stock_ticker, new_score)
            portfolio_composite_score_counts[stock_ticker] += 1

        # Average over the number of analysis methods
        for composite_score in stock_info_container.get_all_composite_scores_single_level():
            stock_ticker = composite_score.get_ticker()
            current_composite_score = composite_score.get_score()
            new_score = current_composite_score / portfolio_composite_score_counts[stock_ticker]
            stock_info_container.add_stock_composite_score(stock_ticker, new_score)

        return stock_info_container


    def compute_shares(self, customer_metrics, stock_score_list, stock_info_container):

        total_nbr_shares = 400  #customer_metrics.investmentAmount

        # Compute total score
        total_score = 0.0
        for stock_score in stock_score_list:
            total_score += stock_score.get_score()

        # Scale shares proportionally   #TODO this is wrong bc it does not take money into account
        for stock_score in stock_score_list:
            num_shares = np.floor(total_nbr_shares * stock_score.get_score() / total_score)
            stock_info_container.add_stock_to_portfolio(stock_score.get_ticker(), num_shares)

        return stock_info_container


    def sort_stock_score_list(self, stock_info_container):

        def score_sort(stock_score):
            return stock_score.get_score()

        score_list = stock_info_container.get_all_composite_scores_single_level()
        score_list.sort(reverse=True, key=score_sort)
        return score_list


    # --------------------------------------------------------------------------
    # Helpers
    # --------------------------------------------------------------------------


    def __get_weighting(self, analysis_source):
        if analysis_source in self.__weighting:
            return self.__weighting[analysis_source]
        else:
            return 1.0
