from data_function import record_file

data = ''


def console_input():
    global data
    data = ''
    my_data = input('\nВведи данные: ').replace(' ', '')
    security(my_data)


def security(my_data):
    global data
    if my_data[0].isdigit():
        if not len(my_data) % 2 :
            for i in range(0, len(my_data)-1, 2):
                if not my_data[i].isdigit() or my_data[i+1].isdigit():
                    print('\nНеверный ввод!\n\nПример ввода:"ABBCCC или 1A2B3C"\n')
                    console_input()
                    break
            else: 
                data = my_data
                record_file(data)
        else:
            print('\nНеверный ввод!\n\nПример ввода:"ABBCCC или 1A2B3C"\n')
            console_input()
    else:
        for i in range(len(my_data)):
            if my_data[i].isdigit():
                print('\nНеверный ввод!\n\nПример ввода:"1A2B3C или ABBCCC"\n')
                console_input()
                break
        else: 
            data = my_data
            record_file(data)

