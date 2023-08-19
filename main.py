import os

from menus.action import create
from inputs.inputs import timed_input
from menus.text import START_MENU
from menus.action import main_menu


def main():
    if not os.path.exists("phone_book.csv"):
        os.system("touch phone_book.csv")
        fields = ["fname", "lname", "mname", "company", "bphone", "cphone"]
        create(fds=fields, mode="w")
    opt = timed_input(menu=START_MENU, delay=30)
    main_menu(opt=opt)


if __name__ == "__main__":
    main()
