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
    is_valid = False
    search_data = ()

    while not is_valid:
        column = input("enter column name:_")
        if not column:
            print("please, enter column name")
            continue
        value = input("enter search value:_")
        if not value:
            print("please, enter search value")
            continue

        search_data = column, value
        is_valid = True

    return search_data
