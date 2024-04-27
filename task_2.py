# from datetime import datetime

# def het_days_from_today(date):
#     dr_day = datetime.strptime(date, "%Y.%m.%d").date()
#     today = datetime.today().date()
#     res = (today - dr_day).days
#     return res
# print(het_days_from_today(date='2020.10.09'))


from random import randint, sample

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min) + 1:
        return[]
    # if max > 1000:
    #     return[]
    # if min >= max:
    #     return[]
    # if quantity < 1:
    #     return[]
    # if quantity > max - min:
    #     return[]
    
    lotery_list = set()


    while len(lotery_list) != quantity:
        number = randint(min, max)
        print(number)
        lotery_list.add(number)
    print(type(lotery_list))
    return (list(lotery_list))

# lotery_list = get_numbers_ticket(1, 1000, 6)
# print(sorted(list(lotery_list)))


# from random import randint, sample

# def get_numbers_ticket(min, max, quantity):
#     return sample(range(min, max+1), quantity)

# print(sorted(list(lotery_list)))

if __name__ == "__main__":
    # print(get_numbers_ticket(10, 500, 490))


    print(get_numbers_ticket(0, 50, 5))  #min < 1 має вивести пустий список але генерує випадкові числа
    print(get_numbers_ticket(1, 1001, 10))  #max > 1000 має вивести пустий список але генерує випадкові числа
    print(get_numbers_ticket(50, 50, 5))  #min >= max має вивести пустий список але генерує випадкові числа
    print(get_numbers_ticket(1, 50, 0))  #quantity < 1 має вивести пустий список але генерує випадкові числа
    print(get_numbers_ticket(1, 50, 51))  #quantity too large має вивести пустий список але генерує випадкові числа
    print (get_numbers_ticket(10, 20,15))  #quantity exceeds max-min+1 має вивести пустий список але генерує випадкові числа
    print(get_numbers_ticket(1, 10, 6))  #Має вивести отсортований список унікальних чисел від 1 до 10 кількістю 6