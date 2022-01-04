# Задание 6.
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) — Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("task_6.txt", encoding='utf-8') as subjects_file:
    subjects_dictionary = {}
    subjects = subjects_file.readlines()

    for subject in subjects:
        if len(subject):
            subject = subject.split()
            hours_subject_sum = 0
            for hours_subject in subject[1:]:
                if len(hours_subject) > 1:
                    hours_subject_sum += int(hours_subject.split('(')[0])
            subjects_dictionary[subject[0]] = hours_subject_sum
    print(f"{subjects_dictionary}")
