# Инкопсуляция
#
# public - открытый интерфес - через которую мы можемобьшшаться с классом и его объектом
#
# private - закрытая часть реализация класса - не доступоно не через обьект не через класс
# пометить атрибут закрытым - добавить в начале __ (Пример: __min)
#
#
# protected - защищенная часть реализации - доступ только в классе потомке.
# пометить атрибут защищенным - добавить в начале _ (Пример: _min)
#
# Наследование
#

class WaterBird:

    def __init__(self, name):
        self.name = name
        print(f'Bird name is {self.name}')

    def where_is_live(self):
        print('On the Earth')

    def swim(self):
        print('Can swim very good')

    def voice(self):
        pass


class Penguin(WaterBird):

    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin is ready')

    def where_is_live(self):
        print('South pole')

    def run(self):
        print('Running')

    def voice(self):
        print('pi-pi-pi')

#
# class Duck(WaterBird):
#
#     def __init__(self, name):
#         super().__init__(name)
#         print('Duck is ready')
#
#     def where_is_live(self):
#         print('AnyWhere')
#
#     def Fly(self):
#         print('fly')
#
#     def voice(self):
#         print('Kra-kra-kra')
#
#
# Penguin = Penguin('Ping')
# Penguin.voice()
# Penguin.swim()
# Penguin.run()
# Penguin.where_is_live()
#
#
# Duck = Duck('Donald Dug')
# Duck.voice()
# Duck.swim()
# Duck.Fly()
# Penguin.where_is_live()


#Полиморфизм

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dislpay(self):
        print(f'Name: {self.name}\tAge: {self.age}')

class Empoloyee(Person):


    def __init__(self, name, age, company):
        super.__init__(name, age)
        self.company = company

    def dislpay(self):
        super().dislpay()
        print(f'Company: {self.company}')

class Student(Person):


    def __init__(self, name, age, university):
        super.__init__(name, age)
        self.university = university

    def dislpay(self):
        print(f'Studentname {self.name} From {self.university}')


people = [
    Person('Tom', 23),
    Empoloyee('Bob', 35, 'Google'),
    Student('Sam', 19, 'harvard')
]

for p in people:
    p.dislpay()
    print()
