# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]

new_list = []

for i in lst:
    if lst.count(i) > 1:
        new_list.append(lst.pop(lst.index(i)))
new_set = set(new_list)

second_list = []

for i in new_set:
    second_list.append(i)

print(second_list)
