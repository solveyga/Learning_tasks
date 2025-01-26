import unittest
import pytest

def missingNumber(nums: list) -> str:
    """
    Функция принимает массив чисел, сортирует его, проверяет пропущенное число в диапазоне [0, n] и возвращает его.
    :param
    nums - полученный массив с n числами
    :returns
    str - ответ с пропущенным числом
    """
    n = len(nums)
    full_sum = n*(n+1) // 2
    nums_sum = sum(nums)
    return f"Пропущено число {full_sum - nums_sum}."


"""
Позитивные тесты
"""
"""Тест проверяет обычный массив, в котором пропущено не первое и не последнее число."""
assert "Пропущено число 3." == missingNumber([0, 1, 2, 4])

"""Тест проверяет массив с пропущенным нулем. Числа расположены в обратном порядке."""
assert "Пропущено число 0." == missingNumber([4, 3, 2, 1])

"""Тест проверяет массив с пропущенным максимальным числом."""
assert "Пропущено число 4." == missingNumber([3, 1, 2, 0])

"""Тест проверяет минимальный массив, в котором пропущено минимальное число"""
assert "Пропущено число 0." == missingNumber([1])

"""Тест проверяет минимальный массив, в котором пропущено масимальное число"""
assert "Пропущено число 1." == missingNumber([0])

"""
Критичные негативные тесты
"""

"""Тест исключения, в котором передан не массив"""
class TestNumber(unittest.TestCase):
    def test_number_instead_list(self):
        with self.assertRaises(AttributeError):
            missingNumber(3)

"""Тест исключения, в котором передан массив, но его элементы - не числа"""
class TestNumber(unittest.TestCase):
    def test_number_instead_list(self):
        with self.assertRaises(TypeError):
            missingNumber([0, 2])

"""
Остальные негативные тесты
"""

"""Тест необрабатываемого случая, в котором массив содержит число больше своей длины."""
assert "Пропущено число -1." == missingNumber([2])


"""Тест с вещественными числами. Функция не обрабатывает гарантируемый ввод, поэтому результат может быть неожиданным."""
assert "Пропущено число -0.5." == missingNumber([1.0, 2.5])

"""Тест с дублирующимися данными. Обработка такого не добавлена в функцию."""
assert "Пропущено число 2." == missingNumber([1, 1, 2])

"""Тест пустого массива. В функции нет обработки входных данных."""
assert "Пропущено число 0." == missingNumber([])

"""Тест массива со значение None."""
class TestNone(unittest.TestCase):
    def test_number_instead_list(self):
        with self.assertRaises(TypeError):
            missingNumber([None])




