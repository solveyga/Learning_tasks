import unittest

def missingNumber(nums: list) -> str:
    """
    Функция принимает массив чисел, сортирует его, проверяет пропущенное число в диапазоне [0, n] и возвращает его.
    Ключевые параметры:
    expected_num - число со значением, равным индексу числа из массива.
    """
    try:
        nums.sort()
        if nums[-1] > len(nums):
            raise ValueError("Функция принимает массив из n чисел в диапазоне [0, n]. Передан массив с числом больше n.")
    except TypeError:
        return "Функция принимает только массив чисел."
    except AttributeError:
        return "Функция принимает только массив чисел."
    except ValueError as e:
        return e
    if nums[-1] != len(nums):
        return f"Пропущено число {len(nums)}"
    elif nums[0] != 0:
        return f"Пропущено число 0"
    for i in range(1, len(nums)):
        expected_num = i
        if nums[i] != expected_num:
            return f"Пропущено число {expected_num}"

"""Тест проверяет обычный массив, в котором не первое и не последнее число."""
assert "Пропущено число 3" == missingNumber([0, 1, 2, 4])

"""Тест проверяет массив с пропущенным нулем."""
assert "Пропущено число 0" == missingNumber([3, 1, 2, 4])

"""Тест проверяет массив с пропущенным максимальным числом."""
assert "Пропущено число 4" == missingNumber([3, 1, 2, 0])

"""Тест исключения, в котором массив содержит число больше длины массива."""
class TestNumberOutside(unittest.TestCase):
    def test_number_outside(self):
        with self.assertRaises(ValueError):
            missingNumber[2]

"""Тест исключения, в котором передан не массив"""
class TestNumber(unittest.TestCase):
    def test_number_instead_list(self):
        with self.assertRaises(AttributeError):
            missingNumber(3)

"""Тест исключения, в котором передан массив, но его элементы - не числа"""
class TestNumber(unittest.TestCase):
    def test_number_instead_list(self):
        with self.assertRaises(TypeError):
            missingNumber(['0', '2'])
"""
Вопрос: нужна ли обработка для дробных чисел?
А для целых отрицательных?
"""


