# m2^31 -1 = 2147483647

from string import digits, punctuation, whitespace
from random import choices

letters = "абвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"
letters_and_digits = letters + digits + punctuation + whitespace

LONG_TEXT = "".join(choices(letters_and_digits, k=10000))

with open("long_text.txt", "w") as f:
    for i in LONG_TEXT:
        f.write(i)
