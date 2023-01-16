from data_function import record_file

data = ''


def console_input(link):
    global data
    data = ''
    data = input('\nВведи данные: ').replace(' ', '')
    security(link)


def security(link):
    global data
    if data[0].isdigit():
        if not len(data) % 2 :
            for i in range(0, len(data)-1, 2):
                if not data[i].isdigit() or data[i+1].isdigit():
                    print('\nНеверный ввод!\n\nПример ввода:"ABBCCC или 1A2B3C"\n')
                    console_input()
                    break
            else: 
                record_file(data, link)
        else:
            print('\nНеверный ввод!\n\nПример ввода:"ABBCCC или 1A2B3C"\n')
            console_input()
    else:
        for i in range(len(data)):
            if data[i].isdigit():
                print('\nНеверный ввод!\n\nПример ввода:"1A2B3C или ABBCCC"\n')
                console_input()
                break
        else: 
            record_file(data, link)

