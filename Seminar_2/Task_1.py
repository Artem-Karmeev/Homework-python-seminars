# Напишите программу, 
# которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число: ')

# for item in num:
#     if item.isdigit():
#         res += int(item)
# print(res)

res = [int(i) for i in num if i.isdigit()]
print(sum(res))




