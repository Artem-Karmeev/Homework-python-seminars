from random import randint as RI
from input_fun import my_input, input_name, bot_or_human
from bot import my_bot

sum_candy = 159
name_1, name_2 = '', ''

fate = RI(0,1)
res = bot_or_human()

if res:
    if fate:
        name_1 = input_name()
        name_2 = 'Bot'
        while True:
            step = my_input(name_1)
            sum_candy -= step
            print(f'Cумма конфет = {sum_candy}')
            if sum_candy <= 0:
                print(f"Победил {name_1}!")
                break
            step = my_bot(sum_candy)
            sum_candy -= step
            print(f'Bot взял = {step} конфет, сумма конфет = {sum_candy}')
            if sum_candy <= 0:
                print(f"Победил {name_2}!")
                break
    else:
        name_1 = 'Bot'
        name_2 = input_name()
        while True:
            step = my_bot(sum_candy)
            sum_candy -= step
            print(f'Bot взял = {step} конфет, сумма конфет = {sum_candy}')
            if sum_candy <= 0:
                print(f"Победил {name_1}!")
                break
            step = my_input(name_2)
            sum_candy -= step
            print(f'Cумма конфет = {sum_candy}')
            if sum_candy <= 0:
                print(f"Победил {name_2}!")
                break
else:
    # За право первого хода игрокам придется драться в реальном мире.
    name_1 = input_name()
    name_2 = input_name()
    while True:
        step = my_input(name_1)
        sum_candy -= step
        print(f'Cумма конфет = {sum_candy}')
        if sum_candy <= 0:
            print(f"Победил {name_1}!")
            break
        step = my_input(name_2)
        sum_candy -= step
        print(f'Cумма конфет = {sum_candy}')
        if sum_candy <= 0:
            print(f"Победил {name_2}!")
            break

ex = input('Press enter to exit: ')# кастыль, чтоб консоль не закрывалась 


