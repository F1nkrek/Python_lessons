seconds = int(input("Введите число секунд: "))
if seconds > 0:
    hour = seconds // 3600
    if hour < 10:
        hour = str(0) + str(hour)
    seconds = seconds % 3600
    minute = seconds // 60
    if minute < 10:
        minute = str(0) + str(minute)
    seconds = seconds % 60
    if seconds < 10:
        seconds = str(0) + str(seconds)
    print(f"{hour}:{minute}:{seconds}")
else:
    print("Некорректная запись!")
