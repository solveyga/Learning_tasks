import pytest
from vowels_and_consonants import letters_list
from long_text_generator import LONG_TEXT


@pytest.fixture
def control_empty_vowels():
    empty_vowels = set()
    return empty_vowels


@pytest.fixture
def control_empty_consonants():
    empty_consonants = set()
    return empty_consonants


@pytest.fixture
def control_full_vowels():
    full_vowels = {'о', 'и', 'е', 'а', 'у', 'ы', 'я', 'э', 'ю', 'ё'}
    return full_vowels


@pytest.fixture
def control_full_consonants():
    full_consonants = {"б", "п", "в", "ф", "д", "т", "з", "с", "ж", "ш", "ч",
                          "ц", "щ", "г", "к", "х", "м", "н", "л", "р", "й"}
    return full_consonants


def test_letters_list_capital_letter(control_full_vowels, control_full_consonants):
    control_vowels = control_full_vowels
    control_consonants = control_full_consonants
    test = letters_list("Съешь ещё этих мягких французских булок, да выпей же чаю 1234567890.")
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


def test_letter_list_empty(control_empty_vowels, control_empty_consonants):
    control_vowels = control_empty_vowels
    control_consonants = control_empty_consonants
    test = letters_list("")
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


@pytest.mark.parametrize("input_value", ["The quick brown fox jumps over the lazy dog.", "いろはにほへと"])
def test_letter_list_no_cyrillic(input_value, control_empty_vowels, control_empty_consonants):
    control_vowels = control_empty_vowels
    control_consonants = control_empty_consonants
    test = letters_list(input_value)
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


def test_letter_list_long_string(control_full_vowels, control_full_consonants):
    control_vowels = control_full_vowels
    control_consonants = control_full_consonants
    test = letters_list(LONG_TEXT)
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


@pytest.mark.parametrize("input_value", [True, 123, 345.9875, {'a', 'b'}, ['c', 'd']])
def test_letter_list_not_string(input_value, control_empty_vowels, control_empty_consonants):
    control_vowels = control_empty_vowels
    control_consonants = control_empty_consonants
    test = letters_list(input_value)
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants
