"""Provides user input timing and prompt functions"""

import select
import sys

from .input import input_charfield, input_phonefield


def timed_input(menu, delay):
    """Provides app's certain menu's showtime duration"""

    print(menu)
    print(f"You have {delay} seconds to answer!\nEnter your choice: ")
    a, b, c = select.select([sys.stdin], [], [], delay)
    if a:
        return sys.stdin.readline().strip()
    print("Your time expired. Make another attempt.")
    return sys.exit(0)


def user_input():
    """Asks for data to create a new record"""

    first_name = input_charfield("first_name")
    last_name = input_charfield("last_name")
    middle_name = input_charfield("middle_name")
    company = input_charfield("company")
    business_phone = input_phonefield("business_phone")
    cellular_phone = input_phonefield("cellular_phone")
    user_data = (
        first_name,
        last_name,
        middle_name,
        company,
        business_phone,
        cellular_phone,
    )
    return user_data


def update_input():
    """Prompts and waits for row number, column name, new value to be entered"""

    update_data = {}
    while True:
        row = input_charfield("row")
        column = input_charfield("column")
        new_value = input_charfield("new value")
        update_data[row] = column, new_value
        print(update_data)
        break
    return update_data


def delete_input():
    """Awaits user to enter row number to be deleted"""

    row = input_charfield("row")
    return row


def search_single_row():
    """Executes search 'one row - multiple columns values match'"""

    search_data = {}
    print("one row - many columns")
    while True:
        print("to exit enter 'stop'")
        column = input_charfield("column")
        if column == "stop":
            break
        value = input_charfield("value")
        search_data[column] = value
    return search_data


def search_multiple_rows():
    """Executes search one column - multiple rows values match"""

    search_data = {}
    print("one column - many rows")
    while True:
        try:
            list(search_data)[0]
        except IndexError:
            column = input_charfield("column")
            search_data[column] = ()
        print("to exit enter 'stop'")
        while True:
            value = input_charfield("value")
            if value == "stop":
                break
            column = list(search_data)[0]
            search_data[column] = search_data[column] + (value,)
        return search_data
