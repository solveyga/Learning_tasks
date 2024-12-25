'''
Написать и протестировать функцию, которая:
- принимает на вход строку
- возвращает списки кириллических гласных и согласных
'''

def letters_list(input_string):
    uniq_letters = set(input_string.lower())
    vowels = {'а', 'о', 'е', 'ё', 'и', 'у'}
    consonants = {'б', 'п', 'в', 'ф', 'д', 'т', 'з', 'с', 'ж', 'ш', 'ч', 'ц', 'щ', 'г', 'к', 'х', 'м', 'н', 'л', 'р'}
    output_vowels = []
    output_consonants = []
    for i in uniq_letters:
        if i in vowels:
            output_vowels.append(i)
        elif i in consonants:
            output_consonants.append(i)
    return output_vowels, output_consonants


print(letters_list('Тестовая строка со знаком препинания.'))
