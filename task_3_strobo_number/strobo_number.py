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
        reverse_number: str = ''
        strobogram_digit = '0689'
        for i in range(len(num) - 1, -1, -1):
            if num[i] in strobogram_digit:
                if num[i] == '6':
                    reverse_number += '9'
                elif num[i] == '9':
                    reverse_number += '6'
                else:
                    reverse_number += num[i]
            else:
                return False
        return num == reverse_number
    except TypeError:
        return "Ожидается строка с целым числом."


"""Тест для стробограмматическое число."""
assert True == is_strobogram_number('86098')

"""Тест для числа, у которого все цифры стробограмматические, но само число не подходит под условие."""

"""Тест не стробограмматического числа."""

"""Тест для строки с буквами, а не числами."""

"""Тест проверяет обработку integer вместо string(такая ошибка возникнет при попытке итерации)."""


class TestInteger(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
            is_strobogram_number(609)


"""
Вопросы:
- нужна обработка входных данных? Раз есть условие, что подается строка с числом, я бы сделала только обработку ошибки) 
"""
