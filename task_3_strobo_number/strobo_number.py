import unittest


def is_strobogram_number(num: str) -> bool:
    """
    Функция проверяет, является ли число стробограмматическим, то есть одинаковым при повороте на 180 градусов.
    :param
    num: строка с целым числом, которое нужно проверить
    :return:
    bool: True, если число стробограмматическое
    """
    reverse_digit: list = []
    strobogram_digit: dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    for i in range(
        len(num) - 1, -1, -1
    ):  # можно использовать for item in reversed(num), чтобы работать с элементами, а не индексами, но reversed - встроенная функция
        if num[i] not in strobogram_digit.keys():
            return False
        reverse_digit.append(strobogram_digit[num[i]])
    return num == "".join(reverse_digit)


"""
Позитивные тесты
"""

"""Тест стробограмматического числа из одной цифры"""
assert is_strobogram_number("8")

"""Тест для стробограмматического числа с разными цифрами, в том числе заменой цифры."""
assert is_strobogram_number("1860981")

"""
Критичные негативные тесты
"""

"""Тест для числа, у которого все цифры стробограмматические, но само число не подходит под условие."""
assert False == is_strobogram_number("8061")

"""Тест не стробограмматического числа."""
assert False == is_strobogram_number("9087")

"""
Остальные негативные тесты
"""

"""Тест для строки, которая не является целым числом."""
assert False == is_strobogram_number("860.98")

"""Тест для пустой строки. Вернется True, поскольку нет обработки входных данных, т.к. они гарантированы"""
assert is_strobogram_number("")

"""Тест для ошибки при передаче числа вместо строки с числом."""


class TestInteger(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
            is_strobogram_number(609)
