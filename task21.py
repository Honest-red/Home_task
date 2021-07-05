#ДЗ 21. Задача на словари 2

st = 'file Program Files Python file python Python lessons Git Home task task python file Task python mast be done.' \
     ' fle task 21 is correct and lessons Python dict is done. Python is good file '
d = {}
lst = st.split()
maks = 0

for i in range(len(lst)):
    d[lst[i]] = st.count(lst[i])
print(d)
print()
for keys, value in d.items():
    if d.get(keys) > maks and (st.rfind(keys) != 0):
        maks = value
        word = keys
print('Чаще всего встречается слово', word, ', в тексе встречается', maks, 'раза')
