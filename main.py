"""Phonebook entrypoint"""

import os
import sys

from actions.crud import create
from menus.main_menu import main_menu
from exit_exception.app_exit import AppExitError
from csv_dir.csv_data import path


def main() -> None:
    """Launches main menu"""

    main_menu()


if __name__ == "__main__":
    # creates .csv storage when not found on csv_dir.csv_data path
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
        except AppExitError as e:
            # executes sys.exit for all menus exit points;
            print(e)
            sys.exit(0)
        else:
            break
