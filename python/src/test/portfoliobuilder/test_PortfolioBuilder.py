from unittest import TestCase
from main.portfoliobuilder.PortfolioBuilder import PortfolioBuilder
from main.lib.datastructures.StockInfoContainer import StockInfoContainer
from test.lib.test.TestDataBuilder import TestDataBuilder


class TestPortfolioBuilder(TestCase):


    # --------------------------------------------------------------------------
    # Interface Tests
    # --------------------------------------------------------------------------


    def test_build_suggested_portfolio(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        customer_metrics = test_data_builder.build_customer_metrics()
        stock_info_container = StockInfoContainer()
        self.__build_container(stock_info_container)

        # Run the function
        portfolio_builder = PortfolioBuilder()
        portfolio_builder.build_suggested_portfolio(customer_metrics, stock_info_container)

        # Composite score assertions
        composite_score_list = stock_info_container.get_all_composite_scores_single_level()
        self.assertEqual(3, len(composite_score_list))
        expected_composite_scores = {
            "AAPL": 0.45,
            "TSLA": 0.455,
            "BNGO": 0.15
        }
        for composite_score in composite_score_list:
            stock_ticker = composite_score.get_ticker()
            self.assertAlmostEqual(expected_composite_scores[stock_ticker], composite_score.get_score(), 3)

        # Portfolio length assertions
        self.assertEqual(3, len(stock_info_container.get_all_tickers()))
        portfolio = stock_info_container.get_portfolio()
        self.assertEqual(3, len(portfolio))

        # Portfolio value assertions
        self.assertIsNotNone(portfolio["AAPL"])
        self.assertIsNotNone(portfolio["TSLA"])
        self.assertIsNotNone(portfolio["BNGO"])

        self.assertGreater(portfolio["AAPL"], 0)
        self.assertGreater(portfolio["TSLA"], 0)
        self.assertGreater(portfolio["BNGO"], 0)


    def test_add_hedge_positions(self):
        self.fail()


    def test_transform_portfolio_to_str(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        customer_metrics = test_data_builder.build_customer_metrics()
        stock_info_container = StockInfoContainer()
        self.__build_container(stock_info_container)
        portfolio_builder = PortfolioBuilder()
        portfolio_builder.build_suggested_portfolio(customer_metrics, stock_info_container)

        # Run the function
        actual_portfolio_str = portfolio_builder.transform_portfolio_to_str(stock_info_container)
        expected_portfolio_regex = r"TSLA \([0-9.-]+\) - AAPL \([0-9.-]+\) - BNGO \([0-9.-]+\)"
        self.assertRegex(actual_portfolio_str, expected_portfolio_regex)
        # self.assertEqual(expected_portfolio_str, actual_portfolio_str)


    # --------------------------------------------------------------------------
    # Helpers
    # --------------------------------------------------------------------------


    def __build_container(self, container):
        container.add_stock_raw_score("AAPL", 0.95, "Price")
        container.add_stock_raw_score("TSLA", 0.98, "Price")
        container.add_stock_raw_score("AAPL", 0.85, "Valuation")
        container.add_stock_raw_score("TSLA", 0.84, "Valuation")
        container.add_stock_raw_score("BNGO", 0.30, "Price")


class TestPortfolioBuilderTool(TestCase):

    def test_compute_composite_scores(self):
        self.fail()


    def test_compute_shares(self):
        self.fail()

