# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, 
# в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random

def inp_n():
    while True:
        try:
            n = int(input('Введи максимальную степень: '))
            if n > 0:
                return n
        except:
            print('Нужно ввести целое, положительное число. ')

def rand_polynomial(n):
    my_dict = {}
    for i in range(n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(-100, 100)
                if koef != 0:
                    break
            my_dict[i] = koef
        else:
            my_dict[i] = random.randint(-100, 100)
    return my_dict

def convert_polynomial(my_dict):
    new_str = ''

    for key, value in my_dict.items():

        if key > 1 and key != 0:
            new_str += str(value) + '*x' + '**' + str(key) + ' '
        elif key == 1:
            new_str += str(value) + '*x' + ' '
        elif key == 0:
            new_str += '+ ' + str(value) + ' =0'
    return new_str

n = inp_n()
polynomial_1 =  rand_polynomial(n)
polynomial_2 =  rand_polynomial(n)


print(polynomial_1)
print(polynomial_2)
print(convert_polynomial(polynomial_1))
print(convert_polynomial(polynomial_2))


