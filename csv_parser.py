import pandas as pd

# Factory Method (https://www.geeksforgeeks.org/factory-method-python-design-patterns/)
def CSVParserFactory(key_orientation='top'):
    parsers = {
        'left':_LeftParser,
        'top': _TopParser,
    }
    return parsers[key_orientation]()

# Base class, not to be instantiated
class _CSVParser():
    def parse(self, filename):
        if __class__ == "CSVParser":
            raise NotImplementedError
        
        self._unparsed_data = pd.read_csv(filename) # csv as a 2d array
        self._parsed_data = {}

    def _to_json(self):
        if __class__ == "CSVParser":
            raise NotImplementedError
        
        return self._parsed_data.to_json()

# Parser for left keys
class _LeftParser(_CSVParser):
    def parse(self, filename):
        super().parse(filename)
        self._parsed_data = self._unparsed_data.transpose().copy()
        
        return self._to_json()

# Parser for top keys
class _TopParser(_CSVParser):
    def parse(self, filename):
        super().parse(filename)
        self._parsed_data = self._unparsed_data.copy()
        
        return self._to_json()