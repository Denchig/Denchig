s = " У лукоморья 123 дуб зеленый 456"
letters = 0
numbers = 0

for char in s:
    if char.isdigit():
        numbers+=1
    elif char.isalpha():
        letters+=1

print(f'The string consists of {numbers} numbers and {letters} letters')
