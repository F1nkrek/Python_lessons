# Задание 3
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
from random import randint


def find_multiplicity(list_of_numbers):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] % 20 == 0 or list_of_numbers[i] % 21 == 0:
            list_of_numbers_mod.append(list_of_numbers[i])
    print(list_of_numbers_mod)


list_of_numbers = [randint(20, 240) for i in range(20)]
list_of_numbers.sort()
list_of_numbers_mod = []
print(list_of_numbers)
while True:
    if len(list_of_numbers) != 0:
        find_multiplicity(list_of_numbers)
        break
    else:
        continue
