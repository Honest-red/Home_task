# Вариант с перебором ЛСТ списка по каждому числу но не полной Аккуратностью

from random import randint

m = 5
lst2 = []

lst = [[randint(1, 50) for i in range(m)] for j in range(m)]

# lst = [randint(1, 50) for i in range(m)]
print(lst)

print()
#
def v_print(lsk):
    for i in range(m):


        for j in lst[i]:
            #print(j)

            sum_num = sum([int(m) for m in lst[i]])

            if j < 0b1010:
                j = str('  ' + str(j))
            else:
                j = str(' ' + str(j))
        #print("{: >10} {: >10} {: >10} {: >10}".format(*lst[i]))
            print(j)

            #print(m * ("{: >10}").format(j))

        #print(' ', end='\t')
        #print(lst[i])
        #if len(lst[i]) > m:
        #    print(j, end='\t')
        #        print(j, end='\t')


            #print(lst[i])

        #lst2.append(sum_num)
        #break

    return sum_num

print(v_print(lst))

#print(lst2)