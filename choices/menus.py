from actions.actions import search, search_multiple
from actions.crud import create, read, update
from choices.text import ADD_MENU, START_MENU, SEARCH_MENU, UPDATE_MENU
from inputs.inputs import (
    user_input,
    timed_input,
    search_input,
    search_multiple_input,
    update_input,
)


def add_row():
    user_data = user_input()
    print("Check your input")
    print(user_data)
    selection = timed_input(menu=ADD_MENU, delay=60)
    add_menu(opt=selection, fds=user_data)
    print("your data successfully saved to phonebook")
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def search_row():
    val_dict = search_input()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    selection = timed_input(menu=SEARCH_MENU, delay=60)
    search_menu(opt=selection, val_dict=val_dict)
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def search_rows():
    val_dict = search_multiple_input()
    print("Check your search data")
    for key, value in val_dict.items():
        print(key, ":", value)
    selection = timed_input(menu=SEARCH_MENU, delay=60)
    multiple_search_menu(opt=selection, val_dict=val_dict)
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def update_row():
    val_dict = search_input()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    selection = timed_input(menu=SEARCH_MENU, delay=60)
    search_menu(opt=selection, val_dict=val_dict)
    print("-----enter update data-----")
    update_data = update_input()
    selection = timed_input(menu=UPDATE_MENU, delay=60)
    update_menu(opt=selection, update_data=update_data)
    selection = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=selection)


def main_menu(opt):
    if opt == "1":
        read()
    elif opt == "2":
        add_row()
    elif opt == "3":
        update_row()
    elif opt == "4":
        search_row()
    elif opt == "5":
        search_rows()
    elif opt == "6":
        quit()


def add_menu(opt, fds):
    if opt == "1":
        create(fds=fds, mode="a")
    elif opt == "2":
        add_row()
    elif opt == "3":
        quit()


def search_menu(opt, val_dict):
    if opt == "1":
        search(val_dict)
    elif opt == "2":
        search_row()
    elif opt == "3":
        quit()


def multiple_search_menu(opt, val_dict):
    if opt == "1":
        search_multiple(val_dict)
    elif opt == "2":
        search_rows()
    elif opt == "3":
        quit()


def update_menu(opt, update_data):
    if opt == "1":
        update(update_data)
    elif opt == "2":
        update_row()
    elif opt == "3":
        quit()
