import re

users_phones= ["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]

def normalize_phone(phone_number):
    digit_and_space_phone = re.sub(r'[^+\d]', '', phone_number)
    if re.match(r'^\+38', digit_and_space_phone):
        return print(digit_and_space_phone)
    elif re.match(r'^38', digit_and_space_phone):
        modified_num = "+" + digit_and_space_phone
        return print(modified_num)
    else:
        modified_number = "+38" + re.sub(r"\D", "", digit_and_space_phone)
        return print(modified_number)


for phone_number in users_phones:
    normalize_phone(phone_number)
