

class Student():

    def __init__(self, name, surname, grades=[]):
        self.name = name
        self.surname = surname
        self.grades = grades

    def Grades(self, x):
        self.grades = x

    def Grades_st(self):
        return self.grades

    def names_st(self):
        name_st2 = [Student(), Student()]
        name_st = [0, 2, 'gggg' ]
        #print(self.name_st)

        return name_st

        #return self.name

st1 = Student('Bob', 'Phhnich')

print(st1.name)
print(st1.surname)
print(st1.names_st()[2])
print(st1.names_st2()[0].name)

#print(st1.St)

# class Group():
#     def __init__(self, group_st=[]):
#         self.group_st = group_st
#         pass# констуктор который создает группу по умолчанию как пустой список
#
#     def insert(self): #Метод который позволяет добавить студентов(НЕ атрибуты) в группу. и студент должен добавиться в список студентов группы
#         pass
#         #self.group_st =
#
#         def display_Group(self):
#             #for i in range(len(5)):
#                 # перебираю циклом спсок студентов в котором будут показываться имя и список оценок
#                 print()
#                 Student.name_st()
#                 Student.Grades_st()
#метод дисплей гроуп который отображает группу студентов на экран (при этом у стедента класа студент, который отображают имя и список оценок)
#(циклом перебираем список студентов и вызываем методы из студента, методы который выводят на экран.)