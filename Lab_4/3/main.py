s = " У лукоморья 123 дуб зеленый 456"

s = s[:0] + "О" + s[1:]
print(s)

if s.isdigit() == False:
    print(s.lower())