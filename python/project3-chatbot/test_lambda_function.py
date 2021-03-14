from unittest import TestCase
from lambda_function import *


class TestLambdaFunction(TestCase):


    # Test the portfolio builder using CSV input data for one only
    def test_get_recommended_portfolio__csv_data__oneindustry(self):
        portfolio_actual = get_recommended_portfolio(
            "Medium", 500000,
            [ "Consumer_Staples" ],
            3,
            ticker_type="Industries", use_test_data=False, use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
        expected_portfolio_regex = r".*Consumer_Staples.*"
        self.assertRegex(portfolio_actual, expected_portfolio_regex)


    # Test the portfolio builder using CSV input data for two only
    def test_get_recommended_portfolio__csv_data__twoindustries(self):
        portfolio_actual = get_recommended_portfolio(
            "Medium", 500000,
            [ "Communication_Services", "Consumer_Discretionary" ],
            3,
            ticker_type="Industries", use_test_data=False, use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)
        expected_portfolio_regex = r".*Communication_Services.*Consumer_Discretionary.*"
        self.assertRegex(portfolio_actual, expected_portfolio_regex)


    # Test the portfolio builder using CSV input data for all industries
    def test_get_recommended_portfolio__csv_data__allindustries(self):
        portfolio_actual = get_recommended_portfolio(
            risk="Medium", initial_investment=500000, industries_preferences=[], investing_duration=3,
            ticker_type="Industries",
            use_test_data=False,
            use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertNotEqual("", portfolio_actual)


    # Test the portfolio builder using CSV input data for all industries
    def test_get_recommended_portfolio__csv_data__allindustries__notenoughcapital1(self):
        portfolio_actual = get_recommended_portfolio(
            risk="Medium", initial_investment=0, industries_preferences=[], investing_duration=3,
            ticker_type="Industries",
            use_test_data=False,
            use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertEqual("", portfolio_actual)


    # Test the portfolio builder using CSV input data for all industries
    def test_get_recommended_portfolio__csv_data__allindustries__notenoughcapital2(self):
        portfolio_actual = get_recommended_portfolio(
            risk="Medium", initial_investment=1, industries_preferences=[], investing_duration=3,
            ticker_type="Industries",
            use_test_data=False,
            use_csv_input_data=True)
        print(portfolio_actual)
        self.assertIsNotNone(portfolio_actual)
        self.assertEqual("", portfolio_actual)
