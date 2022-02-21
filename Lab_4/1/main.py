s = " У лукоморья 123 дуб зеленый 456"

for char in s:
    if char == 'я':
        print(f"{s.index(char)} = index of char '{char}'")

counter = 0
for char in s:
    if char == 'у' or char == 'У':
        counter += 1
print(f"Letter 'y' appears: {counter} times")