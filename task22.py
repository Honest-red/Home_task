#ДЗ 22. Инвертирование словаря.
d2 ={}
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
#print(type(d.items()))



tup = tuple(d.items())
#print(tup, type(tup))
lst = [tup for _ in tup]
print(lst)
print(lst[0])


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