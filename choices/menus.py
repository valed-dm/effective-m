"""Contains app's user interface menus"""
from typing import Callable

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
    else:
        return options[opt]()


def sub_menu(handler, navigator, delay, data=None):
    """Subsequent menu"""

    opt = timed_input(menu=SUB_MENU, delay=delay)
    exec_menu(opt, data, handler, navigator)


def exec_menu(opt, data, handler, navigator):
    """Executes app menus"""

    if opt == "1":
        handler(data)
    elif opt == "2":
        navigator()
    elif opt == "3":
        raise StopIteration
    elif opt == "4":
        raise AppExitError


def add_row():
    """Guides user through add row task"""

    user_data = user_input()
    print("Check your input")
    print(user_data)
    sub_menu(handler=create, navigator=add_row, delay=60, data=user_data)
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
    sub_menu(handler=row_result, navigator=search_row, delay=60, data=val_dict)
    # user is to enter row number, column name, new column value
    print("===enter update data=====================")
    update_data = update_input()
    sub_menu(handler=update, navigator=update_row, delay=60, data=update_data)
    raise StopIteration


def delete_row():
    """Guides user through delete row task"""

    print("Enter row to delete")
    row = delete_input()
    sub_menu(handler=delete, navigator=delete_row, delay=60, data=row)
    raise StopIteration


def search_row():
    """Guides user through find single row task"""

    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    sub_menu(handler=row_result, navigator=search_row, delay=60, data=val_dict)
    raise StopIteration


def search_column():
    """Guides user through find multiple rows task"""

    val_dict = search_multiple_rows()
    print("Check your search data")
    print(val_dict)
    sub_menu(handler=column_result, navigator=search_column, delay=60, data=val_dict)
    raise StopIteration
