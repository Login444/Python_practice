# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.
import math

task = 'a*x**2 + b*x + c = 0'
print(task)

a = 5
b = 2
c = 4

discriminant = math.pow(b, 2) - (4 * a * c)

if discriminant > 0:
    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f'x1 = {x_1}; x2 = {x_2}')
elif discriminant == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    x_1 = complex(-b, math.sqrt(-discriminant)) / (2 * a)
    x_2 = complex(-b, -math.sqrt(-discriminant)) / (2 * a)
    print(f'x1 = {x_1}; x2 = {x_2}')

