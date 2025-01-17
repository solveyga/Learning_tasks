"""
Написать и протестировать функцию, которая:
- принимает на вход строку
- возвращает списки кириллических гласных и согласных
"""

import unittest


def letters_in_string(input_value: str) -> str:
    """
    Функция принимает строку, проверяет максимально допустимую длину, выбирает из строки уникальные гласные и согласные и возвращает их список пользователю.

    Ключевые аргументы:
    vowels -- все кириллические гласные
    consonants -- все кириллические согласные
    uniq_letters - уникальные буквы в переданной строке
    vowels_in_string - гласные в переданной строке
    consonants_in_string - согласные в переданной строке
    """
    try:
        input_string: str = input_value.lower()
        if len(input_string) > 256:
            raise ValueError("Допустимы строки не длиннее 256 символов.")
    except AttributeError:
        return "Ожидается строка."
    except ValueError as e:
        return e
    else:
        input_string: str = (str(input_value)).lower()
        uniq_letters: set = set(input_string)
        vowels: str = "аеиоуыэюяё"
        consonants: str = "бвгджзйклмнпрстфхцчшщ"
        vowels_in_string: list = []
        consonants_in_string: list = []
        for i in uniq_letters:
            if i in vowels:
                vowels_in_string.append(i)
            elif i in consonants:
                consonants_in_string.append(i)
        vowels_in_string.sort()
        consonants_in_string.sort()

        if vowels_in_string:
            vowels_result: str = f"Список гласных: {', '.join(list(vowels_in_string))}."
        elif not vowels_in_string:
            vowels_result: str = "Нет кириллических гласных."

        if consonants_in_string:
            consonants: str = (
                f"Список согласных: {', '.join(list(consonants_in_string))}."
            )
        elif not consonants_in_string:
            consonants: str = "Нет кириллических согласных."

        return f"{vowels_result}\n{consonants}"


"""Тест фразы, которая содержит все буквы алфавита. Вернутся все буквы."""
assert (
    f"Список гласных: а, е, и, о, у, ы, э, ю, я, ё.\nСписок согласных: б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ."
    == letters_in_string("Съешь ещё этих мягких французских булок, да выпей же чаю.")
)

"""Тест пустой строки. Нет искомых букв."""
assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_in_string(
    ""
)

"""Тест строки без кириллических символов. Нет искомых букв."""
assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_in_string(
    "The quick brown fox jumps over the lazy dog いろはにほへと 1234567890"
)

"""Тест строки с гласными буквами. Вернутся гласные буквы, согласных нет."""
assert f"Список гласных: а, о, у.\nНет кириллических согласных." == letters_in_string(
    "А о у"
)

"""Тест строки с согласными буквами. Вернутся согласные буквы, гласных нет."""
assert f"Нет кириллических гласных.\nСписок согласных: г, д, ж." == letters_in_string(
    "Гд ж"
)

"""Тест слишком длинной строки. Вернется предупреждение о превышении длины"""


class TestOverlenght(unittest.TestCase):
    def test_overlength(self):
        with self.assertRaises(ValueError):
            letters_in_string(
                "jvraGUOLARUHJvHZcuMcOzeqWsYugmwwjZGSvRJPVxOciGfmbfbPPyEfyiAGSYTdgppNkdrjGzyxcObtFAbYnCzkuQoPJtdfWaCbWJbuejqvFgnMqeQhenUAZcLJIRKJNjvPeKASymaavUYGTjeJHJGNLpyYvnLJTibYVKEZaFjaWXQIRuAMVBsxeqwrAScgztBbyiSxYqevGLFRXpVqCuKCIPkEMsCCJNFpsMXcKUOdwglUExxTsuhMsmTfFgvGOxIe"
            )


"""Тест строки с булевым значением. Искомых букв нет."""


class TestBoolean(unittest.TestCase):
    def test_boolean(self):
        with self.assertRaises(AttributeError):
            letters_in_string(True)


"""Тест строки с числовым значением. Искомых букв нет."""


class TestInteger(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(AttributeError):
            letters_in_string(123)
