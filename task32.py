# ДЗ 32. Список студентов

file = open('src_14.txt', 'rt', encoding='utf-8')
file_st = open('src.txt', 'wt', encoding='utf-8')
st_sum = 0
all_sum = 0

while True:
    data = file.readline()
    if data != '':
        st_sum += 1
        lst = data.split()
        a = 0
        for i in range(len(lst)):
            if i > 1:
                a += int(lst[i])
        aver_sum = round(a / (len(lst) - 2), 2)
        all_sum += aver_sum
        st = lst[1] + ' ' + lst[0][:1] + '.'
        line_txt = '{:<15}    {:>} '.format(st, aver_sum)
        file_st.write(line_txt)
        file_st.write('\n')
        if aver_sum < 5:
            print(line_txt)
    else:
        print('среднний балл по классу -', round((all_sum / st_sum), 2))
        break
file.close()
file_st.close()
