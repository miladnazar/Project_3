from unittest import TestCase
from lambda_function import *


class TestLambdaFunction(TestCase):


    # Test the portfolio builder using test data
    def test_get_recommended_portfolio__test_data(self):
        portfolio_actual = get_recommended_portfolio("Long", 5000, "Medium", "Intermediate", use_test_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
        expected_portfolio_regex = r"AAPL \([0-9.-]+\) - TSLA \([0-9.-]+\) - MSFT \([0-9.-]+\)"
        self.assertRegex(portfolio_actual, expected_portfolio_regex)


    # Test the full-scale portfolio builder
    def test_get_recommended_portfolio__full(self):
        portfolio_actual = get_recommended_portfolio("Long", 5000, "Medium", "Intermediate", use_test_data=False)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
