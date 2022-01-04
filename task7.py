# Задание 7.
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.

import json

firm_dictionary = {}
average_profit_dictionary = {"Средняя прибыль: ": 0}
output_dictionary = [firm_dictionary, average_profit_dictionary]
with open("task_7.txt") as file_firm:
    count = 0
    firms = file_firm.readlines()
    for firm in firms:
        if len(firms):
            firm_name, firm_type, firm_revenue, firm_costs = firm.split()
            firm_profit = int(firm_revenue) - int(firm_costs)
            if firm_profit > 0:
                firm_dictionary[firm_name] = int(firm_profit)
                average_profit_dictionary["Средняя прибыль: "] += firm_profit
                count += 1
    if count:
        i = int(average_profit_dictionary["Средняя прибыль: "] / count)
        average_profit_dictionary["Средняя прибыль: "] = i
        print(f"{json.dumps(output_dictionary, ensure_ascii=False)}\n")
with open("task_7_new.txt", 'w',  encoding='utf-8') as write_file:
    json.dump(output_dictionary, write_file, ensure_ascii=False)
