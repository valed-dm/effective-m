import csv

import pandas as pd

from actions.actions import get_df, mask_standard, sort
from inputs.inputs import user_input, timed_input, search_input
from menus.text import ADD_MENU, START_MENU, SEARCH_MENU


def add_new():
    user_data = user_input()
    print("Check your input")
    print(user_data)
    selection = timed_input(menu=ADD_MENU, delay=60)
    add_menu(opt=selection, fds=user_data)
    print("your data successfully saved to phonebook")
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def search_row():
    column, value = search_input()
    print("Check your search data")
    print(column, value)
    selection = timed_input(menu=SEARCH_MENU, delay=60)
    search_menu(opt=selection, column=column, value=value)
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def search(column, value):
    df = get_df()
    res = mask_standard(df, column, value)
    idx = res.index
    print(res, idx)


def create(fds, mode):
    with open("phone_book.csv", mode, newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fds)


def read():
    ok = True
    sort()
    csv_data = pd.read_csv("phone_book.csv", chunksize=50, iterator=True)
    while ok:
        input("for next page press enter")
        try:
            df = pd.DataFrame(next(csv_data))
            print(df.to_markdown())
        except StopIteration:
            print("data exhausted")
            ok = False
            selection = timed_input(menu=START_MENU, delay=30)
            main_menu(opt=selection)


def update():
    df = get_df()
    print(df)


def delete():
    pass


def main_menu(opt):
    if opt == "1":
        read()
    elif opt == "2":
        add_new()
    elif opt == "3":
        update()
    elif opt == "4":
        search_row()
    elif opt == "5":
        quit()


def add_menu(opt, fds):
    if opt == "1":
        create(fds=fds, mode="a")
    elif opt == "2":
        add_new()
    elif opt == "3":
        quit()


def search_menu(opt, column, value):
    if opt == "1":
        search(column, value)
    elif opt == "2":
        search_row()
    elif opt == "3":
        quit()
