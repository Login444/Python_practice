# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Round:
    def __init__(self, radius):
        self.radius = radius


    def length(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*(self.radius**2)


circle = Round(5)
print(circle.length(), circle.area())
