# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
res_list = []
my_count = len(my_list) - 1


for i in range(len(my_list)//2):
    res_list.append(my_list[i] * my_list[my_count])
    my_count -= 1

if len(my_list) % 2 != 0:
    res_list.append(my_list[(len(my_list)//2)] * my_list[(len(my_list)//2)])

print(res_list)