# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_gen(limit):
    count = 0
    num = 2
    while count < limit:
        is_simple = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_simple = False
                break
        if is_simple:
            yield num
            count += 1
        num += 1


for prime in simple_gen(5):
    print(prime)
