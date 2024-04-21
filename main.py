from datetime import datetime

def het_days_from_today(date):
    dr_day = datetime.strptime(date, "%Y.%m.%d").date()
    today = datetime.today().date()
    res = (today - dr_day).days
    return res
print(het_days_from_today(date='2020.10.09'))

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