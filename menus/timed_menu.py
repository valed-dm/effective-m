"""Displays menu string for given showtime duration"""

import select
import sys

from exit_exception.app_exit import AppExitError


def timed_menu(menu: str, delay: int) -> str:
    """Displays menu string for given showtime duration
    Args:
        menu: Menu string
        delay: Menu showtime in seconds
    """
    print(menu)
    print(f"You have {delay} seconds to answer!\nEnter your choice: ")

    a, b, c = select.select([sys.stdin], [], [], delay)
    if a:
        return sys.stdin.readline().strip()

    raise AppExitError("Your time expired. Make another attempt.")
