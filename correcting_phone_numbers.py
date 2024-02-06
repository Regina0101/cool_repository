import re

users_phones = [
    "+38(050)123-32-34",
    "0503451234",
    "432 11 222 22 22",
    "(050)8889900",
    "38050-111-22-22",
    "+123456789012",
    "38050 111 22 11   "
]

def normalize_phone(phone_number):
    digit_phone = re.sub(r'\D', '', phone_number)

    if len(digit_phone) == 10 and digit_phone.startswith('0'):
        return "+38" + digit_phone
    elif len(digit_phone) == 10:
        return "+380" + digit_phone
    elif len(digit_phone) == 12 or digit_phone.startswith('380'):
        return "+" + digit_phone
    else:
        return digit_phone

for phone_number in users_phones:
    result = normalize_phone(phone_number)
    print(result)
