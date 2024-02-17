# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest
from symbol_deleter import symbol_deleter


class MyTest(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(symbol_deleter('something string'), 'something string')

    def test_lower_case(self):
        self.assertEqual(symbol_deleter('SOMETHING STRING'), 'something string')

    def test_punctuation(self):
        self.assertEqual(symbol_deleter('something string!'), 'something string')

    def test_another_alphabet(self):
        self.assertEqual(symbol_deleter('something stringбуквы'), 'something string')

    def test_all(self):
        self.assertEqual(symbol_deleter('SOMETHING,буквы, sTring!!!'), 'something string')


if __name__ == '__main__':
    unittest.main(verbosity=2)
