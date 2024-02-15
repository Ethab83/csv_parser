# csv_parser

csv parser to json

> [!NOTE]
> compatible with **python 3.10.12+**

## Install dependencies

```shell
pip install -r requirements.txt
```

## Usage

```shell
python main.py file.csv [-t | -l]

    -t: keys are located on top row (default)
    -l: keys are located on left column

# show help
python main.py -h
```

## References

- [`pd.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [`pd.to_json()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)
- [`pd.transpose()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html)