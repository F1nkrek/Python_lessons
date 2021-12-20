# Задание 6
# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

products = []
number = 1
name_Product, price, quantity = None, None, None
while True:
    if name_Product is None:
        tmp = input("Введите название товара: ")
        if not tmp.isalnum():
            print("Наименование товара не может быть пустым. Попробуйте еще раз!")
            continue
        name_Product = tmp

    if price is None:
        tmp = input("Введите стоимость товара: ")
        if not tmp.isdigit():
            print("Цена должна быть целым числом. Попробуйте еще раз!")
            continue
        price = int(tmp)

    if quantity is None:
        tmp = input("Введите количество: ")
        if not tmp.isdigit():
            print("Количество должно быть целым числом. Попробуйте еще раз!")
            continue
        quantity = int(tmp)

    item = {'Наименование': name_Product, 'Цена': price, 'Колличество': quantity}
    product = (number, item)
    products.append(product)
    name_Product, price, quantity = None, None, None
    number += 1
    print(*products, sep="\n")
    finish = input("Для продолжения формирования списка нажмите (Enter), если формирование списка закончено, "
                   "то нажмите (y): ")
    if finish.lower() == 'y' or 'Y' or 'н' or 'Н':
        break
print("[")
print(*products, sep="\n")
print("]")
