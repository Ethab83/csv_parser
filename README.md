# csv_parser (Factory method removed)

csv parser to json

> [!NOTE]
> compatible with **python 3.10.12+**

## Install dependencies

```shell
pip install -r requirements.txt
```

## Usage

```text
usage: python main.py file.csv [-t | -l]

options:
    -h, --help  show this help message and exit
    -t, --top   keys are located on top row (default)
    -l, --left  keys are located on left column

```

## References

- [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [`pd.to_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)
- [`pd.transpose()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html)
- [`CSVParserFactory`](https://www.geeksforgeeks.org/factory-method-python-design-patterns/)
