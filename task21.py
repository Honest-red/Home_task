#ДЗ 21. Задача на словари 2

st = 'file Program Files Python file python Python lessons Git Home task task python file. Task python mast be done.' \
     ' file task 21 is correct and lessons Python dict is done. Python is good'
d2 = {}
lst = st.split()

for i in range(len(lst)):
    d = {i: lst[i]}
    if st.find(d[i]) != -1:
        if st.count(d[i]) > 0:
            d2[d[i]] = st.count(d[i])

print(d2.keys())
    #print(d2[3])
    #if d2[lst[i]] < d2[lst[(i+1)]]:
     #   m1 = d2[lst[i]]
      #  print('MAX', m1)


print(d2)
#Дан текст состоящий из нескольких строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите последнее.
#Задачу необходимо решить с использованием словаря.