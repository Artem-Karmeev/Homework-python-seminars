# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
# temp_list = []

# for i in range(len(my_list)):
#     my_list[i] = str(my_list[i]).split('.')
#     my_list[i][0] = '0'
#     if len(my_list[i]) == 2:
#         temp_list.append(float(my_list[i][0] + '.' + my_list[i][1]))

# print(max(temp_list) - min(temp_list))


temp_list = [str(item).split('.') for item in my_list if item > int(item)]
temp_list = [float(f'0.{temp_list[i][1]}') for i in range(len(temp_list))]
print(max(temp_list) - min(temp_list))

