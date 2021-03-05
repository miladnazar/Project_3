### Required Libraries ###


### Main Handler ###
from main.analysis.priceanalysis.PriceForecaster import PriceForecaster
from main.analysis.valuation.ValuationCalculator import ValuationCalculator
from main.externalapi.balancesheetgetter.BalanceSheetGetter import BalanceSheetGetter
from main.externalapi.pricegetter.PriceGetter import PriceGetter
from main.portfoliobuilder.PortfolioBuilder import PortfolioBuilder
from main.stockfilter.StockFilter import StockFilter

from python.src.main.externalapi.smart.Project3SmartContractTool import Project3SmartContractTool
from python.src.main.lib.datastructures.CustomerMetrics import CustomerMetrics
from python.src.main.lib.datastructures.StockInfoContainer import StockInfoContainer
from python.src.main.portfoliobuilder.PortfolioBuilderProject3 import PortfolioBuilderProject3


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "PortfolioBuilder_Project3":
        return get_recommended_portfolio_intent_handler(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Intents Handlers ###
def get_recommended_portfolio_intent_handler(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    risk = get_slots(intent_request)["risk"]
    initial_investment = get_slots(intent_request)["initial_investment"]
    industries_preferences = get_slots(intent_request)["industries_preferences"]
    investing_duration = get_slots(intent_request)["investing_duration"]
    contract_address = get_slots(intent_request)["contract_address"]

    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(initial_investment)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.

        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the initial investment recommendation
    recommended_portfolio = get_recommended_portfolio(risk, initial_investment, industries_preferences, investing_duration, use_test_data=True)

    TODO Use .csv files as static data

    # Send recommended portfolio to smart contract
    register_portfolio_recommendation_in_smartcontract(recommended_portfolio, contract_address)

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "Thank you for the information. Based on the inputs you provided, my recommendation is to invest the following portfolio: {}".format(
                recommended_portfolio
            ),
        },
    )


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Data Validation ###
def validate_data(investmentAmount):
    """
    Validates the data provided by the user.
    """

    # Handle default starting values - pass responsibility to the slots to retrieve values

    if investmentAmount is None:
        return build_validation_result(True, None, None)

    if investmentAmount is not None:

        # Validate investmentAmount

        # TODO Sanitize - remove "$"

        if float(investmentAmount) is None:
            return build_validation_result(
                False,
                "investmentAmount",
                "The investment amount must be a number. How much do you want to invest?",
            )

        investmentAmount = float(investmentAmount)

        if investmentAmount < 100:
            return build_validation_result(
                False,
                "investmentAmount",
                "The investment amount must be greater than or equal to $100. How much do you want to invest?",
            )

    # Success!
    return build_validation_result(True, None, None)


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def get_recommended_portfolio(risk, initial_investment, industries_preferences, investing_duration, use_test_data=False):

    # Construct helper objects
    price_getter = PriceGetter()
    portfolio_builder_project3 = PortfolioBuilderProject3()

    # Build data structures
    stock_info_container = StockInfoContainer()
    customer_metrics = CustomerMetrics(risk, initial_investment, industries_preferences, investing_duration)

    # Retrieve stock list
    try:
        stock_ticker_list = price_getter.get_tickers(use_test_data=True)
        stock_info_container.add_ticker_list(stock_ticker_list)
    except:
        return "EXCEPTION in: Retrieve stock list"

    # Retrieve price histories
    try:
        price_getter.get_prices(stock_info_container, trailing_n_days=100)
    except:
        return "EXCEPTION in: Retrieve price histories"

    # Call portfolio builder
    try:
        portfolio_builder_project3.build_suggested_portfolio(customer_metrics, stock_info_container)
    except:
        return "EXCEPTION in: Call portfolio builder"

    # Generate string portfolio representation
    suggested_portfolio_str = "ERROR - Portfolio string not initialized"
    try:
        suggested_portfolio = stock_info_container.get_portfolio()
        suggested_portfolio_str = portfolio_builder_project3.transform_portfolio_to_str(suggested_portfolio)
    except:
        return "EXCEPTION in: Generate string portfolio representation"

    return suggested_portfolio_str


def register_portfolio_recommendation_in_smartcontract(recommended_portfolio, contract_address):
    smart_contract_tool = Project3SmartContractTool(contract_address)
    id = 0
    smart_contract_tool.call()
