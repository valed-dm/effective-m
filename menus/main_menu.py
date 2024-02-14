"""Main phonebook menu"""

from actions.crud import read
from choices.text import START_MENU
from exit_exception.app_exit import AppExitError
from interfaces.user_interfaces import (add_row_interface,
                                        delete_row_interface,
                                        search_column_interface,
                                        search_row_interface,
                                        update_row_interface)

from .timed_menu import timed_menu


def main_menu() -> None:
    """Main menu
    WELCOME TO PHONEBOOK MAIN MENU!
    1 - browse
    2 - add
    3 - update
    4 - delete
    5 - search row
    6 - search column
    7 - quit
    Routes CRUD or SEARCH functions depending on user choice
    Raises:
        AppExitError: Custom exception is raised to quit phonebook
    """

    opt = timed_menu(menu=START_MENU, delay=30)
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
