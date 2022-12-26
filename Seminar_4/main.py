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

from input_function import inp_n
from rand_function import rand_polynomial
from convert_function import convert_polynomial
from convert_function import convert_str_in_dict
from addition_function import sum_dict

max_degree_1 = inp_n()
max_degree_2 = inp_n()

print(max_degree_1)
print(max_degree_2)
print(' ')

polynomial_1 = rand_polynomial(max_degree_1)
polynomial_2 = rand_polynomial(max_degree_2)

print(polynomial_1)
print(polynomial_2)
print(' ')


stp_polynomial_1 = convert_polynomial(polynomial_1)
stp_polynomial_2 = convert_polynomial(polynomial_2)

print(stp_polynomial_1)
print(stp_polynomial_2)
print(' ')

tmp_dict_1 = convert_str_in_dict(stp_polynomial_1)
tmp_dict_2 = convert_str_in_dict(stp_polynomial_2)

print(tmp_dict_1)
print(tmp_dict_2)
print(' ')

res_dict = sum_dict(tmp_dict_1, tmp_dict_2)

print(res_dict)
print(' ')

print(convert_polynomial(res_dict))