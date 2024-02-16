"""Gets, sorts, requests .csv file as database"""

from typing import Dict, Tuple

import pandas as pd
from pandas import DataFrame
from csv_dir.csv_data import path
from inputs.check_input import input_charfield


def get_df(p: str = path) -> DataFrame:
    """Creates dataframe from .csv
    Args:
        p: path to .csv file
    Returns:
        DataFrame: df from .csv at given path
    """

    data = pd.read_csv(p)
    df = pd.DataFrame(data)
    return df


def sort() -> None:
    """Sorts and save sorted data to .csv"""

    df = pd.read_csv(path)
    sorted_df = df.sort_values(by=["fname"])
    sorted_df.to_csv(path, index=False)


def row_result(val_dict: Dict[str, str], p: str = path) -> DataFrame:
    """Executes single row search with multiple columns values
    Args:
        val_dict: {column_1: value_1, column_2: value_2, ...} search data dict
        p: path to .csv file
    Returns:
        DataFrame: df from .csv at given path with search mask applied
    """

    df = get_df(p)
    masks = []
    for key, value in val_dict.items():
        mask = df[key] == value
        masks.append(mask)
    aggregate_mask = masks[0]
    for mask in masks[1:]:
        # aggregate_mask contains any given columns data to be contained in a single row
        aggregate_mask = aggregate_mask & mask
    res = df[aggregate_mask]
    print(res)
    return res


def column_result(val_dict: Dict[str, Tuple[str]], p: str = path) -> DataFrame:
    """Executes multiple row search with one or more column's values
    Args:
        val_dict: {column: (value_1, value_2, value_3 ...)} search data dict
        p: path to .csv file
    Returns:
        DataFrame: df from .csv at given path with search mask applied
    """

    df = get_df(p)
    key = list(val_dict)[0]
    # .isin() considers multiple column values to be contained in all selected rows
    mask = df[key].isin(val_dict[key])
    res = df[mask]
    print(res)
    return res


def search_single_row() -> Dict[str, str]:
    """Prompts for search data 'one row - multiple columns'
    Returns:
        Dict: {column_1: value_1, column_2: value_2, ...}
    """

    search_data = {}
    print("one row - many columns")
    while True:
        print("to exit enter 'stop'")
        column = input_charfield("column")
        if column == "stop":
            break
        value = input_charfield("value")
        # fills search_data with key-values pairs
        search_data[column] = value
    return search_data


def search_multiple_rows() -> Dict[str, Tuple[str]]:
    """Prompts for search data 'one column - multiple rows'
    Returns:
        Dict: {column: (value_1, value_2, value_3 ...)}
    """

    search_data: Dict[str, Tuple] = {}
    print("one column - many rows")
    while True:
        try:
            list(search_data)[0]
        except IndexError:
            # prompts for column name when does not exist
            column = input_charfield("column")
            # creates new key-value pair in search data Dict
            search_data[column] = ()
        print("to exit enter 'stop'")
        while True:
            # prompts for an extra column value
            value = input_charfield("value")
            if value == "stop":
                break
            # gets related column name
            column = list(search_data)[0]
            # adds one more value to column values Tuple
            search_data[column] = search_data[column] + (value,)
        return search_data
