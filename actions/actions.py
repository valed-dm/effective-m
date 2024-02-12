"""Gets, sorts, requests .csv file as database"""
from typing import Dict, Tuple

import pandas as pd
from pandas import DataFrame, Series

from utils.csv_data import path


def get_df(p: str = path) -> DataFrame:
    """Creates dataframe from .csv
    Args:
        p: path to .csv file
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
        val_dict: {column_1: value_1, column_2: value_2, ...}
        p: path to .csv file
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
        val_dict: {column: (value_1, value_2, value_3 ...)}
        p: path to .csv file
    """

    df = get_df(p)
    key = list(val_dict)[0]
    # .isin() considers multiple column values to be contained in all selected rows
    mask = df[key].isin(val_dict[key])
    res = df[mask]
    print(res)
    return res
