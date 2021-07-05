# ДЗ 23. Написать функцию square.

def square(a):
    p = 4 * a
    s = a ** 2
    d = ((a**2) * 2) ** 0.5
    return p, s, d


side = int(input('Input side of square: '))
print(square(side))