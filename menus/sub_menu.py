from typing import Callable

from menus.gtypes import handler_type, data_type
from choices.text import SUB_MENU
from exit_exception.app_exit import AppExitError
from .timed_menu import timed_menu


def sub_menu(
        handler: handler_type,
        user_interface: Callable[[], None | bool],
        delay: int,
        data: data_type = None
) -> None:
    """Subsequent menu
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
