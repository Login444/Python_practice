# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов.
import string

text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"


text = text.lower()

for i in range(len(text)):
    if text[i] in string.punctuation:
        text = text.replace(text[i], " ")

text = text.split()

my_set = set(text)

result = []
result_two = []
result_one = []

for i in my_set:
    if i not in string.digits:
        if text.count(i) > 2:
            my_tup = (i, text.count(i))
            result.append(my_tup)
        elif text.count(i) == 2:
            my_tup = (i, text.count(i))
            result_two.append(my_tup)
        else:
            my_tup = (i, text.count(i))
            result_one.append(my_tup)


result.sort(reverse=True)
result_two.sort(reverse=True)
result_one.sort(reverse=True)

for i in result_two:
    result.append(i)

for i in result_one:
    result.append(i)

print(result)


# [('lazy', 3), ('the', 2), ('fox', 2), ('dog', 2), ('quick', 1), ('brown', 1), ('jumps', 1), ('over', 1)]

