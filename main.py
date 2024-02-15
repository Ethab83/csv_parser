import argparse as ap
import json as js
import pandas as pd

def main():
    # parse arguments
    args = parse_args()

    # Create a new CSVParser()
    parser = CSVParser()

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


class CSVParser:
    def parser_factory(self, args):
        self._unparsed_data = pd.read_csv(args.filename) # csv as a 2d array
        self._parsed_data = {}
        if args.left:
            self._parse_left()
        else:
            self._parse_top()
        
        return self._to_json()

    def _parse_left(self):
        self._parsed_data = self._unparsed_data.transpose().copy()

    def _parse_top(self):
        self._parsed_data = self._unparsed_data.copy()

    def _to_json(self):
        return self._parsed_data.to_json()

if __name__ == '__main__':
    main()
