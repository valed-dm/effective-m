import os

from actions.crud import create
from inputs.inputs import timed_input
from choices.menus import main_menu
from choices.text import START_MENU


def main():
    if not os.path.exists("phone_book.csv"):
        os.system("touch phone_book.csv")
        fields = ["fname", "lname", "mname", "company", "bphone", "cphone"]
        create(fds=fields, mode="w")
    opt = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=opt)


if __name__ == "__main__":
    try:
        main()
    except StopIteration:
        ok = False
        option = timed_input(menu=START_MENU, delay=30)
        main_menu(opt=option)
