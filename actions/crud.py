"""CRUD for .csv as database"""

import csv

import pandas as pd

from utils.csv_data import path, fields
from .actions import sort, get_df


def create(data: list[str] = fields, p: str = path) -> None:
    """Creates row in .csv file with CSV File API usage
    Args:
        data: list of phonebook fields values to be stored in a .csv file row
        p: path to .csv file
    """

    with open(p, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)


def read() -> None:
    """Reads .csv by pages.
    Page size (rows qty per page shown) = chunksize.
    """

    sort()
    csv_data = pd.read_csv(path, chunksize=50, iterator=True)
    while True:
        inp = input("for next page press enter; to quit type stop:_")
        if inp == "stop":
            raise StopIteration
        df = pd.DataFrame(next(csv_data))
        print(df.to_markdown())


def update(update_data, p=path):
    """Updates row column data stored in .csv"""

    df = get_df(p)
    str_row = list(update_data)[0]
    column = update_data[str_row][0]
    new_value = update_data[str_row][1]
    df.loc[int(str_row), [column]] = [new_value]
    print("update success!")
    print(f"column name: {column} row: {str_row} new data: {new_value}")
    df.to_csv(p, index=False)


def delete(row, p=path):
    """Deletes row from .csv using row number"""

    df = get_df(p)
    df.drop([int(row)], inplace=True)
    print(f"row {row} successfully deleted!")
    df.to_csv(p, index=False)
