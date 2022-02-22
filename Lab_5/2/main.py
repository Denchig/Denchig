import copy

words = ['кулон', 'серпантин', 'кукла', 'планета']
words_copy = copy.deepcopy(words)

print(words_copy[::-1])
