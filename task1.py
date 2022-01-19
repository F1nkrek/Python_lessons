# Задание 1.
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, day=1, month=1, year=1999):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        print(f"classmethod - {cls}, {day:02}.{month:02}.{year:04}")

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 9999:
            print(f"staticmethod - {day:02}.{month:02}.{year:04}")
            return day, month, year
        else:
            print(f"staticmethod - {day:02}.{month:02}.{year:04} Не верная дата!")


date = "18-01-2022"
date_incorrect = "18-22-2022"
Date.from_string(date)
Date.is_date_valid(date)
Date.is_date_valid(date_incorrect)
