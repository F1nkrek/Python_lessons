# Задание 5.
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

try:
    with open("task_5.txt", "w") as file_with_numbers:
        for i in range(10):
            file_with_numbers.write(str(random.randint(5, 50)) + " ")
    with open("task_5.txt") as file_with_numbers:
        numbers = file_with_numbers.readline()
        print(numbers)
        sum_number = 0
        for i in numbers.split():
            sum_number += int(i)
        print(f"Сумма чисел: {sum_number}")
    with open("task_5.txt", "a", encoding='utf-8') as file_with_numbers:
        file_with_numbers.write(f"\nСумма чисел: {str(sum_number)}")
except IOError:
    print("Нет такого файла!")
