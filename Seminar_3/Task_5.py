# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# a = 1-1*2
# print(a)

n = int(input('Введите n: '))

temp_list = [0,1]

for i in range(n-1):
    temp_list.append(temp_list[i] + temp_list[i+1])

fibonacci_list = temp_list.copy()

for i in range(2, len(fibonacci_list), 2):
    fibonacci_list[i] = fibonacci_list[i] - fibonacci_list[i] * 2

fibonacci_list.reverse()

for i in range(1, len(temp_list)):
    fibonacci_list.append(temp_list[i])

print(fibonacci_list)

