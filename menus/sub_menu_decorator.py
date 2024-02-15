"""Subsequent Menu Decorator"""

from functools import wraps
from typing import Callable

from menus.gtypes import handler_type
from menus.sub_menu import sub_menu


def sub_menu_decorator(**kwargs: handler_type | int):
    """Provides SUB MENU operation through user interfaces
    Args:
        **kwargs: CRUD or SEARCH functions; Menu showtime in seconds.
    """

    def inner_decorator(func: Callable[[], None | bool]) -> Callable[[], None | bool]:
        @wraps(func)
        def wrapper():
            data = func()
            sub_menu(**kwargs, user_interface=func, data=data)
            # Redirects user to MAIN MENU after requested task finished
            raise StopIteration

        return wrapper

    return inner_decorator
