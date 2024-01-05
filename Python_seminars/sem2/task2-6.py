# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

account_sum = 0
count_of_operation = 0


def choice_true_false() -> bool:
    """
    Функция подтверждения либо отклонения операции
    :return:
    """
    answer = int(input('1.Да\n'
                       '2.Нет\n'))
    if answer == 1:
        return True
    else:
        return False


def add_money(money_sum: float, count: int) -> float:
    """
    Функция для пополнения счета
    :param money_sum: текущий остаток на счете
    :param count: счетчик операций (за каждую 3-ю начисляется 3% на остаток)
    :return: конечный остаток на счете после выполнения операции
    """
    if money_sum > 5000000:
        money_sum = money_sum * 0.9
    cash = int(input('Укажите сумму пополнения: '))
    while (cash % 50) != 0:
        difference = 50 - (cash % 50)
        if difference >= 25:
            print(f'Сумма пополнения должна быть кратная 50 у.е.\n'
                  f'Рекомендуем увеличить сумму пополнения на {50 - difference} у.е.\n'
                  f'Изменить сумму?')
            if choice_true_false():
                cash = int(input('Укажите сумму пополнения: '))
            else:
                return money_sum
        else:
            print(f'Сумма пополнения должна быть кратная 50 у.е.\n'
                  'Рекомендуем уменьшить сумму на {difference} у.е.\n'
                  'Изменить сумму?')
            if choice_true_false():
                cash = int(input('Укажите сумму пополнения: '))
            else:
                return money_sum
    new_money_sum = money_sum + cash
    if (count % 3) == 0:
        new_money_sum_plus_percent = new_money_sum * 0.03
        return new_money_sum_plus_percent
    return new_money_sum


def take_money(money_sum: float, count: int) -> float:
    """
    Функция для снятия наличных со счета
    :param money_sum: текущий остаток на счете
    :param count: счетчик операций (за каждую 3-ю начисляется 3% на остаток)
    :return: конечный остаток на счете после выполнения операции
    """
    if money_sum > 5000000:
        money_sum = money_sum * 0.9
    cash = int(input('Укажите сумму снятия: '))
    while (cash % 50) != 0:
        difference = 50 - (cash % 50)
        if difference >= 25:
            print(f'Сумма снятия должна быть кратная 50 у.е.\n'
                  f'Рекомендуем увеличить сумму снятия на {50 - difference} у.е.\n'
                  f'Изменить сумму?')
            if choice_true_false():
                cash = int(input('Укажите сумму снятия: '))
            else:
                return money_sum
        else:
            print(f'Сумма снятия должна быть кратная 50 у.е.\n'
                  f'Рекомендуем уменьшить сумму на {difference} у.е.\n'
                  f'Изменить сумму?')
            if choice_true_false():
                cash = int(input('Укажите сумму снятия: '))
            else:
                return money_sum
    if cash > money_sum:
        print(f'Вы не можете снять сумму больше чем на счете.\n'
              f'Ваш баланс: {money_sum}')
        return money_sum
    new_money_sum = money_sum - percentage(cash)
    if (count % 3) == 0:
        new_money_sum_plus_percent = new_money_sum * 0.03
        return new_money_sum_plus_percent
    return new_money_sum


def percentage(cash: int) -> float:
    """
    Функция для вычисления суммы комиссии за снятие наличных
    :param cash: сумма снятия наличных
    :return: комиссия за снятие
    """
    min_percent = 30.0
    max_percent = 600.0
    percent = cash * 0.015
    if percent < 30:
        return min_percent
    elif percent > 600:
        return max_percent
    else:
        return percent


