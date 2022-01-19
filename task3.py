# Задание 3.
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class NumberError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.list_of_number = []

    def check_value(self):
        number = None
        while True:
            try:
                try:
                    number = int(input("Введите число: "))
                    self.list_of_number.append(number)
                    print(f"{self.list_of_number}")
                    stop = input(f"Для продолжения нажмите Enter. Для выхода введите 'n': ").lower()
                    if stop == 'n':
                        print(self.list_of_number)
                        break
                except ValueError:
                    raise NumberError
            except NumberError:
                stop = input(f"Вы ввели не число! Для продолжения нажмите Enter. Для выхода введите 'n': ").lower()
                if stop == 'n':
                    print(self.list_of_number)
                    break
                else:
                    self.check_value()


start = TypeCheck()
start.check_value()
