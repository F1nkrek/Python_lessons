n = int(input("Введите число: "))
tmp = n % 10
n = n // 10
while n > 0:
    if n % 10 > tmp:
        tmp = n % 10
    else:
        n = n // 10
print(tmp)