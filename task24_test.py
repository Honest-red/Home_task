
file = open('src_14.txt', 'rt', encoding='utf-8')

class Point:

    def __init__(self, *tt, *rr):
        self.name = tt
        self.lastname == rr


while True:
    data = file.readline()
    if data != '':
        lst = data.split()

        for i in range(len(lst)):
            if i > 1:
                pass
                #print(lst[i], end=' ')
            elif i == 0:
                k = Point(lst[0], lst[1])
                #ee = Point.name = lst[0]
                #ww = Point.lastname = lst[1]
                #print('Имя', Point.name)
                #print('ФАмилия', Point.lastname)
                #k = ee +' '+ ww
                print(k)

                #tt = lst[i]
                #pt_i = Point(tt)
        #print()
    else:
        break
file.close()

v = Point()
print(v)

class Rect:

    v = [Point(), Point(), Point(), Point()]


r = Rect()



print(r.v[3].name)
