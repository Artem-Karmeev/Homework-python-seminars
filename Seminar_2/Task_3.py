# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random

original_list = [1,2,3,4,5,6,7,8,9]
temp_list = []
a = 8

print(f'До:    {original_list}')

while len(original_list) > 0:
    x = random.randint(0, a)
    temp_list.append(original_list[x])
    original_list.pop(x)
    a -= 1

original_list = temp_list

print(f'После: {original_list}')