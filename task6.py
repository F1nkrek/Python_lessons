# Задание 6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle


def func_count(start_number, finish_number):
    for i in count(start_number):
        if i > finish_number:
            break
        else:
            print(i)


def func_cycle(list_of_numbers, iteration):
    i = 0
    tmp = cycle(list_of_numbers)
    while i < iteration:
        print(next(tmp))
        i += 1


while True:
    start_number = start_number = int(input("Начальное число: "))
    finish_number = int(input("Конечное число: "))
    if start_number < finish_number:
        func_count(start_number, finish_number)
        break
    else:
        print("Второе число меньше первого!")
        continue

func_cycle(list_of_numbers=[4, 8, 15, 16, 23, 42], iteration=int(input("\nВведите количество повторений: ")))
