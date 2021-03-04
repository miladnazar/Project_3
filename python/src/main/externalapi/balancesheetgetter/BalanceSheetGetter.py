import json

import requests


class BalanceSheetGetter:


    def __init__(self, debug_level=0):
        self.__debug_level = 0

        # Fmp Cloud variables
        self.__fmp_cloud_key = 'd62b3ac01083146edd0acaa71d57074a'
        self.__data_url_list = [
            [ "https://fmpcloud.io/api/v3/income-statement/", "?limit=120&apikey=" ],
            [ "https://fmpcloud.io/api/v3/balance-sheet-statement/", "?limit=120&apikey=" ],
            [ "https://fmpcloud.io/api/v3/cash-flow-statement/", "?limit=120&apikey=" ],
            [ "https://fmpcloud.io/api/v3/income-statement-as-reported/", "?limit=10&apikey=" ],
            [ "https://fmpcloud.io/api/v3/balance-sheet-statement-as-reported/", "?limit=10&apikey=" ],
            [ "https://fmpcloud.io/api/v3/cash-flow-statement-as-reported/", "?limit=10&apikey=" ],
            [ "https://fmpcloud.io/api/v3/financial-statement-full-as-reported/", "?apikey=" ],
            [ "https://fmpcloud.io/api/v3/ratios/", "?limit=40&apikey=" ],
            [ "https://fmpcloud.io/api/v3/key-metrics/", "?limit=40&apikey=" ],
            [ "https://fmpcloud.io/api/v3/financial-growth/", "?limit=20&apikey=" ],
            [ "https://fmpcloud.io/api/v3/market-capitalization/", "?apikey=" ],
            [ "https://fmpcloud.io/api/v3/discounted-cash-flow/", "?apikey=" ]
        ]


    def load_financial_info(self, stock_info_container):

        for stock_ticker in stock_info_container.get_all_tickers():
            try:
                stock_financial_metadata_collection = {}
                for data_url in self.__data_url_list:
                    try:
                        url = data_url[0] + stock_ticker + data_url[1] + self.__fmp_cloud_key
                        stock_financial_metadata_str = requests.get(url)
                        stock_financial_metadata_json = json.loads(stock_financial_metadata_str.content)
                        stock_financial_metadata = self.__process_stock_financial_metadata_json(stock_financial_metadata_json)
                        stock_financial_metadata_collection = stock_financial_metadata_collection.combine_data_list_map(stock_financial_metadata)
                    except:
                        continue

                stock_info_container.add_stock_financial_metadata(stock_ticker, stock_financial_metadata_collection)
            except:
                continue

        return stock_info_container


    # --------------------------------------------------------------------------
    # Helpers
    # --------------------------------------------------------------------------


    def __process_stock_financial_metadata_json(self, stock_financial_metadata_json):

        # TODO Calculations and data aggregation?

        # marketCap
        # revenue
        # Gross_Profit_ratio
        # p_to_sales = MarketCapit / Revenue
        # price_to_sales

        #
        # price_to_sales_df['ps_average_sector'] = price_to_sales_df['price_to_sales'].mean()
        # price_to_sales_df['pscompany_vs_averagesector'] = price_to_sales_df['price_to_sales'] - price_to_sales_df[
        #     'ps_average_sector']
        # price_to_sales_df['price_as_per_average_industryPS'] = price_to_sales_df['ps_average_sector'] * \
        #                                                        price_to_sales_df['revenue']
        # price_to_sales_df['price_difference'] = price_to_sales_df['price_as_per_average_industryPS'] - \
        #                                         price_to_sales_df['Market_Capit']
        #

        # TODO Transform to dataframe? price_to_sales_df = pd.DataFrame.from_dict(financial_metadata, orient='index')

        return stock_financial_metadata_json
