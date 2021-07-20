from random import randint
m = 5
lst2 = []
lst = [[randint(1, 50) for i in range(m)] for j in range(m)]

print(lst)
print()
def v_print(lsk):

    #for i in range(m):
        #i = 0
        #j= 0
        #lst2.append(j)
        for j in lsk:

            #sum_num = sum([int(m) for m in lst[i]])
            #print(j)
            print(j)
            #print()
       # break
        #print(end='\t')
        return j
#print(list(map(v_print,lst)))
print(v_print(lst))

#print(lst2)