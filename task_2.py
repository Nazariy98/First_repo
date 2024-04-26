# 1 випадок
from random import randint, sample

def get_numbers_ticket(min, max, quantity):
    lotery_list = set()
    while len(lotery_list) != quantity:
        lotery_list.add(randint(min, max))
    return lotery_list
lotery_list = get_numbers_ticket(1, 1000, 6)
print(sorted(list(lotery_list)))

# 2 випадок
from random import randint, sample

def get_numbers_ticket(min, max, quantity):
    return sample(range(min, max+1), quantity)

print(sorted(list(lotery_list)))