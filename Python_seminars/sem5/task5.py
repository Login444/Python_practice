# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение

result_1 = ['FizzBuzz' if i %3 ==0 and i % 5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(1,101)]

result_2 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0:
        result_2.append('FizzBuzz')
    elif i % 5 == 0:
        result_2.append('Buzz')
    elif i % 3 == 0:
        result_2.append('Fizz')
    else:
        result_2.append(i)
print(result_2)
print(result_1)
