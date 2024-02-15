import pandas as pd

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
