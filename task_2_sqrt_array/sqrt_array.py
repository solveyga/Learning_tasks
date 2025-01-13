"""
Задание:
Дан массив отсортированных целых чисел, надо вернуть отсортированный массив квадратов этих чисел
"""

import unittest


def sqrt_array(int_array: list) -> str:
    """
    Функция принимает массив целых чисел и возвращает отсортированный массив квадратов этих чисел
    sqrt_list - массив переданных значений в квадрате
    """
    try:
        sqrt_list: list = []
        for i in int_array:
            if (i - int(i)) != 0:
                raise ValueError("Допустимы только целые числа")
            else:
                sqrt_list.append(i**2)
        sqrt_list.sort()
        return sqrt_list
    except TypeError:
        return "Ожидается массив целых чисел."
    except ValueError as e:
        return e


"""Тест для целых чисел с повторами значений. Вернутся значения квадратов в порядке возрастания"""
assert [0, 1, 1, 25, 100, 100, 4611686014132420609] == sqrt_array(
    [-10, -1, 0, 1, 5, 10, 2147483647]
)

"""Тест для пустого массива. Вернется пустой ответ (или обработка ошибки)"""
assert [] == sqrt_array([])

"""Тест обработки исключений. Передано число вместо массива."""


class TestInt(unittest.TestCase):
    def test_integer(self):
        with self.assertRaises(TypeError):
            sqrt_array(100)


"""Тест обработки исключений. Передан массив букв вместо целых чисел."""


class TestCharArray(unittest.TestCase):
    def test_char_array(self):
        with self.assertRaises(TypeError):
            sqrt_array(["a", 3])


"""Тест обработки исключений. Передан массив c дробным числом."""


class TestFloat(unittest.TestCase):
    def test_float(self):
        sqrt_array([3.1415])
