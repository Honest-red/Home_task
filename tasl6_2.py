#ДЗ 6. Високосный год.

a = int(input('введите год: '))

if (a%400)==0:
    print('год', a,'высокосный')
elif (a%100!=0) and (a%4==0):
    print('год', a,'высокосный')
else:
    print('год', a,'Не высокосный')