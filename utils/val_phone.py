"""Simple phone number validation is used as example. Not specified in specifications."""

import re


pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
pattern1 = re.compile(
    r"(?P<country_code>\+\d{1,3})?\s?\(?(?P<area_code>\d{1,4})\)?[\s.-]?(?P<local_number>\d{3}[\s.-]?\d{4})"
)
# pattern2 = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")


def preprocess_phone_number(phone_number):
    """Example of number preparation"""

    # Remove extra spaces
    phone_number = " ".join(phone_number.split())
    # Replace common incorrect separators
    phone_number = phone_number.replace(",", ".").replace(";", ".")
    return phone_number


def val_phone(phone_number):
    """Example of simple phone validation"""

    phone_number = preprocess_phone_number(phone_number)
    match = re.search(pattern1, phone_number)
    if match:
        return True
    return False


# non-comprehensive test data
test_phone_numbers = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "invalid phone number",
    "7 978 9445115",
    "+7 (978) 944-5005",
    "+60 (0)3 2723 7900",
    "+60 (0)3 2723 7900",
    "+ 60 (0)4 255 9000",
    "+6 (03) 8924 8686",
    "+6 (03) 8924 8000",
    "+ 60 (7) 268-6200",
    "+60 (7) 228-6202",
    "+601-4228-8055",
    "991.335.2510",
]


if __name__ == "__main__":
    for number in test_phone_numbers:
        print(f"{number}: {val_phone(number)}")
