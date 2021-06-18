# ДЗ 11. Поиск символа в строке. С If

st = input('Введите строку:')
sim = input('Введите искомый символ:')

a = 0
b = 0
while b != -1:
    b = st.find(sim, a)
    if b == -1:
       break
    a = b + 1
    print(b, end = ' ')
