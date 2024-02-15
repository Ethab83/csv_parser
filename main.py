import csv_parser
import argparse as ap
import json as js
import pandas as pd

def main():
    # parse arguments
    args = parse_args()

    unparsed_data = pd.read_csv(args.filename) # csv as a 2d array
    parsed_data = {}

    # get json
    if args.top:
        json = unparsed_data.copy().to_json()
    if args.left:
        # transpose
        json = unparsed_data.transpose().copy().to_json()

    else:
        json = unparsed_data.copy().to_json()

    parsed_json = js.loads(json) 

    # write json to output.txt
    with open("output.txt", "w") as out_file:
        out_file.write(js.dumps(parsed_json, indent=4) )

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


if __name__ == '__main__':
    main()
