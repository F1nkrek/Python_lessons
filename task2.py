# Задание 2.
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("task_2.txt", "w") as text_file:
    str_list = ["Я помню чудное мнгоновенье:\n", "Передо мной явилась ты,\n", "Как мимолетное виденье,\n", "Как гений "
                                                                                                           "чистой "
                                                                                                           "красоты.\n"]
    text_file.writelines(str_list)
with open("task_2.txt") as text_file:
    string_count = 0
    for line in text_file:
        string_count += 1
        words = 0
        tmp = 0
        for word in line:
            if word != ' ' and tmp == 0:
                words += 1
                tmp = 1
            elif word == ' ':
                tmp = 0
        print(line.replace("\n", ""), "-", words, "слова")
    print("Количество строк в файле:", string_count, "строки")
