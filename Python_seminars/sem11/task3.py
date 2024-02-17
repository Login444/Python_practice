# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# Было:

# class Square:
#     def __init__(self, length, width=None):
#         self.length = length
#         self.width = width if width else length
#
#     def perimeter(self):
#         return 2 * sum(self.length, self.width)
#
#     def area(self):
#         return self.width * self.length

# Стало:
from functools import total_ordering


@total_ordering
class Square:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return 2 * sum(self.length, self.width)

    def area(self):
        return self.width * self.length

    def __add__(self, other):
        if isinstance(other, Square):
            new_length = self.length + other.length
            new_width = self.width + other.width
            return Square(new_length, new_width)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Square):
            if self.length > other.length and self.width > other.width:
                new_length = self.length - other.length
                new_width = self.width - other.width
                return Square(new_length, new_width)
            raise ValueError
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError

    def __str__(self):
        return f'{self.length}, {self.width}'


s1 = Square(1, 2)
s2 = Square(3, 5)
print(s1 + s2)
print(s2 - s1)
print(s1 == s2)
print(s1 != s2)
print(s1 < s2)
print(s1 > s2)
print(s1 >= s2)
print(s1 <= s2)
