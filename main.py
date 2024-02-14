import argparse as ap
import json as js
import pandas as pd

def main():
    args = parse_args()

    parser = Parser(args.filename)

    if args.top:
        # TODO: parse with top as keys
        pass
    elif args.left:
        # TODO: parse with left as keys
        pass
    else:
        # TODO: parse with top as keys
        pass

    
def parse_args():
    parser = ap.ArgumentParser(
                    prog='csv_parser',
                    description='parse csv to json',
                    epilog='Created by: Ethan Mulcahy & Jonathan Pimentel')
    
    # arguments
    parser.add_argument('filename')
    parser.add_argument('-t', '--top', action='store_true', required=False, help='keys are located on top row (default)')
    parser.add_argument('-l', '--left', action='store_true', required=False, help='keys are located on left column')

    return parser.parse_args()

class Parser:
    def __init__(self, filename):
        self.unparsed_data = pd.read_csv(filename) # csv as a 2d array
        self.parsed_data = {}

    def to_json(self):
        # TODO
        pass

# TODO: maybe separate classes for top parser and left parser
#       (sorta overkill but probably required for factory method)

if __name__ == '__main__':
    main()
