from main.analysis.valuation.ValuationCalculator import ValuationCalculator
from unittest import TestCase

from test.lib.test.CustomTestObject import CustomTestObject
from test.lib.test.TestDataBuilder import TestDataBuilder

class TestValuationCalculator(TestCase):


    def test_inheritence(self):
        valuation_calculator = ValuationCalculator()
        self.assertEqual("Valuation", valuation_calculator.get_const_analysis_method_str())


    def test_valuation_calculator_analyze(self):

        # Build test data
        test_helper = TestDataBuilder()
        stock_info_container = test_helper.build_container_financial_metadata()
        stock_info_container = test_helper.build_container_price_history(stock_info_container)

        # Run the function
        valuation_calculator = ValuationCalculator()
        valuation_calculator.analyze(stock_info_container)

        # Assertions
        all_tickers = stock_info_container.get_all_tickers()
        self.assertEqual(3, len(all_tickers))

        score_aapl = stock_info_container.get_stock_raw_score_list("AAPL")[0]
        score_bngo = stock_info_container.get_stock_raw_score_list("BNGO")[0]
        score_ciic = stock_info_container.get_stock_raw_score_list("CIIC")[0]

        self.assertTrue(score_aapl.get_score() != 0)
        self.assertTrue(score_bngo.get_score() != 0)
        self.assertTrue(score_ciic.get_score() != 0)

        self.assertEqual("Valuation.DCF", score_aapl.get_analysis_source())
        self.assertEqual("Valuation.DCF", score_bngo.get_analysis_source())
        self.assertEqual("Valuation.DCF", score_ciic.get_analysis_source())


    # --------------------------------------------------------------------------
    # Dividend Discount Model
    # --------------------------------------------------------------------------


    def test_compute_value__dividend_discount_model(self):
        CustomTestObject().failNotImplemented()


    # --------------------------------------------------------------------------
    # Market Relative Model
    # --------------------------------------------------------------------------

    def test_compute_value__equity_value(self):
        CustomTestObject().failNotImplemented()


    def test_compute_market_value(self):
        CustomTestObject().failNotImplemented()


    # --------------------------------------------------------------------------
    # DCF Model
    # --------------------------------------------------------------------------


    def test_compute_cost_of_equity(self):
        CustomTestObject().failNotImplemented()


    def test_compute_wacc(self):
        CustomTestObject().failNotImplemented()


    def test_compute_value__dcf(self):
        valuation_calculator = ValuationCalculator()
        npv_actual = valuation_calculator.compute_value__dcf(
            ebitda_projection=[-645000.00, 189430.00, 183115.00, 187266.00, 191375.00, 195432.00, 199427.00,
                               203348.00, 207184.00, 210923.00, 214550.00],
            wacc=0.08)
        npv_expected = 621178.98
        self.assertAlmostEqual(npv_expected, npv_actual, 1)
