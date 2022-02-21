def formula1(x):
    return x ** 4 + 4 ** x



def formula2(x, y):
    return y ** 4 + 4 ** x



def formula3(tf):
    return 5 / 9 * (tf - 32)



def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False



def diagonal(a, b):
    return (a ** 2 + b ** 2) ** 0.5



def triangle(a, h):
    return 1 / 2 * a * h



def circle(r):
    return 3.14 * r ** 2