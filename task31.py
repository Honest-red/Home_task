# В работе!!1

from random import randint

def qsort(nums, first_idx, last_idx):
    if first_idx >= (first_idx + last_idx) // 2:
        return
    
    print(last_idx)
    #print((first_idx + last_idx) // 2)
    #print()
    k = 0

    i, j = first_idx, last_idx


    #middle_value = nums[(first_idx + last_idx) // 2]
    while i <= (first_idx + last_idx) // 2:
        #while nums[i] < middle_value:
            #i += 1
        #while nums[j] > middle_value:
            #j -= 1
        #if i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        k += 1
        print(k)
    qsort(nums, first_idx, j)
    qsort(nums, i, last_idx)

st = 'file Program Files Python file python Python lessons Git Home task task python file Task python mast' \
     ' fle task 21 is correct and lessons Python dict is done. Python is good file '
lst = st.split()

print(lst)
qsort(lst, 0, len(lst)-1)
print(lst)
print(len(lst))
