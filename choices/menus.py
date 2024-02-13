"""Contains phonebook user interface menus"""

from typing import Callable

from actions.actions import row_result, column_result
from actions.crud import create, read, update, delete
from choices.gtypes import handler_type, data_type
from choices.text import SUB_MENU
from custom_exc.app_exit import AppExitError
from inputs.inputs import (
    user_input,
    timed_menu,
    search_single_row,
    search_multiple_rows,
    update_input,
    delete_input,
)


def main_menu_agent(opt: str) -> None:
    """Main menu agent function
    Routes CRUD or SEARCH functions depending on user choice
    Args:
        opt: User choice string value
    Raises:
        AppExitError: Custom exception is raised to quit phonebook
    """

    options = {
        "1": read,
        "2": add_row_interface,
        "3": update_row_interface,
        "4": delete_row_interface,
        "5": search_row_interface,
        "6": search_column_interface,
    }
    if opt == "7":
        raise AppExitError
    options[opt]()


def sub_menu(
        handler: handler_type,
        user_interface: Callable[[], None],
        delay: int,
        data: data_type = None
) -> None:
    """Launches subsequent menu
    SUB MENU
    1 - execute
    2 - repeat entry
    3 - MAIN MENU
    4 - quit
    Args:
        handler: CRUD or SEARCH functions depending on user choice
        user_interface: Repeats chosen entry operation anew to correct inputted data
        delay: Menu showtime in seconds
        data:
            None
            row: str - row_number to be deleted
            user_data: Tuple[str] - (str, str, str, str, str, str) new row data to insert
            val_dict: Dict[str, str]  - {column_1: value_1, column_2: value_2 ...} single row search by multiple values
            update_data: Dict[str, tuple[str, str]]  - {row_number: (column, value)} to update the selected field value
    Raises:
        StopIteration: Exception is raised to get to phonebook main menu
        AppExitError: Custom exception is raised to quit app
    """

    opt = timed_menu(menu=SUB_MENU, delay=delay)
    if opt == "1":
        handler(data)
    if opt == "2":
        user_interface()
    if opt == "3":
        raise StopIteration
    if opt == "4":
        raise AppExitError


def add_row_interface():
    """Guides user through add row task"""

    user_data = user_input()
    print("Check your input")
    print(user_data)
    sub_menu(handler=create, user_interface=add_row_interface, delay=60, data=user_data)
    print("your data successfully saved to phonebook")
    # redirects to main menu
    raise StopIteration


def update_row_interface():
    """Guides user through update row task"""

    # user is to define needed row number
    print("===find row number to update=============")
    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    sub_menu(handler=row_result, user_interface=search_row_interface, delay=60, data=val_dict)
    # user is to enter row number, column name, new column value
    print("===enter update data=====================")
    update_data = update_input()
    sub_menu(handler=update, user_interface=update_row_interface, delay=60, data=update_data)

    # redirects to main menu
    raise StopIteration


def delete_row_interface():
    """Guides user through delete row task"""

    print("Enter row to delete")
    row = delete_input()
    sub_menu(handler=delete, user_interface=delete_row_interface, delay=60, data=row)

    # redirects to main menu
    raise StopIteration


def search_row_interface():
    """Guides user through find single row task"""

    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    sub_menu(handler=row_result, user_interface=search_row_interface, delay=60, data=val_dict)

    # redirects to main menu
    raise StopIteration


def search_column_interface():
    """Guides user through find multiple rows task"""

    val_dict = search_multiple_rows()
    print("Check your search data")
    print(val_dict)
    sub_menu(handler=column_result, user_interface=search_column_interface, delay=60, data=val_dict)

    # redirects to main menu
    raise StopIteration
