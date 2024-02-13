"""Phonebook entrypoint"""

import os
import sys

from actions.crud import create
from choices.menus import main_menu_agent
from choices.text import START_MENU
from custom_exc.app_exit import AppExitError
from inputs.inputs import timed_menu
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

    opt = timed_menu(menu=START_MENU, delay=30)
    main_menu_agent(opt)


if __name__ == "__main__":
    # creates .csv storage when not found on utils.csv_data path
    if not os.path.exists(path):
        create()

    # restarts or exits from phonebook app
    while True:
        try:
            main()
        except (StopIteration, KeyboardInterrupt):
            # when raised makes user redirected to main menu;
            pass
        except KeyError:
            # no search match found;
            # makes user redirected to main menu for a new attempt;
            print("Request returns no data. Try other search.")
        except AppExitError:
            # executes sys.exit for all menus exit points;
            print("phonebook operation is terminated by user")
            sys.exit(0)
        else:
            break
