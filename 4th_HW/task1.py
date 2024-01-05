# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
from copy import deepcopy

matrix_example = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]


def transpose(matrix):
    """
    Мой вариант решения.
    :param matrix:
    :return:
    """
    result = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


transposed_matrix = transpose(matrix_example)

print(transposed_matrix)

# def transpose(matrix):
#     """
#     "Эталонное" решение
#     :param matrix:
#     :return:
#     """
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed

