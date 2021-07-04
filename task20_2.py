#ДЗ 20. Задача на словари 1

st = 'file Program Files Python file python Python lessons Git Home task task python file'

lst = st.split()
for i in range(len(lst)):
    if st.find(lst[i]) != -1:
        print('Это слово', lst[i], 'Встречается в тексте' ,st.count(lst[i]), 'раз(а)')