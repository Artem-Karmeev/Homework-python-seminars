# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

x1 = float(input('Введите Х1 '))
y1 = float(input('Введите Y1 '))
x2 = float(input('Введите Х2 '))
y2 = float(input('Введите Y2 '))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('{:.1f}'.format(distance), sep = '')