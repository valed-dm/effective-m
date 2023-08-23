"""Some .csv needed data storage"""

path = "csv/phone_book.csv"
fields = ["fname", "lname", "mname", "company", "bphone", "cphone"]
fds = [
    "Paul",
    "Smith",
    "Batkovich",
    "COMPANY",
    "+1 (123) 456 7890",
    "+2 (123) 456 7890",
]
updated = [
    "Paul",
    "Smith",
    "Batkovich",
    "EFFECTIVE",
    "+1 (123) 456 7890",
    "+2 (123) 456 7890",
]
company_low = [
    "Paul",
    "Smith",
    "Batk",
    "company",
    "+1 (123) 456 7890",
    "+2 (123) 456 7890",
]
effective_low = [
    "Paul",
    "Smith",
    "Batk",
    "effective",
    "+1 (123) 456 7890",
    "+2 (123) 456 7890",
]
val_dict_1 = {
    "fname": "Paul",
    "mname": "Batk",
    "company": "effective",
}
