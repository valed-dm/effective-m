"""Provides user input simple check, prompt functions"""

from inputs.val_phone import val_phone


def input_charfield(field):
    """Checks text input"""

    while True:
        res = input(f"enter {field} > ")
        if not res:
            print("repeat your entry > ")
            continue
        break
    return res


def input_phonefield(field):
    """Checks phone number input"""

    while True:
        res = input_charfield(field)
        if not val_phone(res):
            print(f"enter valid {field}")
            continue
        break
    return res
