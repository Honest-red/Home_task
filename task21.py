#ДЗ 21. Задача на словари 2

st = 'file Program Files Python file python Python lessons Git Home task task python file Task python mast be done.' \
     ' fle task 21 is correct and lessons Python dict is done. Python is good file '
d = {}
lst = st.split()
maks = 0

for i in range(len(lst)):
    if st.find(lst[i]) != -1:
        d[lst[i]] = st.count(lst[i])
print(d)
print()
for keys, value in d.items():
    if d.get(keys) > maks:
        maks = value
        word = keys
if st.rfind(keys) != 0:
    print('Чаще всего встречается слово', word, ', в тексе встречается', maks, 'раза')

#Дан текст состоящий из нескольких строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите последнее.
#Задачу необходимо решить с использованием словаря.

