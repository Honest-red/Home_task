#ДЗ 13. Замена символов в строке

st = input('Введите строку:')

af = st.find('h')
arf = st.rfind('h')
b = st[af+1: arf:]
sth = b.replace('h', 'H')
print(st[: af+1:]+sth+st[arf: :])