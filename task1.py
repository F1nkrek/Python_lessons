# Задание 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
try:
    file, hours, rate, bonus = argv

    print(f"Выработка в часах: {hours}")
    print(f"Ставка: {rate}")
    print(f"Премия: {bonus}")
    print(f"Зарплата сотрудника: {(int(hours) * int(rate)) + int(bonus)}")
except ValueError:
    print("Недостаточно данных! Введите параметры!")
