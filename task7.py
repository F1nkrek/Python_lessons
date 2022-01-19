# Задание 7.
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        res = self.a + self.b + other.a + other.b
        return f"Сумма равна: {self.a} + {self.b} + {other.a} + {other.b} = {res}"

    def __mul__(self, other):
        res = (self.a + self.b) * (other.a + other.b)
        return f"Произведение равно: ({self.a} + {self.b}) * ({other.a} + {other.b}) = {res}"


cn1 = ComplexNumber(4, 5)
cn2 = ComplexNumber(2, 3)
print(cn1 + cn2)
print(cn1 * cn2)
