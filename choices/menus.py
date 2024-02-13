"""Contains app's user interface menus"""
from typing import Callable, Dict, Tuple, Union, List

from pandas import DataFrame

from actions.actions import row_result, column_result
from actions.crud import create, read, update, delete
from choices.text import SUB_MENU
from custom_exc.app_exit import AppExitError
from inputs.inputs import (
    user_input,
    timed_input,
    search_single_row,
    search_multiple_rows,
    update_input,
    delete_input,
)


def main_menu(opt: str) -> Callable[[], None] | AppExitError:
    """Main menu
    Args:
        opt: User choice string value
    Returns:
        CRUD or SEARCH functions depending on user choice
    Raises:
        AppExitError: Custom exception is raised to quit app
    """

    options = {
        "1": read,
        "2": add_row,
        "3": update_row,
        "4": delete_row,
        "5": search_row,
        "6": search_column,
    }

    if opt == "7":
        raise AppExitError

    return options[opt]()


def sub_menu(
        handler: Union[
            Callable[[List[str], str], None],  # create
            Callable[[Dict[str, Tuple[str, str]], str], None],  # update
            Callable[[str, str], None],  # delete
            Callable[[Dict[str, str], str], DataFrame],  # row_result
            Callable[[Dict[str, Tuple[str]], str], DataFrame],  # column_result
        ],
        repeater: Callable[[], None],
        delay: int,
        data: Union[
            None,
            str,
            Tuple[str],
            Dict[str, str],
            Dict[str, tuple[str, str]],
        ] = None
) -> None:
    """Subsequent menu
    Args:
        handler: CRUD or SEARCH functions depending on user choice
        repeater: Repeats chosen entry operation anew to correct inputted data
        delay: Menu showtime in seconds
        data:
            None
            row: str - row_number to be deleted
            user_data: Tuple[str] - (str, str, str, str, str, str) new row data to insert
            val_dict: Dict[str, str]  - {column_1: value_1, column_2: value_2 ...} single row search by multiple values
            update_data: Dict[str, tuple[str, str]]  - {row_number: (column, value)} to update the selected field value
    """

    opt = timed_input(menu=SUB_MENU, delay=delay)
    exec_menu(opt, data, handler, repeater)


def exec_menu(opt, data, handler, repeater):
    """Executes app menus"""

    if opt == "1":
        handler(data)
    elif opt == "2":
        repeater()
    elif opt == "3":
        raise StopIteration
    elif opt == "4":
        raise AppExitError


def add_row():
    """Guides user through add row task"""

    user_data = user_input()
    print("Check your input")
    print(user_data)
    sub_menu(handler=create, repeater=add_row, delay=60, data=user_data)
    print("your data successfully saved to phonebook")
    raise StopIteration


def update_row():
    """Guides user through update row task"""

    # user is to define needed row number
    print("===find row number to update=============")
    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    sub_menu(handler=row_result, repeater=search_row, delay=60, data=val_dict)
    # user is to enter row number, column name, new column value
    print("===enter update data=====================")
    update_data = update_input()
    sub_menu(handler=update, repeater=update_row, delay=60, data=update_data)
    raise StopIteration


def delete_row():
    """Guides user through delete row task"""

    print("Enter row to delete")
    row = delete_input()
    sub_menu(handler=delete, repeater=delete_row, delay=60, data=row)
    raise StopIteration


def search_row():
    """Guides user through find single row task"""

    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    sub_menu(handler=row_result, repeater=search_row, delay=60, data=val_dict)
    raise StopIteration


def search_column():
    """Guides user through find multiple rows task"""

    val_dict = search_multiple_rows()
    print("Check your search data")
    print(val_dict)
    sub_menu(handler=column_result, repeater=search_column, delay=60, data=val_dict)
    raise StopIteration
