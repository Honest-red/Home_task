#ДЗ 16. Ромб 1

#rows = int(input('Input a high: '))
rows = 9
cols = rows
for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (
            j == (rows//4)-i
            #j == (rows//2)+i
            or i == (cols//2)+j
            #or i == (cols//2)+(cols-1-j)
            #or (j > (rows//2)-i and j < (rows//2)+i and i <= (rows-1)//2)
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()