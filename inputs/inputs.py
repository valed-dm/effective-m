import select
import sys


def timed_input(menu, delay):
    print(menu)
    print(f"You have {delay} seconds to answer!\nEnter your choice: ")
    a, b, c = select.select([sys.stdin], [], [], delay)
    if a:
        return sys.stdin.readline().strip()
    else:
        print("Your time got over")
        sys.exit(0)


def user_input():
    is_valid = False
    user_data = ()

    while not is_valid:
        first_name = input("enter your first name:_")
        if not first_name:
            print("please, enter first name")
            continue
        last_name = input("enter your last name:_")
        if not last_name:
            print("please, enter last name")
            continue
        middle_name = input("enter your middle name:_")
        if not middle_name:
            print("please, enter middle name")
            continue
        company = input("enter company name:_")
        if not company:
            print("please, enter company name")
            continue
        business_phone = input("enter business phone:_")
        if not business_phone:
            print("please, enter business phone")
            continue
        cellular_phone = input("enter cellular phone:_")
        if not cellular_phone:
            print("please, enter cellular phone")
            continue

        user_data = (
            first_name,
            last_name,
            middle_name,
            company,
            business_phone,
            cellular_phone,
        )

        is_valid = True

    return user_data


def search_input():
    search_data = {}

    while True:
        print("start input; to exit enter 'stop'")
        column = input("enter column name:_")
        if column == "stop":
            break
        elif not column:
            print("please, enter column name")
            continue
        value = input("enter search value:_")
        if not value:
            print("please, enter search value")
            continue

        search_data[column] = (value,)

    return search_data


def search_multiple_input():
    search_data = {}

    while True:
        values = []
        print("start input, to exit enter 'stop'")
        column = input("enter column name:_")
        if column == "stop":
            break
        elif not column:
            print("please, enter column name")
            continue

        print("enter search values, to exit enter 'stop'")
        while True:
            value = input("enter next search value:_")
            if value == "stop":
                break
            if not value:
                print("please, enter next search value")
                continue
            values.append(value)

        search_data[column] = values

    return search_data


def update_input():
    is_valid = False
    update_data = {}

    while not is_valid:
        row = input("enter row>")
        if not row:
            print("please, enter row")
            continue
        column = input("enter column name>")
        if not column:
            print("please, enter column name")
            continue
        new_value = input("enter new value>")
        if not new_value:
            print("please, enter new value")
            continue

        update_data[row] = column, new_value
        print(update_data)

        is_valid = True

    return update_data
