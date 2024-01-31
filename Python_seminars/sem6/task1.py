# � Вспомните какие модули вы уже проходили на курсе.
# � Создайте файл, в котором вы импортируете встроенные в
# модуль функции под псевдонимами. (3-7 строк импорта).

from random import randint as randomizer
from math import sqrt as square
from math import pow as multi

number = randomizer(1,10)
print(square(number))
print(multi(number, square(number)))
