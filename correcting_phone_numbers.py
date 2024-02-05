import re

users_phones = [
    "+38(050)123-32-34",
    "0503451234",
    "432 11 222 22 22",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

def normalize_phone(phone_number):
    digit_and_space_phone = re.sub(r'[^+\d]', '', phone_number)

    if len(digit_and_space_phone) == 13 and re.match(r'^\+380', digit_and_space_phone):
        return digit_and_space_phone
    elif len(digit_and_space_phone) == 10 and re.match(r'^\d{10}', digit_and_space_phone):
        if digit_and_space_phone.startswith('0'):
            return "+38" + digit_and_space_phone
        else:
            return "+380" + digit_and_space_phone[3:]
    elif len(digit_and_space_phone) < 10:
        return "Number is too short"
    elif len(digit_and_space_phone) > 13:
        return "Number is too long"
    else:
        modified_number = "+380" + re.sub(r"\D", "", digit_and_space_phone)[3:]
        return modified_number

for phone_number in users_phones:
    result = normalize_phone(phone_number)
    print(result)
