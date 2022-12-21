# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


while True:
    try:
        my_int = int(input('Введите число: '))
        if my_int > 0:
            break
        else:
            print('Введите положительное число')
    except:
        print('Введи число!')

temp_list = []
res_str = ''

while True:
    temp_list.append(str(my_int % 2))
    my_int = (my_int - (my_int % 2)) // 2
    if my_int == 0:
        break

temp_list.reverse()

for i in range(len(temp_list)):
    res_str += temp_list[i]

print(res_str)