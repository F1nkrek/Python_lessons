# Задание 3.
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort(reverse=True)
    s = my_list[0] + my_list[1]
    return s


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
print(f"Сумма двух наибольших чисел - {my_func(x, y, z)}")
