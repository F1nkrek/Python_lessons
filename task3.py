# Задание 3.
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    data_dictionary = {}
    average_salary = 0
    tmp = 0
    with open("task_3.txt", encoding='utf-8') as database:
        for line in database:
            key, value = line.split()
            data_dictionary[key] = value
            average_salary += int(value)
            tmp += 1
            if int(value) < 20000:
                print(f"{key} - { data_dictionary[key]}")
    print(f"Средняя зарплата сотрудникоа: {int(average_salary/tmp)}")
except IOError:
    print("Нет такого файла!")

