from function import random_num

num = int(input('Try to guess the number: '))
if num == random_num():
    print("Victory")
else:
    print("Repeat again")
