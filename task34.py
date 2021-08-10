# ДЗ 34. Студенты и группы
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



class Group():
    def __init__(self):
        self.hillel_group = []

    def add_hillel(self):
        self.hillel_group.append(Student())

    def display_group(self):
        print('Группа студентов:')
        while True:
            Student.name_st()
            Student.grades_st()


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
        print(st.name_st())
        print(st.grades_st())
    else:
        break
file.close()

