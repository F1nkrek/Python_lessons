# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

months_List = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
               'Декабрь']
seasons_Dictionary = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц по номеру: "))
if month == 12 or month == 1 or month == 2:
    print(f"Месяц {months_List[month - 1]}, {seasons_Dictionary.get(1)}")
elif month == 3 or month == 4 or month == 5:
    print(f"Месяц {months_List[month - 1]}, {seasons_Dictionary.get(2)}")
elif month == 6 or month == 7 or month == 8:
    print(f"Месяц {months_List[month - 1]}, {seasons_Dictionary.get(3)}")
elif month == 9 or month == 10 or month == 11:
    print(f"Месяц {months_List[month - 1]}, {seasons_Dictionary.get(4)}")
else:
    print("Такого месяца не существует!")
