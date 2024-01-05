# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним,
# только если треугольник существует .

a = int(10)
b = int(4)
c = int(5)


def triangle_type(a, b, c):
    if a == b and a == c:
        print('Треугольник равносторонний')
    elif a == b or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')


def triangle_is_valid(a, b, c):
    """

    :param a: сторона треугольника
    :param b: сторона треугольника
    :param c: сторона треугольника
    :return: False - если треугольник не существует. True - если треугольник существует
    """

    if a > b + c:
        return False
    elif b > a + c:
        return False
    elif c > a + b:
        return False
    else:
        return True


if triangle_is_valid(a, b, c):
    print('Треугольник существует')
    triangle_type(a, b, c)
else:
    print('Треугольник не существует')