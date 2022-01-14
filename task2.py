# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def square_coat(self):
        return f"Ткань для пальто: {self.size / 6.5 + 0.5 :.2f}"

    def square_costume(self):
        return f"Ткань для костюма: {self.height * 2 + 0.3}"

    @property
    def full_cloth(self):
        return f"Сумма затраченной ткани равна: {self.size / 6.5 + 0.5 + 2 * self.height + 0.3 :.2f}"


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)


class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)


clothes = Clothes(54, 172)
print(f"Размер: {clothes.size}")
print(f"Размер: {clothes.height}")
print(clothes.square_coat())
print(clothes.square_costume())
print(clothes.full_cloth)
