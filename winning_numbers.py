import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return set()

    num_set = set(random.sample(range(minimum, maximum + 1), quantity))

    return num_set

result = get_numbers_ticket(1, 1000, 5)
print(result)
