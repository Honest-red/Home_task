#ДЗ 26. Написать функцию arithmetic

number = int(input('Input fіrst number: '))
number2 = int(input('Input second number: '))
oper = input('Input operation character : ')


def arithmetic(a, b, zn):
    if zn == '+':   result = a + b
    elif zn == '-': result = a - b
    elif zn == '*': result = a * b
    elif zn == '/': result = a / b
    else:           result = 'Неизвестная операция'
    return result


print(arithmetic(number, number2, oper))
