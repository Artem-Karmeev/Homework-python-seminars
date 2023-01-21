# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти '))


# if quarter > 0 and quarter < 5:
#     if (quarter == 1):
#         print('x > 0; y > 0')
#     if (quarter == 2):
#         print('x < 0; y > 0')
#     if quarter == 3:
#         print('x < 0; y < 0')
#     if (quarter == 4):
#         print('x > 0; y < 0')
# else:
#     print('Введите число от 1 до 4 ')


a, b, c, d = 'x > 0; y > 0', 'x < 0; y > 0', 'x < 0; y < 0', 'x > 0; y < 0'
num_quar = lambda x: a if 1 in x else b if 2 in x else c if 2 in x else d
print(num_quar(quarter))