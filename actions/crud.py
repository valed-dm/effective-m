import csv

import pandas as pd

from actions.actions import sort, get_df


def create(fds, mode):
    with open("phone_book.csv", mode, newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fds)


def read():
    sort()
    csv_data = pd.read_csv("phone_book.csv", chunksize=50, iterator=True)
    while True:
        inp = input("for next page press enter; to quit type stop:_")
        if inp == "stop":
            raise StopIteration
        df = pd.DataFrame(next(csv_data))
        print(df.to_markdown())


def update(update_data):
    df = get_df()
    str_row = list(update_data)[0]
    column = update_data[str_row][0]
    new_value = update_data[str_row][1]
    df.loc[int(str_row), [column]] = [new_value]
    print(f"column name: {column}\nrow: {str_row}\nnew data: {new_value}")
    df.to_csv("phone_book.csv", index=False)


def delete():
    pass
