import matplotlib.pyplot as plt

from python.src.main.portfoliobuilder.EfficientFrontierPerformance import EfficientFrontierPerformance

plt.style.use('fivethirtyeight')
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


class EfficientFrontierPortfolioBuilderTool:


    def __init__(self, debug_level=0):
        self.__debug_level = debug_level


    # generate_portfolio(starting_investment, pd.read_csv('Resources/Real_State_Stocks_Update.csv'))
    def compute_portfolio(self, customer_metrics, stock_info_container):

        if customer_metrics.get_initial_investment() <= 0:
            return ""

        # TODO Integrate all customer_metrics

        # def generate_portfolio(starting_investment, stock_price_history):
        # Reset the date as the index
        # stock_price_history = stock_price_history.set_index(pd.DatetimeIndex(stock_price_history['Date'].values))

        stock_price_history = stock_info_container.get_all_price_history()

        # Clean up data
        # stock_price_history.dropna(axis=1, inplace=True)

        # Optimize the portfolio
        # Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
        mu = expected_returns.mean_historical_return(stock_price_history)
        S = risk_models.sample_cov(stock_price_history)

        # Optimize for the maximal Sharpe ratio
        ef = EfficientFrontier(mu, S)  # Creates the Efficient Frontier Object
        weights = ef.max_sharpe()
        cleaned_weights = ef.clean_weights()

        # Get expected performance
        expected_performance_tuple = ef.portfolio_performance(verbose=True)
        expected_performance = EfficientFrontierPerformance(expected_performance_tuple[0], expected_performance_tuple[1], expected_performance_tuple[2])

        # Get the descret allocation of each share per stock
        latest_prices = get_latest_prices(stock_price_history)
        da = DiscreteAllocation(cleaned_weights, latest_prices, total_portfolio_value=customer_metrics.get_initial_investment())
        allocation, leftover = da.lp_portfolio()

        # Store in StockInfoContainer
        stock_info_container.add_portfolio_to_portfolio(allocation)
        stock_info_container.set_portfolio_performance(expected_performance)

        return stock_info_container


    # --------------------------------------------------------------------------
    # Helper functions
    # --------------------------------------------------------------------------
