# Задание 2
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

list_of_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_of_numbers_mod = []
print(list_of_numbers)
for i in range(1, len(list_of_numbers)):
    if list_of_numbers[int(i)] > list_of_numbers[int(i-1)]:
        list_of_numbers_mod.append(list_of_numbers[i])
print(list_of_numbers_mod)