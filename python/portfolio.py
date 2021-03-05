import sys
import getopt
import traceback

from config import *

def main():#argc, argv):
    try:
        argv=""
        (opts,args) = getopt.getopt(argv,"hr:i:p:d:")

        command=""

        # uint risk;
        # uint unitial_investment;
        # string[] industries_preferences;
        # uint investing_duration;
        for opt,arg in opts:
            if opt=="-c":
                command=str(arg)
            else:
                usage()
                sys.exit(1)

        id = 0
        metrics = ""
        industry_data = ""
        portfolios_info = ""

        build_portfolio()

        # TODO David specify inputs and outputs foreach component.

        contract = initContract()
        print(contract)
        portfolio = contract.functions.registerPortfolio().call()
        # portfolio = contract.functions.buildPortfolio(id, metrics, industry_data, portfolios_info)

        print(portfolio)

        
    except:
        traceback.print_exc()

def usage():
    print("Usage: python portfolio.py -c command")

if __name__ == "__main__":
    # main(sys.argv[1:])
    main()
    exit()
