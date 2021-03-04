from unittest import TestCase


class TestPriceForecaster(TestCase):

    def add_two_numbers(self, x, y):
        return x * y



    def test_add_two_numbers(self):
        result = self.add_two_numbers(3, 4)
        self.assertEqual(7, result)



    # def test_compute_forecast_lstm(self):
    #     test_dataframe = .....
    #     compute_forecast_lstm(self, stock_info_container, stock_price_history)
    #     self.assertEqual(False)
