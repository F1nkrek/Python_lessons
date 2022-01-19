# Задание 2.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ExceptionZeroDivision(Exception):

    def zero_division(self, divisible, devider):
        try:
            res = round(divisible / devider, 1)
        except ZeroDivisionError:
            print(f"{divisible} / {devider} !на ноль делить нельзя!")
        else:
            print(f"{divisible} / {devider} = {res}")


division = ExceptionZeroDivision()
division.zero_division(10, 2)
division.zero_division(10, 0)
division.zero_division(10, 3)
division.zero_division(0, 3)
