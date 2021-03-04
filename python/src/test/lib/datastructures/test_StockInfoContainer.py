from unittest import TestCase
from main.lib.datastructures.StockInfoContainer import StockInfoContainer
from test.lib.test.TestDataBuilder import TestDataBuilder


# NOTE: Fails unless run from this file due to reading data from relative directory.
class TestStockInfoContainer(TestCase):


    def test_add_ticker(self):

        # Build test data
        container = StockInfoContainer()
        container.add_ticker("AAPL")

        # Assertions and tests
        self.assertEqual("AAPL", container.get_all_tickers()[0])
        container.add_ticker("MSFT")
        container.add_ticker("TSLA")
        self.assertEqual(3, len(container.get_all_tickers()))
        container.add_ticker("AAPL")

        # Validate that the tickers were registered
        self.assertEqual(3, len(container.get_all_tickers()))


    def test_remove_ticker(self):

        # Build test data
        container = StockInfoContainer()
        container.add_ticker("AAPL")
        container.add_ticker("MSFT")
        container.add_ticker("TSLA")

        # Assertions and tests
        self.assertEqual(3, len(container.get_all_tickers()))
        container.remove_ticker("MSFT")
        self.assertEqual(2, len(container.get_all_tickers()))


    def test_add_ticker_list(self):

        # Build test data
        container = StockInfoContainer()
        container.add_ticker_list(["AAPL", "MSFT", "TSLA"])

        # Assertions
        all_tickers = container.get_all_tickers()
        expected_tickers = ["AAPL", "MSFT", "TSLA"]
        for ticker in expected_tickers:
            self.assertTrue(ticker in set(all_tickers))

        # Validate that the tickers were registered
        self.assertEqual(3, len(all_tickers))


    def test_add_stock_raw_score(self):

        # Build test data
        container = StockInfoContainer()
        container.add_stock_raw_score("AAPL", 0.8, "price analysis")

        # Assertions
        score_info_list = container.get_stock_raw_score_list("AAPL")
        self.assertEqual("price analysis", score_info_list[0].get_analysis_source())
        self.assertEqual(0.8, score_info_list[0].get_score())

        # Validate that the tickers were registered
        self.assertEqual(1, len(container.get_all_tickers()))


    def test_add_stock_composite_score(self):

        # Build test data
        container = StockInfoContainer()
        container.add_stock_composite_score("AAPL", 0.8)

        # Assertions
        score_info = container.get_stock_composite_score("AAPL")
        self.assertEqual("Composite", score_info.get_analysis_source())
        self.assertEqual(0.8, score_info.get_score())

        # Validate that the tickers were registered
        self.assertEqual(1, len(container.get_all_tickers()))


    def test_add_stock_to_portfolio(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_portfolio()

        # Assertions
        portfolio = container.get_portfolio()
        self.assertEqual(3, len(portfolio))
        self.assertEqual(102, portfolio["AAPL"])
        self.assertEqual(103, portfolio["MSFT"])
        self.assertEqual(104, portfolio["TSLA"])

        # Validate that the tickers were registered
        self.assertEqual(3, len(container.get_all_tickers()))


    def test_add_stock_price_history(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_index, expected_stock_price_history) = test_data_builder.build_stock_price_data()

        # Call add function
        container.add_stock_price_history(expected_stock_price_history)

        # Extract needed data for testing
        actual_stock_price_history__aapl = container.get_stock_price_history("AAPL")
        actual_stock_price_history__msft = container.get_stock_price_history("MSFT")
        actual_index = actual_stock_price_history__aapl.index

        # Perform assertions
        self.assertEqual(3, actual_stock_price_history__aapl.shape[0])
        self.assertEqual(3, actual_stock_price_history__msft.shape[0])
        self.assertEqual(expected_index[0], actual_index[0])
        self.assertEqual(expected_index[1], actual_index[1])
        self.assertEqual(expected_index[2], actual_index[2])
        self.assertEqual(expected_stock_price_history["AAPL"].values[0], actual_stock_price_history__aapl.values[0])
        self.assertEqual(expected_stock_price_history["AAPL"].values[1], actual_stock_price_history__aapl.values[1])
        self.assertEqual(expected_stock_price_history["AAPL"].values[2], actual_stock_price_history__aapl.values[2])
        self.assertEqual(expected_stock_price_history["MSFT"].values[0], actual_stock_price_history__msft.values[0])
        self.assertEqual(expected_stock_price_history["MSFT"].values[1], actual_stock_price_history__msft.values[1])
        self.assertEqual(expected_stock_price_history["MSFT"].values[2], actual_stock_price_history__msft.values[2])

        # Validate that the tickers were registered
        self.assertEqual(2, len(container.get_all_tickers()))


    def test_add_stock_financial_metadata(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_financial_metadata_listmap) = test_data_builder.build_financial_metadata()
        actual_financial_metadata = container.get_stock_financial_metadata("AAPL")
        actual_financial_metadata_datamap = actual_financial_metadata.get_latest()

        # Make assertions
        self.assertEqual(expected_financial_metadata_listmap[0]["numberofsignificantvendors"],
                         actual_financial_metadata_datamap["numberofsignificantvendors"])
        self.assertEqual(expected_financial_metadata_listmap[0]["currentstateandlocaltaxexpensebenefit"],
                         actual_financial_metadata_datamap["currentstateandlocaltaxexpensebenefit"])
        self.assertEqual(expected_financial_metadata_listmap[0]["investmentincomeinterestanddividend"],
                         actual_financial_metadata_datamap["investmentincomeinterestanddividend"])
        self.assertIsNone(container.get_stock_financial_metadata("MSFT"))

        # Validate that the tickers were registered
        self.assertEqual(1, len(container.get_all_tickers()))


    def test_get_all_tickers(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_portfolio()

        # Assertions
        all_tickers = container.get_all_tickers()
        self.assertEqual(3, len(all_tickers))
        expected_tickers = ["AAPL", "MSFT", "TSLA"]
        for ticker in expected_tickers:
            self.assertTrue(ticker in set(all_tickers))


    def test_get_all_raw_scores_single_level(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_raw_scores()

        # Assertions
        all_scores_single_level = container.get_all_raw_scores_single_level()
        expected_scores = {
            "AAPL": 0.8,
            "MSFT": 0.6,
            "TSLA": 0.4
        }
        expected_analysis_methods = {
            "AAPL": "price analysis",
            "MSFT": "valuation analysis",
            "TSLA": "other analysis"
        }
        self.assertEqual(3, len(all_scores_single_level))
        for actual_score_info in all_scores_single_level:
            ticker = actual_score_info.get_ticker()
            self.assertEqual(expected_analysis_methods[ticker], actual_score_info.get_analysis_source())
            self.assertEqual(expected_scores[ticker], actual_score_info.get_score())


    def test_get_all_composite_scores_single_level(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_composite_scores()

        # Assertions
        all_scores_single_level = container.get_all_composite_scores_single_level()
        expected_scores = {
            "AAPL": 0.8,
            "MSFT": 0.6,
            "TSLA": 0.4
        }
        self.assertEqual(3, len(all_scores_single_level))
        for actual_score_info in all_scores_single_level:
            ticker = actual_score_info.get_ticker()
            self.assertEqual("Composite", actual_score_info.get_analysis_source())
            self.assertEqual(expected_scores[ticker], actual_score_info.get_score())


    def test_get_portfolio(self):
        # Functionality tested in add() test
        self.test_add_stock_to_portfolio()


    def test_get_all_price_history(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_index, expected_stock_price_history) = test_data_builder.build_stock_price_data()

        # Call add function
        container.add_stock_price_history(expected_stock_price_history)

        # Extract needed data for testing
        all_price_history = container.get_all_price_history()
        actual_stock_price_history__aapl = all_price_history["AAPL"]
        actual_stock_price_history__msft = all_price_history["MSFT"]
        actual_index = actual_stock_price_history__aapl.index

        # Perform assertions
        self.assertEqual(3, actual_stock_price_history__aapl.shape[0])
        self.assertEqual(3, actual_stock_price_history__msft.shape[0])
        self.assertEqual(expected_index[0], actual_index[0])
        self.assertEqual(expected_index[1], actual_index[1])
        self.assertEqual(expected_index[2], actual_index[2])
        self.assertEqual(expected_stock_price_history["AAPL"].values[0], actual_stock_price_history__aapl.values[0])
        self.assertEqual(expected_stock_price_history["AAPL"].values[1], actual_stock_price_history__aapl.values[1])
        self.assertEqual(expected_stock_price_history["AAPL"].values[2], actual_stock_price_history__aapl.values[2])
        self.assertEqual(expected_stock_price_history["MSFT"].values[0], actual_stock_price_history__msft.values[0])
        self.assertEqual(expected_stock_price_history["MSFT"].values[1], actual_stock_price_history__msft.values[1])
        self.assertEqual(expected_stock_price_history["MSFT"].values[2], actual_stock_price_history__msft.values[2])


    def test_get_all_financial_metadata(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_financial_metadata) = test_data_builder.build_financial_metadata()
        actual_financial_metadata = container.get_all_financial_metadata()

        # Make assertions
        self.assertEqual(expected_financial_metadata[0]["numberofsignificantvendors"],
                         actual_financial_metadata["AAPL"].get_latest()["numberofsignificantvendors"])
        self.assertEqual(expected_financial_metadata[0]["currentstateandlocaltaxexpensebenefit"],
                         actual_financial_metadata["AAPL"].get_latest()["currentstateandlocaltaxexpensebenefit"])
        self.assertEqual(expected_financial_metadata[0]["investmentincomeinterestanddividend"],
                         actual_financial_metadata["AAPL"].get_latest()["investmentincomeinterestanddividend"])


    def test_get_stock_raw_scores(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_raw_scores()

        # Assertions
        score_info = container.get_stock_raw_score_list("AAPL")
        self.assertEqual("price analysis", score_info[0].get_analysis_source())
        self.assertEqual(0.8, score_info[0].get_score())


    def test_get_stock_composite_scores(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_composite_scores()

        # Assertions
        score_info = container.get_stock_composite_score("AAPL")
        self.assertEqual("Composite", score_info.get_analysis_source())
        self.assertEqual(0.8, score_info.get_score())


    def test_get_stock_num_shares(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        container = test_data_builder.build_simple_portfolio()

        # Assertions
        self.assertEqual(102, container.get_stock_num_shares("AAPL"))
        self.assertEqual(103, container.get_stock_num_shares("MSFT"))
        self.assertEqual(104, container.get_stock_num_shares("TSLA"))


    def test_get_stock_price_history(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_index, expected_stock_price_history) = test_data_builder.build_stock_price_data()

        # Call add function
        container.add_stock_price_history(expected_stock_price_history)

        # Extract needed data for testing
        actual_stock_price_history__aapl = container.get_stock_price_history("AAPL")
        actual_stock_price_history__msft = container.get_stock_price_history("MSFT")
        actual_index = actual_stock_price_history__aapl.index

        # Perform assertions
        self.assertEqual(3, actual_stock_price_history__aapl.shape[0])
        self.assertEqual(3, actual_stock_price_history__msft.shape[0])
        self.assertEqual(expected_index[0], actual_index[0])
        self.assertEqual(expected_index[1], actual_index[1])
        self.assertEqual(expected_index[2], actual_index[2])
        self.assertEqual(expected_stock_price_history["AAPL"].values[0], actual_stock_price_history__aapl.values[0])
        self.assertEqual(expected_stock_price_history["AAPL"].values[1], actual_stock_price_history__aapl.values[1])
        self.assertEqual(expected_stock_price_history["AAPL"].values[2], actual_stock_price_history__aapl.values[2])
        self.assertEqual(expected_stock_price_history["MSFT"].values[0], actual_stock_price_history__msft.values[0])
        self.assertEqual(expected_stock_price_history["MSFT"].values[1], actual_stock_price_history__msft.values[1])
        self.assertEqual(expected_stock_price_history["MSFT"].values[2], actual_stock_price_history__msft.values[2])


    def test_get_stock_financial_metadata(self):

        # Build test data
        test_data_builder = TestDataBuilder()
        (container, expected_financial_metadata) = test_data_builder.build_financial_metadata()

        # Assertions
        financial_metadata__aapl = container.get_stock_financial_metadata("AAPL")
        self.assertEqual(expected_financial_metadata[0]["numberofsignificantvendors"],
                         financial_metadata__aapl.get_latest()["numberofsignificantvendors"])
        self.assertEqual(expected_financial_metadata[0]["currentstateandlocaltaxexpensebenefit"],
                         financial_metadata__aapl.get_latest()["currentstateandlocaltaxexpensebenefit"])
        self.assertEqual(expected_financial_metadata[0]["investmentincomeinterestanddividend"],
                         financial_metadata__aapl.get_latest()["investmentincomeinterestanddividend"])

        self.assertIsNone(container.get_stock_financial_metadata("MSFT"))
