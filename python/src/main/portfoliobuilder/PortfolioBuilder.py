import numpy as np

from main.portfoliobuilder.PortfolioBuilderTool import PortfolioBuilderTool


class PortfolioBuilder:


    def __init__(self, debug_level=0):
        self.__debug_level = debug_level
        self.__portfolio_builder_tool = PortfolioBuilderTool()


    # --------------------------------------------------------------------------
    # Portfolio building functions
    # --------------------------------------------------------------------------


    def build_suggested_portfolio(self, customer_metrics, stock_info_container):
        """
        Construct a suggested portfolio based on scores assigned to stocks through various analysis techniques.

        :param customer_metrics: CustomerMetrics instance containing high-level portfolio design requirements from the customer.
        :param stock_info_container: StockInfoContainer containing stocks with associated score.
        :return:
        """

        # Compute composite score and sort
        self.__portfolio_builder_tool.compute_composite_scores(customer_metrics, stock_info_container)
        stock_score_list = self.__portfolio_builder_tool.sort_stock_score_list(stock_info_container)

        # Compute number of shares
        stock_info_container = self.__portfolio_builder_tool.compute_shares(customer_metrics, stock_score_list, stock_info_container)
        return stock_info_container


    def transform_portfolio_to_str(self, portfolio):

        # Transform to string representation
        portfolio_str = ""
        i = 0
        for (stock_ticker, num_shares) in portfolio.items():
            if i > 0:
                portfolio_str += " - "
            portfolio_str += f"{stock_ticker} ({num_shares})"
            i += 1

        return portfolio_str


    def add_hedge_positions(self, stock_info_container):
        # TODO
        return stock_info_container
