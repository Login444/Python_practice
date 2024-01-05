# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.


import decimal
import math

decimal.getcontext().prec = 42
DEFAULT = 1000
radius = int(input('Введите радиус: '))
pi = decimal.Decimal(math.pi)
diam = radius * 2

if diam <= DEFAULT:
    result = decimal.Decimal(2 * pi * radius)
    print(result)
else:
    print('Диаметр не должен превышать 1000')
