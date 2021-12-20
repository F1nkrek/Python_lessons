# Задание 2
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print("Вводите значения, нажимайте enter. Для окончания ввода просто нажмите enter!")
n = 1
item = int(input(f"Значение {n}: "))
new_List = []
while True:
    try:
        new_List.append(item)
        n = n + 1
        item = int(input(f"Значение {n}: "))
    except:
        break
print(f"Элементов списка: {n-1}")
print(f"Ваш список: {new_List}")

elem = 0
if len(new_List) % 2 == 0:
    while elem < len(new_List):
        new_List[elem], new_List[elem + 1] = new_List[elem + 1], new_List[elem]
        elem += 2
else:
    while elem < len(new_List) - 1:
        new_List[elem], new_List[elem + 1] = new_List[elem + 1], new_List[elem]
        elem += 2
print(f"Ваш список с обенянными переменными: {new_List}")
