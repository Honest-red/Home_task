#ДЗ 22. Инвертирование словаря.

d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
d2 = {}
d3 = {}
i = 0
for key, value in d.items():
    d2 = dict.fromkeys(value)
    d3.update(d2)
    lst = key

    lst = d.get(key)
    lst1 = tuple(lst)
    print(lst[2])

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