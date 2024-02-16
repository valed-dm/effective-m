"""Subsequent Menu Decorator"""

from functools import wraps

from menus.gtypes import handler_type
from menus.sub_menu import sub_menu


def sub_menu_decorator(**kwargs: handler_type | int):
    """Provides SUB MENU operation through user interfaces
    Args:
        **kwargs: CRUD or SEARCH functions; Menu showtime in seconds.
    """

    def inner_decorator(func):
        @wraps(func)
        def wrapper():
            data = func()
            handler = kwargs["handler"]
            # handler_execute_switch=True when option EXECUTE is chosen in SUB MENU
            handler_execute_switch = sub_menu(user_interface=func, delay=kwargs["delay"])
            if handler_execute_switch:
                handler(data)
            # Redirects user to MAIN MENU after requested task finished
            raise StopIteration

        return wrapper

    return inner_decorator
