# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются.

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# Создадим счетчик count, в который будем складывать все совпадения

count = 0

# Используем итератор:

for i in list1:
    for k in list2:
        if i == k:
            count += 1

print(f'Количество совпадающих чисел: {count}')


