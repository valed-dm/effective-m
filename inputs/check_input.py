"""Provides user input simple check, prompt functions"""

from inputs.val_phone import val_phone


def input_charfield(field: str) -> str:
    """Simplest text checker for non-empty input
    Args:
        field: str
    Returns:
        str
    """

    while True:
        res = input(f"enter {field} > ")
        if not res:
            print("repeat your entry > ")
            continue
        break
    return res


def input_phonefield(field: str) -> str:
    """Just an example of phone number validation
    Args:
        field: str
    Returns:
        str
    """

    while True:
        res = input_charfield(field)
        if not val_phone(res):
            print(f"enter valid {field}")
            continue
        break
    return res
