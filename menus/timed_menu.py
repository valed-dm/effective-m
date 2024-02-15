"""Displays menu string for given showtime duration"""

import select
import sys


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

    print("Your time expired. Make another attempt.")
    sys.exit(0)
