# # * args - список именованных аргументов,  кортеж получим
# # ** kwargs -  список не именованых, словарь получим
# #
# # def __init__(self, v1=None, v2=None, v3=None, v4=None):
# #     if v1 is None: (проверка)
# #      #self.v = list - vtoroi variant
# #         self.v1 = Point()
# #         #self.v.append(Point()) - vtori variant
# #     else:
# #         self.v1 = v1
# #     self.v2 = v2
# #     self.v3 = v3
# #     self.v4 = v4
# #
# 
# #
# # getter позволяет преобразовать внутреннюю информаци в понятную для пользователя.
# # Геттер - наоборт проверить изменение параметров изменение объекта.
# #
# 
# 
# class Mine:
#     def __init__(self, x=0, y=0):
#         self.__x = abs(x)
#         self.__y = abs(y)
# 
#     def __set_x(self, x):
#         self.__x = abs(x)
# 
#     def __get_x(self):
#         return self.__x
# 
# 
#     @property #- обертка в проперти
#     def y(self):
#         return self.__y
#     @y.setter
#     def y(self, y):
#         self.__y = abs(y)
# 
# 
# 
#     def __del_x(self):
#         self.__x = 0
# 
# 
#     x = property(__get_x, __set_x, __del_x, 'коментарий для пользователя') #принммае 4 параметра, ссылка на фукнцию геттре ссфлка на функцию сеттер, третий на делитер(в тех случаях когда надо удалить), 4 на коментраи
# 
#     # def print_mine(self):
#     #     return f'x={self.__x}, y={self.__y}'
# 
#     def __str__(self):
#         return f'x={self.__x}, y={self.__y}'
# 
#     def __add__(self, other): # - перепределяем как складывать 2 объекта
#         m = Mine(self.__x + other.x, self.__y + other.y)
#         return m
# 
# m1 = Mine(1, 3)
# m2 = Mine(6, 2)
# # m1.set_x(6)
# # m1.set_y(8)
# #del m1.x  #- удаление объекта
# 
# #rint(m1.x)
# #Проперти специальный класса, который позволяет получить интерфес изменения но под контролем
# #print(m1)
# #
# # str  -  строку являющаеся внутреннее сотояние объекта понятное человеку
# # repor - вернуть строку по кторой мы сможем ввосздать объект заново (который позвоил пересоздать объект)
# 
# 
# #Декторатор - обертка для других фнкций,можно создаить самому или использовать существующие.
# 
# 
# m3 = m1 + m2
# print(m3)
# 

# 
# стек область памяти в котороый выполняется программа, область не имеет произвольый доступ, нет возможности обратиться.
# обносвязанный списко позволяет двигаться в одном направлении, получив один элемент мы можем перейти к следующем.
# храниться значение и ссылка на следующий объект. послединй хранить значение ноне
# 
# двусвзанный списко позволяет двигаться в оба направления, хранит даннеы перед и после елемента.


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        
    def __str__(self):
        return self.__value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node
        

        
