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


    def displayGroup(self):
        print('Группа студентов:')
        while True:
            print(Student().name_st())
            Student().Grades_st()


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

r = Group()
r.add_hillel()
print(r.displayGroup())
#print(st.name_st())
#st.grades(5, 4, 3, 2, 1)


#print(st.grades_st())



#реальизовать 2 класса класс студент и класс группа
#
# Класс студент должен содержать имя студента и список оценок - атрибуты экземпляра и они в констукторе.
# В конструкторе инициализируется список оценок (не в конструктор передавать а отдельным методом)
#
# Метод котроый добаввить студенту оценки.
#
# Метод отобразит список оценок
# Метод который вернет имя
#
# Класс группа
# 2 атрибута - атрибуты экземпляла - Название и список обьектов типа студент
# -----------------------------------------------------------------------------------------
# В группе должен быть конструктор который создает группу по умолчанию пустой список
#
# Метод который позволяет добавить студентов(НЕ атрибуты) в группу. и студент должен добавиться в список студентов группы
#
# метод дисплей гроуп который отображает группу студентов на экран (при этом у стедента класа студент, который отображают имя и список оценок)
# (циклом перебираем список студентов и вызываем методы из студента, методы который выводят на экран.)
#