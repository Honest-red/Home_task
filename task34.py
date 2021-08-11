#ДЗ 34. Студенты и группы

from random import randint


class Student():
    def __init__(self, *name):
        self.name = name[0]
        self.sur = name[1]
        self.gr = list()

    def grades(self, *grad):
        if len(grad) == 0:
            self.gr = [randint(1, 12) for _ in range(10)]
        else:
            self.gr.append(int(grad[0].strip()))

    def grades_st(self):
        return self.gr

    def name_st(self):
        return self.name + ' ' + self.sur




file = open('src_14.txt', 'rt', encoding='utf-8')

while True:
    data = file.readline()
    if data != '':
        lst = data.split()
        for i in range(len(lst)):
            if i > 1:
                st.grades(lst[i])
            elif i == 0:
                st = Student(lst[0], lst[1])

        #print(st.name_st())
        #print(st.grades_st())
    else:
        break
file.close()


class Group():
    def __init__(self, group_name):
        self.group_name = group_name
        self.hillel_group = list()

    def add_hillel(self, *st):
        for student in st:
            self.hillel_group.append(student)


    def displayGroup(self):
        print('Группа студентов:', self.group_name)
        for i in self.hillel_group:
            print('fff')
            Student.name_st()


r = Group('Pomidor')
r.add_hillel()
r.displayGroup()
print(r.hillel_group)