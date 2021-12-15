revenue = int(input("Введите величину выручку: "))
cost = int(input("Введите величину издержек: "))
if revenue > cost:
    profit = revenue - cost
    print(f"Доход составил: {profit}!")
    print(f"Рентабельность: {revenue/profit:.2%}!")
    staff = int(input("Введите число сотрудников: "))
    print(f"Прибыль на сотрудника: {profit/staff}")
elif revenue == cost:
    print("Сработали в 0")
else:
    print(f"Издержки больше выручки на {cost - revenue}!")