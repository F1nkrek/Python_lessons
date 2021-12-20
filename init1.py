# Задание 1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

test_List = ['abc', '1', 2, 3.5]
test_Tuple = ('abc', 123, 8.5)
test_Dictionary = {'name': 'Ivan', 'age': '25'}
test_United_List = [test_List, test_Tuple, test_Dictionary]

for element in test_United_List:
    print(f"{element} тип {type(element)}")
    for item in element:
        print(f"    {item} - тип {type(item)}")
    print()
