"""Application entrypoint"""

import os
import sys

from actions.crud import create
from choices.menus import main_menu
from choices.text import START_MENU
from custom_exc.app_exit import AppExitError
from inputs.inputs import timed_input
from utils.csv_data import path


def main() -> None:
    """Launches main menu
    WELCOME TO PHONEBOOK MAIN MENU!
    1 - browse
    2 - add
    3 - update
    4 - delete
    5 - search row
    6 - search column
    7 - quit
    """

    opt = timed_input(menu=START_MENU, delay=30)
    main_menu(opt)


if __name__ == "__main__":
    if not os.path.exists(path):
        create()

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
            print("phbook operation is terminated by user")
            sys.exit(0)
        else:
            break
