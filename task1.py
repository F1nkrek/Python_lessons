# Задание 1.
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task_1.txt", "w") as data_write:
    while True:
        text = input("Введите любой текст, при окончании оставте пустую строку: ")
        data_write.write(text + '\n')
        if text == "":
            break
with open("task_1.txt") as data_read:
    print(data_read.read())
