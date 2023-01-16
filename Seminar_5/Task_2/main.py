from random import randint as RI
from input_fun import my_input
from input_fun import input_name
from bot import my_bot
sum_candy = 121
name_1 = input_name()
name_2 = 'bot'
fate = 1 #RI(0,1)


if fate == 1:
    while True:
        step = RI(1,28) #my_input(name_1)
        sum_candy -= step
        if sum_candy <= 0:
            print(f"Победил {name_1}!")
            break
        step = my_bot(sum_candy)
        sum_candy -= step
        print(f' step = {step}, sum = {sum_candy}')
        if sum_candy <= 0:
            print(f"Победил {name_2}!")
            break

        