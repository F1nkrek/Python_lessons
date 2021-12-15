a = float(input("В первый день пробежал: "))
b = float(input("Необходимо пробежать не менее: "))
day = 1
print(f"В день {day} пробежал {a} км")
if a > b:
    print(f"В день {day} пробежал {a} км")
else:
    while a < b:
        a = a + a/10
        day += 1
        print(f"В день {day} пробежал {a:.2f} км")
print(f"Итого потребовалось {day}, чтобы добиться результата")