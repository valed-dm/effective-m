import pandas as pd


def mask_standard(df, val_dict):
    masks = []
    for key, value in val_dict.items():
        mask = df[key] == value[0]
        masks.append(mask)
    aggregate_mask = masks[0]
    for mask in masks[1:]:
        aggregate_mask = aggregate_mask & mask
    return df[aggregate_mask]


def mask_multiple(df, val_dict):
    # val_dict = {"c_1": [v_1, v_2, ...], "c_2": [v_1, v_2, ...], ...}
    dfs = []
    for key, value in val_dict.items():
        mask = df[key].isin(value)
        dfs.append(df[mask])
    return dfs


def get_df():
    data = pd.read_csv("phone_book.csv")
    df = pd.DataFrame(data)
    return df


def search(val_dict):
    df = get_df()
    res = mask_standard(df, val_dict)
    print(res)
    return res


def search_multiple(data):
    df = get_df()
    dfs = mask_multiple(df, data)
    for res in dfs:
        print(res)
    return dfs


def sort():
    df = pd.read_csv("phone_book.csv")
    sorted_df = df.sort_values(by=["fname"])
    sorted_df.to_csv("phone_book.csv", index=False)
