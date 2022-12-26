import random

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