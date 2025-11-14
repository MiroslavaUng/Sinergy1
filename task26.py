class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)   # вызов родительского конструктора

    # переопределение метода
    def seating_capacity(self, capacity=50):
        return f'Вместимость одного автобуса {self.name}: {capacity} пассажиров'

# создание объекта
a = Autobus('Renaul Logan', 180, 12)

# вызов метода
print(a.seating_capacity())