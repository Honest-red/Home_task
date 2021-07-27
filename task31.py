# ДЗ 31. Реверс списка

def sort(lst1, first_idx, last_idx):
    if first_idx >= len(lst1) // 2:
        return
    lst1[first_idx], lst1[last_idx] = lst1[last_idx], lst1[first_idx]
    sort(lst1, first_idx + 1, last_idx - 1)


st = 'file Program Files Python file python Python lessons Git Home task task python file Task python mast'
lst = st.split()

print(lst)
sort(lst, 0, len(lst)-1)
print(lst)
