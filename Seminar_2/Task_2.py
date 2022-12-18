# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введи N: '))

res = []
my_sum = 0

for i in range(1, n+1):
    res.append(round((1 + 1/i)**i, 2))

res[0] = int(res[0])

for i in range(n):
    my_sum += res[i]

print(f'Для n={n} -> {res} \nСумма {my_sum}')