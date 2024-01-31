# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Square:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return 2 * sum(self.length, self.width)

    def area(self):
        return self.width * self.length


my_square = Square(5, 4)

print(my_square.perimeter())
print(my_square.area())
