#ДЗ 22. Инвертирование словаря.

from pprint import pprint
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

d2 = {}
i = 0

for key, value in d.items():
    for i in range(len(value)):
        d_zn = d2.get(value[i])
        if d_zn != key and d2.get(value[i], '1') != '1':

            lst = d_zn
            lst.append(key)
            d2[value[i]] = lst
        else:
            lst = [key]
            d2.update({value[i]: lst})
pprint(d2)
