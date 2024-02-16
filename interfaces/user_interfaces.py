"""User interfaces"""
from typing import Dict, Tuple

from actions import (column_result, create, delete, row_result,
                     search_multiple_rows, search_single_row, update)
from inputs.inputs import field_update_input, new_record_data, row_delete_input
from menus.gtypes import row_type
from menus.sub_menu_decorator import sub_menu_decorator


@sub_menu_decorator(handler=create, delay=60)
def add_row_interface() -> row_type:
    """Guides user through add row task
    Returns:
        Tuple[str, str, str, str, str, str] -
        first_name, last_name, middle_name, company, business_phone, cellular_phone
    """

    new_record = new_record_data()
    print("Check your new record data\n", new_record)
    return new_record


@sub_menu_decorator(handler=update, delay=60)
def update_row_interface() -> Dict[str, Tuple[str, str]]:
    """Guides user through update row task
    Returns:
        Dict[row_number, Tuple[column_name, new_value]]
    """

    update_data = field_update_input()
    print("Check update data\n", update_data)
    return update_data


@sub_menu_decorator(handler=delete, delay=60)
def delete_row_interface() -> str:
    """Guides user through delete row task
    Returns:
        str - row number
    """

    print("Enter row to delete or type stop")
    row = row_delete_input()
    return row


@sub_menu_decorator(handler=row_result, delay=60)
def search_row_interface() -> Dict[str, str]:
    """Guides user through search for a single row task
    Returns:
        Dict: {column_1: value_1, column_2: value_2, ...} pairs dictionary
    """

    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    return val_dict


@sub_menu_decorator(handler=column_result, delay=60)
def search_column_interface() -> Dict[str, Tuple[str]]:
    """Guides user through search for multiple rows task
    Returns:
        Dict: {column: (value_1, value_2, value_3 ...)}
    """

    val_dict = search_multiple_rows()
    print("Check your search data")
    print(val_dict)
    return val_dict
