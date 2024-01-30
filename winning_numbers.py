import random

def get_numbers_ticket():
    num_list = set()

    for _ in range(5):
        random_number = random.randint(1, 1000)
        num_list.add(random_number)

    return num_list

result = get_numbers_ticket()

result_list = list(result)
two_random_numbers = random.sample(result_list, 3)
print(two_random_numbers, result)
