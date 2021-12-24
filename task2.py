# Задание 2.
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, y_birth, city, email, phone):
    return print(f"{name} {surname} {y_birth} {city} {email} {phone}")


user(name="Ivan", surname="Ivanov", y_birth=1989, city="MSK", email="ivan@gmail.com", phone=89999999999)
