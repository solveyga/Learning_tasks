"""
Написать и протестировать функцию, которая:
- принимает на вход строку
- возвращает списки кириллических гласных и согласных
"""


def letters_list(input_value):
    input_string = str(input_value)
    if len(input_string) <= 256:
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

            return f"{vowels_result}\n{consonants}"
    else:
        return "Допустимы строки не длиннее 256 символов."


#print(letters_list("Съешь ещё этих мягких французских булок, да выпей же чаю."))

assert (
    f"Список гласных: а, е, и, о, у, ы, э, ю, я, ё.\nСписок согласных: б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ."
    == letters_list("Съешь ещё этих мягких французских булок, да выпей же чаю.")
)

assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_list("")

assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_list(
    "The quick brown fox jumps over the lazy dog いろはにほへと 1234567890"
)

assert f"Список гласных: а, о, у.\nНет кириллических согласных." == letters_list(
    "А о у"
)

assert f"Нет кириллических гласных.\nСписок согласных: г, д, ж." == letters_list("Гд ж")

assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_list(True)

assert f"Нет кириллических гласных.\nНет кириллических согласных." == letters_list(123)

assert f'Допустимы строки не длиннее 256 символов.' == letters_list("jvraGUOLARUHJvHZcuMcOzeqWsYugmwwjZGSvRJPVxOciGfmbfbPPyEfyiAGSYTdgppNkdrjGzyxcObtFAbYnCzkuQoPJtdfWaCbWJbuejqvFgnMqeQhenUAZcLJIRKJNjvPeKASymaavUYGTjeJHJGNLpyYvnLJTibYVKEZaFjaWXQIRuAMVBsxeqwrAScgztBbyiSxYqevGLFRXpVqCuKCIPkEMsCCJNFpsMXcKUOdwglUExxTsuhMsmTfFgvGOxIe")
