import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return [], []

    num_list = sorted(random.sample(range(minimum, maximum + 1), quantity))
    winners = random.sample(num_list, 3)

    return num_list, winners

result, winners = get_numbers_ticket(1, 1000, 5)
print("Всі числа:", result)
print("Переможці:", winners)
