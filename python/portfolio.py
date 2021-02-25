import sys
import getopt
import traceback

import config

def main():
    try:
        (opts,args) = getopt.getopt(argv,"hc:")

        command=""

        for opt,arg in opts:
            if opt=="-c":
                command=str(arg)
            else:
                usage()
                sys.exit(1)

        
    except:
        traceback.print_exc()

def usage():
    print("Usage: python portfolio.py -c command")

if __name__ == "__main__":
    main(sys.argv[1:])
    exit()
