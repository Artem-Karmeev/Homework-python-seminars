# Напишите программу, 
# которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число: ')
res = 0

for char in num:
    if char.isdigit():
        res += int(char)
print(res)