# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.


from random import choice


class Vehicle:
    _speed: int
    _name: str
    _color: str
    _is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def turn(self):
        return choice(["в лево", "в право", "прямо"])

    def stop(self):
        return "остановилась"

    def show_speed(self):
        return self.speed

    def go(self):
        if self.speed > 0:
            return f"поехала {self.turn()} со скоростю {self.show_speed()}"
        else:
            return self.stop()

    def police(self):
        if self.is_police == True:
            return "Полицейская машина"
        else:
            return "Гражданская машина"


class TownCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"{self.speed} !Превышение скорости!"
        else:
            return self.speed


class SportCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"{self.speed} !Превышение скорости!"
        else:
            return self.speed


class PoliceCar(Vehicle):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(65, "белого", "Toyota", False)
car2 = WorkCar(50, "зеленого", "ГАЗ", False)
car3 = SportCar(250, "красного", "Ferrari", False)
car4 = PoliceCar(0, "спец", "УАЗ", True)
print(f"{car1.police()} {car1.name} {car1.color} цвета, {car1.go()}")
print(f"{car2.police()} {car2.name} {car2.color} цвета, {car2.go()}")
print(f"{car3.police()} {car3.name} {car3.color} цвета, {car3.go()}")
print(f"{car4.police()} {car4.name} {car4.color} цвета, {car4.go()}")
