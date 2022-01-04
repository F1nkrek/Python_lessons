# Задание 4.
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dictionary_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translate_words = []
try:
    with open("task_4.txt") as origin:
        for line in origin:
            tmp = line.split(" - ")
            if tmp[0] in dictionary_words:
                word = dictionary_words[tmp[0]]
                translate_words.append(word +' - '+ tmp[1])
except IOError:
    print("Произошла ошибка ввода-вывода!")
try:
    with open("task_4_translate.txt", "w", encoding='utf-8') as translate:
        translate.writelines(translate_words)
except IOError:
    print("Произошла ошибка ввода-вывода!")
try:
    with open("task_4.txt") as origin:
        print(origin.read())
        print("Перевод.")
    with open("task_4_translate.txt", encoding='utf-8') as translate:
        print(translate.read())
except IOError:
    print("Произошла ошибка ввода-вывода!")
