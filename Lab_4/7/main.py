s = " У лукоморья 123 дуб зеленый 456"

s = s[:-1] + "Р"
print(s)

counter = 0
for char in s:
    if char == 'о':
        counter += 1
print(f"Letter 'о' appears: {counter} times")