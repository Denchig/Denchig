a = float(input('Write first number: '))
b = float(input('Write second number: '))
c = float(input('Write third number: '))
sum_numbers = a + b + c
product_number = a * b * c

print(f'Sum = {sum_numbers} \nProduct = {product_number}')

--------------------------------------------------------------------------------------------------------

a = float(input('Write first number: '))
b = float(input('Write second number: '))

def bigger(first, second):
    if first > second:
        print(f'{first} is bigger')
    elif first < second:
        print(f'{second} is bigger')
    else:
        print('The numbers are equal')

bigger(a, b)

----------------------------------------------------------------------------------------------------------

text = input('Write your text here: ')
text = text[len(text)//2:]
print(text[::-1])

----------------------------------------------------------------------------------------------------------

text = input('Write your text here: ')
text = text[:len(text)//2]
print(text[::-1])

-----------------------------------------------------------------------------------------------------------

text = input('Write your text here: ')
print(text[2::3])

-----------------------------------------------------------------------------------------------------------

text = input('Write your text here: ')
print(10 * text[:5])

------------------------------------------------------------------------------------------------------------

text_1 = input('Write first line: ')
text_2 = input('Write second line: ')
print(text_1[len(text_1)//2:] + text_2[len(text_2)//2:] + text_2[:len(text_2)//2] + text_1[:len(text_1)//2])