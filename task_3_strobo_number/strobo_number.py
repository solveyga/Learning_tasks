import unittest


def is_strobogram_number(num: str) -> bool:
    """
    Функция принимает строку с целым числом и возвращает True, если число стробограмматическое.
    Ключевые аргументы:
    num - строка с целым числом, которую принимает функция
    reverse_number - num с поворотом на 180 градусов
    strobogram_digit - стробограмматические цифры
    """
    try:
        reverse_number: str = ""
        strobogram_digit: str = "018"
        for i in range(len(num) - 1, -1, -1):
            if num[i] in strobogram_digit:
                reverse_number += num[i]
            elif num[i] == "6":
                reverse_number += "9"
            elif num[i] == "9":
                reverse_number += "6"
            else:
                return False
        return num == reverse_number
    except TypeError:
        return "Ожидается строка с целым числом."


"""Тест для стробограмматическое число."""
assert is_strobogram_number("1860981")

"""Тест для числа, у которого все цифры стробограмматические, но само число не подходит под условие."""
assert False == is_strobogram_number("8061")

"""Тест не стробограмматического числа."""
assert False == is_strobogram_number("9087")

"""Тест для строки, которая не является целым числом."""
assert False == is_strobogram_number("860.98")

"""Тест проверяет обработку integer вместо string."""


class TestInteger(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
            is_strobogram_number(609)


"""
Вопросы:
1. Нужна ли обработка входных данных? Раз есть условие, что подается строка с числом, я бы сделала только обработку ошибки) 
2. В решении литкода 1 считается стробограмматической. Я не нашла определения стробограм. цифр в сети, так что это выглядит как допущение.
"""
