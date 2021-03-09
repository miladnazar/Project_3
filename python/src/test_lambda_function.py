from unittest import TestCase
from lambda_function import *


class TestLambdaFunction(TestCase):



    # Test the portfolio builder using CSV input data for Technology only
    def test_get_recommended_portfolio__csv_data__technology(self):
        portfolio_actual = get_recommended_portfolio(
            "Medium", 5000,
            [ "Technology" ],
            3,
            ticker_type="Industries", use_test_data=False, use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
        expected_portfolio_regex = r"Technology \([0-9.-]+\)"
        self.assertRegex(portfolio_actual, expected_portfolio_regex)


    # Test the portfolio builder using CSV input data for all industries
    def test_get_recommended_portfolio__csv_data__allindustries(self):
        portfolio_actual = get_recommended_portfolio(
            risk="Medium", initial_investment=5000, industries_preferences=[], investing_duration=3,
            ticker_type="Industries",
            use_test_data=False,
            use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
