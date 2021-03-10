from python.src.main.portfoliobuilder.EfficientFrontierPortfolioBuilderTool import EfficientFrontierPortfolioBuilderTool


class PortfolioBuilderProject3:


    def __init__(self, debug_level=0):
        self.__debug_level = debug_level
        self.__efficient_frontier_portfolio_builder_tool = EfficientFrontierPortfolioBuilderTool()


    # --------------------------------------------------------------------------
    # Portfolio building functions
    # --------------------------------------------------------------------------


    def build_suggested_portfolio(self, customer_metrics, stock_info_container):
        """
        Construct a suggested portfolio.

        :param customer_metrics: CustomerMetrics instance containing high-level portfolio design requirements from the customer.
        :param stock_info_container: StockInfoContainer containing stocks with associated score.
        :return:
        """

        # Run the efficient frontier algorithm
        self.__efficient_frontier_portfolio_builder_tool.compute_portfolio(customer_metrics, stock_info_container)
        return stock_info_container


    def transform_portfolio_to_str(self, portfolio, expected_performance=None):

        # Transform to string representation
        portfolio_str = ""
        i = 0
        for (stock_ticker, num_shares) in portfolio.items():
            if i > 0:
                portfolio_str += " - "
            portfolio_str += f"{stock_ticker} ({num_shares})"
            i += 1

        if not (expected_performance is None):
            portfolio_str += "  --" + expected_performance.get_string()

        return portfolio_str
