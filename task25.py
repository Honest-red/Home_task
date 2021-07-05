#ДЗ 25. Написать функцию season

year = int(input('Input month number: '))


def season(a):
    if 3 <= a <= 5:                     month = 'Spring'
    elif 6 <= a <= 8:                   month = 'Summer'
    elif 9 <= a <= 11:                  month = 'Аutumn'
    elif a == 12 or a == 1 or a == 2:   month = 'Winter'
    else:                               month = 'month number is not correct'
    return month


print(season(year))
