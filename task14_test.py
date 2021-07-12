from random import randint


m = 5
lst2 = []


lst = [[randint(1, 50) for i in range(m)]  for j in range(m)]

#lst = [randint(1, 50) for i in range(m)]
print(lst)


print()

def v_print(lst):
    for i in range(m):
        for j in range(m):

            if lst[i][j] < 0b1010:
                lst2.append(' ' + str(lst[i][j]))
            else:
                lst2.append(lst[i][j])


            print(lst2[i], end=' ')
        print(lst2[j])

       # print(' ', end='\n')
            #lst2.append(lst[i][j])
            #print(lst2)
        #print(lst2[i], end='\n')
        #print('III', i)
        #print('jjjj', j)

        #print(lst2[j], end='\n')
print(v_print(lst))

print(lst2)