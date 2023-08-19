import pandas as pd


def mask_standard(df, column, value):
    mask = df[column] == value
    return df[mask]


def search(column, value):
    df = get_df()
    res = mask_standard(df, column, value)
    idx = res.index
    print(res, idx)


def sort():
    df = pd.read_csv("phone_book.csv")
    sorted_df = df.sort_values(by=["fname"])
    sorted_df.to_csv("phone_book.csv", index=False)


def get_df():
    data = pd.read_csv("phone_book.csv")
    df = pd.DataFrame(data)
    return df
