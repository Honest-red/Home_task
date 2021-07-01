#ДЗ 14. Треугольник 2

rows = int(input('Input a high: '))
cols = (rows*2)-1

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (
            i == rows-1
            or j == rows-i-1
            or j == rows+i-1
            or (j >  (rows-i-1) and j < (rows+i))
        ):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()