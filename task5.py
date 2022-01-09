# Задание 5.
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
# (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
# метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

stationery_draw = Stationery()
pen_draw = Pen()
pencil_draw = Pencil()
handle_draw = Handle()
stationery_draw.draw()
pen_draw.draw()
pencil_draw.draw()
handle_draw.draw()
