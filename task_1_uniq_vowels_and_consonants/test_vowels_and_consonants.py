from vowels_and_consonants import letters_list
from long_text_generator import LONG_TEXT


#  полные множества в качестве фикстуры

def test_letters_list_capital_letter():
    control_vowels = {'о', 'и', 'е', 'а', 'у', 'ы', 'я', 'э', 'ю', 'ё'}
    control_consonants = {"б", "п", "в", "ф", "д", "т", "з", "с", "ж", "ш", "ч",
                          "ц", "щ", "г", "к", "х", "м", "н", "л", "р", "й"}
    test = letters_list("Съешь ещё этих мягких французских булок, да выпей же чаю 1234567890.")
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


def test_letter_list_empty():
    control_vowels = set()
    control_consonants = set()
    test = letters_list("")
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants
    '''
# добавить параметризацию
def test_letter_list_no_cyrillyc():
    assert
    '''


def test_letter_list_long_string():
    control_vowels = {'о', 'и', 'е', 'а', 'у', 'ы', 'я', 'э', 'ю', 'ё'}
    control_consonants = {"б", "п", "в", "ф", "д", "т", "з", "с", "ж", "ш", "ч",
                          "ц", "щ", "г", "к", "х", "м", "н", "л", "р", "й"}
    test = letters_list(LONG_TEXT)
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants


'''
# добавить параметризацию
def test_letter_list_not_string():
    assert
'''
