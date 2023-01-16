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

def input_name(): #-> tuple:
    name_1 = input('Введите имя первого игрока: ')
    # name_2 = input('Введите имя второго игрока: ')
    return name_1#, name_2