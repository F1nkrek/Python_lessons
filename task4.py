# Задание 4, 5, 6.
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class OfficeEquipment:

    def __init__(self, name, model):
        self.name = name
        self.model = model


class Printer(OfficeEquipment):
    count = 0

    def __init__(self, name, model, type_printer, quantity):
        super().__init__(name, model)
        self.quantity = quantity
        self.type_printer = type_printer
        Printer.count += quantity

    @staticmethod
    def names():
        return f"Принтеры: {Printer.count}"

    def type_printer(self):
        return self.type_printer

    def count_printer(self):
        return Printer.count

    def __str__(self):
        return f"\t\tНаименование: {self.name}" f"\t\tМодель: {self.model}" f"\t\tТип: {self.type_printer}" f"\t\tКоличество: {self.quantity} шт "


class Scaner(OfficeEquipment):
    count = 0

    def __init__(self, name, model, type_scan, quantity):
        super().__init__(name, model)
        self.quantity = quantity
        self.type_scan = type_scan
        Scaner.count += quantity

    @staticmethod
    def names():
        return "Сканеры:"

    def type_scan(self):
        return self.type_scan

    def count_scan(self):
        return self.count

    def __str__(self):
        return f"\t\tНаименование: {self.name}" f"\t\tМодель: {self.model}" f"\t\tТип: {self.type_scan}" f"\t\tКоличество: {self.quantity} шт"


class Xerox(OfficeEquipment):
    count = 0

    def __init__(self, name, model, type_xerox, quantity):
        super().__init__(name, model)
        self.quantity = quantity
        self.type_xerox = type_xerox
        Xerox.count += quantity

    @staticmethod
    def names():
        return "Ксероксы:"

    def type_xerox(self):
        return self.type_xerox

    def count_xerox(self):
        return self.count

    def __str__(self):
        return f"\t\tНаименование: {self.name}" f"\t\tМодель: {self.model}" f"\t\tТип: {self.type_xerox}" f"\t\tКоличество: {self.quantity} шт "


class OfficeEquipmentWarehouse:
    count_warehouse = 40

    def unit_count(self):
        unit_count = Printer.count + Scaner.count + Xerox.count
        return unit_count

    def free_spase(self):
        free_space = self.count_warehouse - self.unit_count()
        if free_space < 0:

            return f"закончилось. {self.unit_count() - self.count_warehouse} единиц перемещено на другой склад."
        else:
            return free_space

    def __str__(self):
        return f"Склад рамером на {self.count_warehouse}. Занято: {self.unit_count()}. Свободное место {self.free_spase()}"


s = OfficeEquipmentWarehouse()
printer1 = Printer("Canon", "MF3010", "ч/б", 3)
printer2 = Printer("Epson", "L802", "цветной", 2)
printer3 = Printer("HP", "P1102", "ч/б", 3)
print(printer1.names())
print(printer1.__str__())
print(printer2.__str__())
print(printer3.__str__())
print(f"Итого на складе: {printer1.count} шт.")

scaner1 = Scaner("Canon", "lide110", "планшетный", 1)
scaner2 = Scaner("Epson", "DS870", "поточный", 2)
print(scaner1.names())
print(scaner1.__str__())
print(scaner2.__str__())
print(f"Итого на складе: {scaner1.count} шт.")

xerox1 = Xerox("Ricoh", "MP2014", "A3", 5)
xerox2 = Xerox("Canon", "2206iF", "A3", 3)
xerox3 = Xerox("Sharp", "AR7024", "A3", 1)
xerox4 = Xerox("Kyosera", "FS1020", "A4", 2)
print(xerox1.names())
print(xerox1.__str__())
print(xerox2.__str__())
print(xerox3.__str__())
print(xerox4.__str__())
print(f"Итого на складе: {xerox1.count} шт.")
warehouse = OfficeEquipmentWarehouse()
print(warehouse.__str__())
