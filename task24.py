#ДЗ 24. Написать функцию is_year_leap

year = int(input('введите год: '))


def is_year_leap(a):
    is_year = a % 400 == 0 or ((a % 100 != 0) and (a % 4 == 0))
    return is_year


print(is_year_leap(year))
