# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


new_names = ['Иван', 'Артем']
new_base = [100000, 50000]
new_bonus = ['10.25%', '12.0%']


def bonus_calculation(names, base, bonus: list):
    result = {}
    for i in range(len(base)):
        result[names[i]] = (base[i] * float(bonus[i][:-1])/100)
    return result


print(bonus_calculation(new_names, new_base, new_bonus))