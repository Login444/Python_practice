# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

def convert_to_base(number: int, base: int):
    result = ''
    while number > 0:
        if base <= 9:
            result = str(number % base) + result
            number = number // base
        elif base <= 16:
            base_dictionary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            remainder = number % base
            if remainder > 9:
                result = str(base_dictionary.get(remainder)) + result
                number = number // base
    return result


def convert_to_base_hex(number: int):
    result = ''
    base_dictionary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number > 0:
        remainder = number % 16
        if remainder > 9:
            result = str(base_dictionary.get(remainder)) + result
            number = number // 16
        else:
            result = str(remainder) + result
            number = number // 16
    return result


num = int(input('Введите целое число: '))
print(convert_to_base_hex(num))
print(hex(num))
