"""Application entrypoint"""

import os
import sys

from actions.crud import create
from choices.menus import main_menu
from choices.text import START_MENU
from custom_exc.app_exit import AppExitError
from inputs.inputs import timed_input


def main():
    """Launches main menu. Creates phone_book.csv as db storage if not exists."""

    if not os.path.exists("phone_book.csv"):
        os.system("touch phone_book.csv")
        fields = ["fname", "lname", "mname", "company", "bphone", "cphone"]
        create(fields)
    opt = timed_input(menu=START_MENU, delay=30)
    main_menu(opt)


if __name__ == "__main__":
    # automatically restarts app and processes exceptions
    while True:
        try:
            main()
        except (StopIteration, KeyboardInterrupt):
            pass
        except KeyError:
            # no search match found
            print("Request returns no data. Try other search.")
        except AppExitError:
            # executes sys.exit for all menus exit point
            sys.exit(0)
        else:
            break
