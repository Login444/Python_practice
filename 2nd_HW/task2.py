# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.
import fractions


frac1 = "1/2"
frac2 = "1/3"

middle_frac1 = frac1.index('/')
middle_frac2 = frac2.index('/')
num_frac1 = int(frac1[:middle_frac1])
num_frac2 = int(frac2[:middle_frac2])
denom_frac1 = int(frac1[middle_frac1+1:])
denom_frac2 = int(frac2[middle_frac2+1:])


def sum_frac(num_frac1: int, denom_frac1: int, num_frac2: int, denom_frac2: int):
    if denom_frac1 != denom_frac2:
        numerator = (num_frac1 * denom_frac2) + (num_frac2 * denom_frac1)
        denumerator = denom_frac1 * denom_frac2
        result = str(numerator) + '/' + str(denumerator)
    else:
        result = str(num_frac1 + num_frac2) + '/' + str(denom_frac1)
    return result


def multi_frac(num_frac1: int, denom_frac1: int, num_frac2: int, denom_frac2: int):
    if denom_frac1 != denom_frac2:
        numerator = num_frac1 * num_frac2
        denumerator = denom_frac1 * denom_frac2
        result = str(numerator) + '/' + str(denumerator)
    else:
        result = str(num_frac1 * num_frac2) + '/' + str(denom_frac1 * denom_frac2)
    return result


print(f'Сумма дробей: {sum_frac(num_frac1, denom_frac1, num_frac2, denom_frac2)}')
print(f'Произведение дробей: {multi_frac(num_frac1, denom_frac1, num_frac2, denom_frac2)}')

f1 = fractions.Fraction(num_frac1, denom_frac1)
f2 = fractions.Fraction(num_frac2, denom_frac2)

print(f'Сумма дробей: {f1+f2}')
print(f'Произведение дробей: {f1*f2}')
