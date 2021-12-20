# Задание 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

# number = int(input("Введите число: "))
# rating = [7, 5, 3, 3, 2, number]
# my_rating(reverse=True)
# print(rating)

number = int(input("Введите число: "))
rating = [6, 7, 4, 3, 3, 2]
tmp = rating.count(number)
for element in rating:
    if tmp > 0:
        i = rating.index(number)
        rating.insert(i+tmp, number)
        break
    else:
        if number > element:
            j = rating.index(element)
            rating.insert(j, number)
            break
        elif number < rating[len(rating) - 1]:
            rating.append(number)
print(rating)
