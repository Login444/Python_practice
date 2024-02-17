# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
#
# Атрибуты класса:
#
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
#
# Методы класса:
#
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols,
# а также создает двумерный список data размером rows x cols и заполняет его нулями.
#
# __str__(self): Метод, возвращающий строковое представление матрицы.
# Возвращаемая строка представляет матрицу, где элементы разделены пробелами,
# а строки разделены символами новой строки. Например:
#
# 1 2 3
# 4 5 6

# __repr__(self): Метод, возвращающий строковое представление объекта,
# которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.
#
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц.
# Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов,
# а также все элементы равны. Иначе возвращает False.
#
# __add__(self, other): Метод, определяющий операцию сложения двух матриц.
# Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов).
# Если размеры совпадают, создает новую матрицу,
# где каждый элемент равен сумме соответствующих элементов входных матриц.
#
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц.
# Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице.
# Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов
# соответствующей строки из первой матрицы и столбца из второй матрицы.

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row)
            if self.data.index(row) != (len(self.data) - 1):
                matrix_str += "\n"
        return matrix_str

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices should have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix should be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
