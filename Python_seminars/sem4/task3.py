# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def new(nums: str):
    new_dict = {}
    nums = list(map(int, nums.split()))
    for item in range(min(nums), max(nums) + 1):
        new_dict[chr(item)] = item
    return new_dict


text = '578 600'
print(new(text))
