# ДЗ 11. Поиск символа в строке. Не используя If

st = input('Введите строку:')
sim = input('Введите искомый символ:')

a = 0
b = st.find(sim, a)
while b != -1:
    a = b + 1
    print(b, end = ' ')
    b = st.find(sim, a)