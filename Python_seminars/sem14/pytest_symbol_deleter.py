import pytest
from string import ascii_lowercase

ascii_lowercase += " "


def symbol_deleter(text: str):
    if not isinstance(text, str):
        raise ValueError
    return ''.join([i.lower() for i in text if i.lower() in ascii_lowercase])


def test_no_change():
    assert symbol_deleter('something string') == 'something string', 'Внесены изменения'


def test_lower_case():
    assert symbol_deleter('SOMETHING STRING') == 'something string', 'Не весь результат в нижнем регистре'


def test_punctuation():
    assert symbol_deleter('something string!') == 'something string', 'Не убраны знаки препинания'


def test_another_alphabet():
    assert symbol_deleter('something stringбуквы') == 'something string', 'Остались буквы другого алфавита'


def test_all():
    assert symbol_deleter('SOMETHING,буквы, sTring!!!') == 'something string', 'Что то не сработало'


if __name__ == '__main__':
    pytest.main(['-v'])
