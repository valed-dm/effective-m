"""Subsequent menu"""

from typing import Callable

from choices.text import SUB_MENU
from exit_exception.app_errors import terminated_by_user
from exit_exception.app_exit import AppExitError

from .timed_menu import timed_menu


def sub_menu(user_interface: Callable[[], None | bool], delay: int, ) -> None | bool:
    """Subsequent menu
    SUB MENU
    1 - execute
    2 - repeat entry
    3 - MAIN MENU
    4 - quit
    Args:
        user_interface: Repeats chosen entry operation anew to correct inputted data
        delay: Menu showtime in seconds
    Returns:
        bool: Controls execution of handler function when opt=1
    Raises:
        StopIteration: Exception is raised to get to phonebook main menu
        AppExitError: Custom exception is raised to quit app
    """

    opt = timed_menu(menu=SUB_MENU, delay=delay)

    if opt == "2":
        user_interface()
    if opt == "3":
        raise StopIteration
    if opt == "4":
        raise AppExitError(terminated_by_user)

    return True
