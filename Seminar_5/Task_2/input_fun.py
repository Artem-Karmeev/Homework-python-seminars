def my_input(name) -> int:
    while True:
        try:
            a = int(input(f"Ходит {name}: "))
            if 0 < a < 29:
                return a
            else:
                print('Введи число от 1 до 28')
        except:
            print('Необходимо ввести число!')


def input_name() -> str:
    name_1 = input('Введите имя: ')
    return name_1


def bot_or_human() -> bool:
    res = True
    while True:
        res_str = input('Играть против бота? (Y/N): ').lower().replace(' ', '')
        if res_str == 'y' or res_str == 'n':
            if res_str == 'y':
                return res
            else:
                res = False
                return res
        else:
            print('Введите только Y или N ')