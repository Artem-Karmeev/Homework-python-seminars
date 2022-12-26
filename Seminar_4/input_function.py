
def inp_n():
    while True:
        try:
            n = int(input('Введи максимальную степень многочлена: '))
            if n > 0:
                return n
        except:
            print('Нужно ввести целое, положительное число. ')
