"""Subsequent Menu Decorator"""

from functools import wraps

from menus.sub_menu import sub_menu


def sub_menu_decorator(**kwargs):
    """Provides SUB MENU operation through user interfaces"""

    def inner_decorator(func):
        @wraps(func)
        def wrapper():
            data = func()
            sub_menu(**kwargs, user_interface=func, data=data)
            raise StopIteration

        return wrapper

    return inner_decorator
