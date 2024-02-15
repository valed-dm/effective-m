"""CRUD"""

import csv
from typing import Dict, Tuple

import pandas as pd
from csv_dir.csv_data import fields, path

from .actions import get_df, sort


def create(data: list[str] = fields, p: str = path) -> None:
    """Creates row in .csv file with CSV File API usage
    Args:
        data: list of phonebook fields values to be stored in a .csv file row
        p: path to .csv file
    """

    with open(p, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)
        print(f"{data} added to phonebook successfully")


def read() -> None:
    """Reads .csv page by page.
    Page size (rows qty per page shown) = chunksize.
    """

    sort()
    csv_data = pd.read_csv(path, chunksize=50, iterator=True)
    while True:
        inp = input("for next page press enter; to quit type stop:_")
        if inp == "stop":
            raise StopIteration
        # csv_data iterator outputs phonebook records by chunksize=50
        df = pd.DataFrame(next(csv_data))
        print(df.to_markdown())


def update(update_data: Dict[str, Tuple[str, str]], p: str = path) -> None:
    """Updates row-column field data value stored in .csv
    Args:
        update_data: {row_number: (column_name, new_value)}
        p: path to .csv file
    """

    # extracts row number list(dict) -> list[dict_key_1][0]
    row_number: str = list(update_data)[0]
    # update data tuple ('column', 'value')
    ud: tuple = update_data[row_number]
    # reads column name
    column: str = ud[0]
    # reads new field value
    new_value: str = ud[1]

    df = get_df(p)
    df.loc[int(row_number), [column]] = [new_value]

    print("update success!")
    print(f"column name: {column} row: {row_number} new data: {new_value}")

    # saves data to .csv
    df.to_csv(p, index=False)


def delete(row: str, p: str = path) -> None:
    """Deletes row from .csv using row number
    Args:
        row: row number to be deleted
        p: path to .csv file
    """

    df = get_df(p)
    df.drop([int(row)], inplace=True)

    print(f"row {row} successfully deleted!")

    df.to_csv(p, index=False)
