"""
Написать и протестировать функцию, которая:
- принимает на вход строку
- возвращает списки кириллических гласных и согласных
"""

def letters_list(input_string):
    uniq_letters = set(input_string.lower())
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
        "й"
    }
    output_vowels = set()
    output_consonants = set()
    for i in uniq_letters:
        if i in vowels:
            output_vowels.add(i)
        elif i in consonants:
            output_consonants.add(i)
    return output_vowels, output_consonants


output = letters_list("")

print(output[0]==set())