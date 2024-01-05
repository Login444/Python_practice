# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_calc(nums: list, a, b: int):
    return sum(nums[a:b+1])


print(sum_calc([1, 2, 3, 4, 5], -2, 4))