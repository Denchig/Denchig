import random

words = ['кулон', 'серпантин', 'кукла', 'планета']

word = random.choice(words)
letter = random.choice(word)
word_shadow = word.replace(letter, "?")

x = input(f"Угадайте букву в слове: '{word_shadow}': ")

if x == letter:
    print("Правильно!")
else:
    print("Попробуйте в другой раз")
