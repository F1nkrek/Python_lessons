# Задание 3.
# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:

    def __init__(self, nucleus):
        self.nucleus = int(nucleus)

    def __add__(self, other):
        return f"При сложении клеток, в ней стало {self.nucleus + other.nucleus} ячеек"

    def __sub__(self, other):
        return f"При вычитании клеток, в ней стало {self.nucleus - other.nucleus} ячеек"

    def __truediv__(self, other):
        return f"При делении клеток, в ней стало {self.nucleus // other.nucleus} ячеек"

    def __mul__(self, other):
        return f"При умножении клеток, в ней стало {self.nucleus * other.nucleus} ячеек"

    def make_order(self, row):
        result = ''
        for i in range(int(self.nucleus / row)):
            result += '*' * row + '\n'
        result += '*' * (self.nucleus % row) + '\n'
        return result


cell = Cell(25)
cell_2 = Cell(7)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(f"\nКоличество ячеек:\n{cell.make_order(8)}")
