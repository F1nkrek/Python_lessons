# Задание 5.
# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

values = []


def sum_values(num):

    sum_of_numbers = 0
    values.extend(num)
    print(values)
    for n in values:
        sum_of_numbers += int(n)
    print(sum_of_numbers)


while True:
    new_values = input("Введите целые числа через пробел и нажмите 'Enter', чтобы посчитать. При окончании ввода, "
                       "введите символ 'q': ")
    numbers = new_values.split()
    if numbers[len(numbers) - 1] == "q":
        numbers.remove("q")
        sum_values(numbers)
        break
    else:
        sum_values(numbers)
