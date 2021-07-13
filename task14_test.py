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

            sum_num = sum([int(m) for m in lst[i]])

            if j < 0b1010:
                j = str('  ' + str(j))
            else:
                j = str(' ' + str(j))
            print(j)
            #print(lst[i])

        lst2.append(sum_num)
        break

    return sum_num

print(v_print(lst))

#print(lst2)