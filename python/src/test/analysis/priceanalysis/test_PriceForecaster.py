from unittest import TestCase
from main.analysis.priceanalysis.PriceForecaster import PriceForecaster
from test.lib.test.TestDataBuilder import TestDataBuilder


class TestPriceForecaster(TestCase):

    def test_inheritence(self):
        price_forecaster = PriceForecaster()
        self.assertEqual("PriceForecasting", price_forecaster.get_const_analysis_method_str())

    def test_price_forecaster_analyze(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        stock_info_container = test_data_builder.build_container_price_history()

        # Run the function
        price_forecaster = PriceForecaster()
        price_forecaster.analyze(stock_info_container)

        # Assertions
        score_aapl = stock_info_container.get_stock_raw_score_list("AAPL")[0]
        score_bngo = stock_info_container.get_stock_raw_score_list("BNGO")[0]
        score_ciic = stock_info_container.get_stock_raw_score_list("CIIC")[0]

        self.assertTrue(score_aapl.get_score() != 0)
        self.assertTrue(score_bngo.get_score() != 0)
        self.assertTrue(score_ciic.get_score() != 0)

        self.assertEqual("PriceForecasting.ARMA", score_aapl.get_analysis_source())
        self.assertEqual("PriceForecasting.ARMA", score_bngo.get_analysis_source())
        self.assertEqual("PriceForecasting.ARMA", score_ciic.get_analysis_source())
