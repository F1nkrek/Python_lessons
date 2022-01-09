# Задание 3.
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


worker1 = Position("Иван", "Иванов", "Директор", 100000, 50000)
worker2 = Position("Сергей", "Смирнов", "Бухгалтер", 60000, 20000)
worker3 = Position("Анна", "Сидорова", "Кадровик", 40000, 10000)
worker4 = Position("Андрей", "Петров", "Менеджер", 20000, 20000)

print(f"Рабочий: {worker1.get_full_name()}\nДолжность: {worker1.position}\nЗарплата: {worker1.get_total_income()}\n")
print(f"Рабочий: {worker2.get_full_name()}\nДолжность: {worker2.position}\nЗарплата: {worker2.get_total_income()}\n")
print(f"Рабочий: {worker3.get_full_name()}\nДолжность: {worker3.position}\nЗарплата: {worker3.get_total_income()}\n")
print(f"Рабочий: {worker4.get_full_name()}\nДолжность: {worker4.position}\nЗарплата: {worker4.get_total_income()}")
