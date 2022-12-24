# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# namber = input("Введи значения через пробел: ").split()
# my_sum = 0

# for i in range(len(namber)):
#     namber[i] = int(namber[i])
#     if i % 2 != 0:
#         my_sum += namber[i]
# print(my_sum)

my_list = [2, 3, 5, 9, 3]
my_sum = 0

for i in range(1, len(my_list), 2):
    my_sum += my_list[i]

print(my_sum)