from vowels_and_consonants import letters_list


def test_letters_list_general():
    control_vowels = {'о', 'и', 'е', 'а', 'у'}
    control_consonants = {'ч', 'м', 'д', 'с', 'щ', 'ш', 'в', 'г', 'б', 'т', 'л', 'к', 'х', 'п', 'ф', 'ц', 'з', 'н', 'р'}
    test = letters_list("Съешь еще этих мягких французских булок да выпей чаю 1234567890.")
    test_vowels = test[0]
    test_consonants = test[-1]
    assert control_vowels == test_vowels
    assert control_consonants == test_consonants

