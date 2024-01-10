mas = [12, 1, 2, 23, 45, 9999, 4, 5, 7]
# Ответ: 5, 10070

cnt = 1
max_cnt = 0
summ = 0
max_sum = 0

for i in range(len(mas) - 1):
    if mas[i] < mas[i+1]:
        cnt += 1
        summ += mas[i]
    else:
        summ += mas[i]
        if cnt > max_cnt:
            max_cnt = cnt
            max_sum = summ
        cnt = 1
        summ = 0

print(max_cnt, max_sum)
