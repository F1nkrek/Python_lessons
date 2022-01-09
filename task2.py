# Задание 2.
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т.

class Road:
    _length: int
    _width: int
    _default_thickness: int = 5
    _std_mass_kub_centimeter: int = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self._default_thickness * self._std_mass_kub_centimeter / 1000
        print(f"Масса асфальта: {self._width}м*{self._length}м*{self._default_thickness}см*{self._std_mass_kub_centimeter}кг = {asphalt_mass:.2f} т.")


road1 = Road(5000, 20)
road2 = Road(10000, 10)
road3 = Road(20000, 30)
road1.asphalt_mass()
road2.asphalt_mass()
road3.asphalt_mass()
