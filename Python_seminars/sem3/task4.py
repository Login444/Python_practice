# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды

my_list = [1, 2, 3, 3, 2, 1, 5]

for item in set(my_list):
    if my_list.count(item) == 2:
        my_list.remove(item)
        my_list.remove(item)

print(my_list)
