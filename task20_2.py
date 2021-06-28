#ДЗ 20. Задача на словари 1

st = 'file Program Files Python file python Python lessons Git Home task task python file'

d2 = {}
lst = st.split()

for i in range(len(lst)):
    d = {i: lst[i]}
    if st.find(d[i]) != -1:
        d2[d[i]] = st.count(d[i])
print(d2)