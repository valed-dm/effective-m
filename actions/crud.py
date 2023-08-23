"""CRUD for .csv as database"""

import csv

import pandas as pd

from .actions import sort, get_df
from utils.csv_data import path, fields


def create(data=fields, p=path):
    """Creates row in .csv file with CSV File API usage"""

    with open(p, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # data - fields array [field_1, field_2, ...]
        writer.writerow(data)


def read():
    """Reads .csv by pages. Page size = chunksize."""

    sort()
    csv_data = pd.read_csv(path, chunksize=50, iterator=True)
    while True:
        inp = input("for next page press enter; to quit type stop:_")
        if inp == "stop":
            raise StopIteration
        df = pd.DataFrame(next(csv_data))
        print(df.to_markdown())


def update(update_data):
    """Updates row column data stored in .csv"""

    df = get_df()
    str_row = list(update_data)[0]
    column = update_data[str_row][0]
    new_value = update_data[str_row][1]
    df.loc[int(str_row), [column]] = [new_value]
    print("update success!")
    print(f"column name: {column} row: {str_row} new data: {new_value}")
    df.to_csv(path, index=False)


def delete(row):
    """Deletes row from .csv using row number"""

    df = get_df()
    df.drop([int(row)], inplace=True)
    print(f"row {row} successfully deleted!")
    df.to_csv(path, index=False)
