#ДЗ 4. Перевернуть число

a = int(input('введите целов трехзначное число:'))

a1 = a%10
#print('первое числло ', a1)
a11 = (a%100)//10
#print('второе число ', a11)
a111 = (a%1000)//100
#print('третье число', a111)

b=(a1*100)+(a11*10)+(a111)
print('итоговое число ', b)

