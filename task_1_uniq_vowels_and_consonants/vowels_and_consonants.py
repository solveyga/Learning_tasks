"""
Написать и протестировать функцию, которая:
- принимает на вход строку
- возвращает списки кириллических гласных и согласных
"""


def letters_list(input_value):
    uniq_letters = set((str(input_value)).lower())
    vowels = {"а", "о", "е", "ё", "и", "у", "ы", "ю", "э", "я"}
    consonants = {
        "б",
        "п",
        "в",
        "ф",
        "д",
        "т",
        "з",
        "с",
        "ж",
        "ш",
        "ч",
        "ц",
        "щ",
        "г",
        "к",
        "х",
        "м",
        "н",
        "л",
        "р",
        "й",
    }
    output_vowels = []
    output_consonants = []
    for i in uniq_letters:
        if i in vowels:
            output_vowels.append(i)
        elif i in consonants:
            output_consonants.append(i)
    output_vowels.sort()
    output_consonants.sort()

    if output_vowels:
        vowels_result = f"Список гласных: {', '.join(list(output_vowels))}."
    elif not output_vowels:
        vowels_result = "Нет кириллических гласных."

    if output_consonants:
        consonants = f"Список согласных: {', '.join(list(output_consonants))}."
    elif not output_consonants:
        consonants = "Нет кириллических согласных."

    return f'{vowels_result}\n{consonants}'

print(letters_list("Съешь ещё этих мягких французских булок, да выпей же чаю 1234567890."))

