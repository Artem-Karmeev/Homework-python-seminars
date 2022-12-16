# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти '))

if number > 0 and number < 5:
    if (number == 1):
        print('x > 0; y > 0')
    if (number == 2):
        print('x < 0; y > 0')
    if (number) == 3:
        print('x < 0; y < 0')
    if (number == 4):
        print('x > 0; y < 0')
else:
    print('Введите число от 1 до 4 ')