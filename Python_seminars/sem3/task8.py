# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

friends_stuff = {
    'Олег': ('палатка', 'топор', 'еда', 'пиво'),
    'Игорь': ('палатка', 'вилка', 'вода', 'пиво'),
    'Гусь': ('палатка', 'топор', 'вода', 'пиво'),
    'Стоун': ('палатка', 'топор', 'вода', 'лимонад')
}

set1 = set()

for i in friends_stuff:
    if not set1:
        set1 = set(friends_stuff[i])
    else:
        set1 &= set(friends_stuff[i])

print(f'У всех есть: {set1}')

my_tuple = friends_stuff.keys()

my_set = set()
for j in my_tuple:
    my_set = set(friends_stuff[j])
    for other in [i for i in my_tuple if i != j]:
        my_set = my_set - set(friends_stuff[other])
    if my_set:
        print(f'Только у {j} есть уникальная вещь: {my_set}')

for j in my_tuple:
    my_set = set()
    to_remove = set(friends_stuff[j])
    for other in [i for i in my_tuple if i != j]:
        if not my_set:
            my_set = set(friends_stuff[other])
        else:
            my_set = my_set & set(friends_stuff[other])
    my_set -= to_remove
    if my_set:
        print(f'У {j} нет: {my_set}')
