"""Provides user input timing and prompt functions"""
from typing import Dict, Tuple

from .check_input import input_charfield, input_phonefield


def new_record_data() -> Tuple[str, str, str, str, str, str]:
    """Prompts for data to create a new record
    Returns:
        Tuple[str, str, str, str, str, str] - new .csv record values
    """

    first_name = input_charfield("first_name")
    last_name = input_charfield("last_name")
    middle_name = input_charfield("middle_name")
    company = input_charfield("company")
    business_phone = input_phonefield("business_phone")
    cellular_phone = input_phonefield("cellular_phone")
    record_data = (
        first_name,
        last_name,
        middle_name,
        company,
        business_phone,
        cellular_phone,
    )
    return record_data


def field_update_input() -> Dict[str, (str, str)]:
    """Prompts for row number, column name, new value
    Returns:
        Dict[str, (str, str)]
    """

    update_data = {}
    while True:
        row = input_charfield("row")
        column = input_charfield("column")
        new_value = input_charfield("new value")
        update_data[row] = column, new_value
        print(update_data)
        break
    return update_data


def delete_input():
    """Awaits user to enter row number to be deleted"""

    row = input_charfield("row")
    return row
