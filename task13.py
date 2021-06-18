#ДЗ 13. Замена символов в строке

st = input('Введите строку:')
sth = st.replace('h', 'H')
af = sth.find('H')
arf = sth.rfind('H')
print(sth[: af:]+sth[af+1: arf:]+sth[arf+1: :])