# Быстрая сотрировка Метод Хора

from random import randint


def qsort(nums, first_idx, last_idx):
    if first_idx >= last_idx:
        return

    i, j = first_idx, last_idx
    middle_value = nums[(first_idx + last_idx) // 2]
    while i <= j:
        while nums[i] < middle_value:
            i += 1

        while nums[j] > middle_value:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    qsort(nums, first_idx, j)
    qsort(nums, i, last_idx)


lst = [randint(1, 99) for _ in range(25)]
print(lst)
qsort(lst, 0, len(lst)-1)
print(lst)