from random import randint


def bubble(array):
    for i in range(len(array) - 1):
        flag = 1
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = 0

        if flag:
            break



lst = [randint(10, 50) for _ in range(20)]
print(lst)
bubble(lst)
print(lst)