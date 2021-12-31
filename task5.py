# Задание 5
# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

from random import randrange
from functools import reduce


list_of_numbers = [randrange(100, 1000, 2) for i in range(6)]
print(list_of_numbers)
print(reduce(lambda x, y: x * y, list_of_numbers))
