"""User interfaces"""

from actions import create, update, delete, row_result, column_result, search_single_row, search_multiple_rows
from inputs.inputs import new_record_data, update_input, delete_input
from menus.sub_menu_decorator import sub_menu_decorator


@sub_menu_decorator(handler=create, delay=60)
def add_row_interface():
    """Guides user through add row task"""

    new_record = new_record_data()
    print("Check your input")
    print(new_record)
    return new_record


@sub_menu_decorator(handler=update, delay=60)
def update_row_interface():
    """Guides user through update row task"""

    update_data = update_input()
    return update_data


@sub_menu_decorator(handler=delete, delay=60)
def delete_row_interface():
    """Guides user through delete row task"""

    print("Enter row to delete or type stop")
    row = delete_input()
    return row


@sub_menu_decorator(handler=row_result, delay=60)
def search_row_interface():
    """Guides user through find single row task"""

    val_dict = search_single_row()
    print("Check your search data")
    for key, val in val_dict.items():
        print(key, val)
    return val_dict


@sub_menu_decorator(handler=column_result, delay=60)
def search_column_interface():
    """Guides user through find multiple rows task"""

    val_dict = search_multiple_rows()
    print("Check your search data")
    print(val_dict)
    return val_dict
