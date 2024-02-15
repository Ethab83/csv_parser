import csv_parser
import argparse as ap
import json as js

def main():
    # parse arguments
    args = parse_args()

    # Create a new CSVParser()
    parser = csv_parser.CSVParser()

    # get json
    json = parser.parser_factory(args)
    parsed = js.loads(json) 
    

    # write json to output.txt
    with open("output.txt", "w") as out_file:
        out_file.write(js.dumps(parsed, indent=4) )

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
