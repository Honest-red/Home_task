#ДЗ 22. Инвертирование словаря.

from pprint import pprint
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

d2 = {}
i = 0
j = 0

for key, value in d.items():
    for i in range(len(value)):
        If d2[value[i]] != 'None'
        If d2.get(value) != 'None'
            Print est polychilos
        Else:
        #str.append(value[i])

            d2.update({value[i]: key})
pprint(d2)





# if d2.get(value[i]) != 'None':
#     d2[value[i]] = 111
#     for i in range(len(value)):
#         d2.update({value[i]: key})
#
#         print(d2)






        #print()
        #print(d3[value[i]])
        #if key in d3[value[i]]:
            #print(key)

            #print()
        # a = str(d3[value[i]]) + key

    #print('333', d3)

    #{'malum': 'punishment',
    # 'pomum': 'apple',
    # 'popula': 'apple',
    # 'baca': 'fruit',
    # 'bacca': 'fruit',
    # 'popum': 'fruit',
    # 'multa': 'punishment'}





            # {'malum':  'punishment',
            #  'pomum':  'apple',
            #  'popula': 'apple',
            #  'baca':   'fruit',
            #  'bacca':  'fruit',
            #  'popum':  'fruit',
            #  'multa':  'punishment'}

            #print(value)
            #print(key)
            #print(a, type(a))
            #print(key, type(key))
            #print()
        #d4 = {value[i]:key}
           #print(d4)


            #[value] = key
        #print()
        #if lst[i] in d3.keys():
            #print('УРА')
        #else:
            #print('NET')

    #print(lst1.append(lst))
    #print(lst1)
    #words = lst.split(:)
    #if words in d2:
        #d2[words] = 'key'
        #print('d2', type('malum'))
    #else:
        #print('Not')
    #print(lst[2])
    #print('LST', lst, type(lst))

    #print('lst1', lst1, type(lst1))
    #print('d3', d3, type(d3))
    #print()
    #if lst1[i] != -1:
        #print(lst1)
        #i += 1
        #d3[lst1] = key
    #print(tuple(lst))
        #print(key)
    #print(value)
        #if d3[lst1] == value:
            #d3[lst1] = key

#print(d3)
        #t = value[i]
            #rint(value, type(t))
            # += 1
            #print(type(key))
       # d3[value] = 'key'
#print(d3)
    # for i in range(len(d3)):
    #     d3[value] = lst[i]
    #     print(d3, len(d3))
    # #key2 = value


    #d2 = d.get(key)

    #print(d2, type(d2))

    # for keys, value in d.items():
    #     if d.get(keys) > maks and (len(d) != 0):
    #         maks = value
    #         word = keys
    # print('Чаще всего встречается слово', word, ', в тексе встречается', maks, 'раза')


# tup = tuple(d.items())
# print(tup, type(tup))
# lst = [tup for _ in tup]
#(lst)
#print(lst[0])

#print(d.keys())
##for i in d.keys():
  #  a = d.keys(i)
   # print(a)
#print(d['fruit'])
#print(d['punishment'])



# Дан словарь ключами которого являются английские слова, а значения - списки латинских слов.
# Необходимо развернуть словарь. Другими словами, необходимо, на основании заданого словаря, создать новый словарь,
# у которого в качестве ключей будут взяты латинские слова, из первого словаря,
# а значениями будут, соответствующие им, английские слова.

# Исходный словарь:

# d = {
#   'apple': ['malum', 'pomum', 'popula'],
#   'fruit': ['baca', 'bacca', 'popum'],
#   'punishment': ['malum', 'multa']
#}
