from str import text_menu


def input_num_menu() -> int:
    print(text_menu)
    while True:
        try:
            x = int(input('Выбери пункт меню: '))
            if 0 < x < 9:
                return x
            else:
                print('Введи число от 1 до 8\n')
        except:
            print('Только число!\n')


def input_contact() -> list:
    name = input('Введите имя: ')
    num = input('Введите номер телефона: ')
    com = input('Введите коментарий: ')
    contact_list = [f'{name}',f'{num}',f'{com}']
    return contact_list


def inpyt_search() -> str:
    meaning = input('Ведите искомые значения: ')
    return meaning


def del_item(meaning: list) -> int:
    while True:
        try:
            x = int(input('Введите "ID" контакта: '))
            for i in range(0, len(meaning), 2):
                if x == int(meaning[i]):
                    return x
            else:
                print('Укажите доступный ID: \n')
        except:
            print('Только число!\n')

def making_changes() -> bool:
    while True:
        user_res = input('У вас есть не сохраненный результат, сохранить? (Y/n)').lower().strip()
        if user_res == 'y' or user_res == 'n':
            if user_res == 'y':
                user_res = True
                return user_res
            else:
                user_res = False
                return user_res
        else:
            print('Введите только "Y" или "N"!')



class PrintOut:

    def __init__(self) -> None:
        pass
    
    def show_contacts(self, contack_list: list): 
        for i in range(len(contack_list)):
            print(*contack_list[i])

    def show_i_contacts(self, contack_list: list): 
        for i in range(1, len(contack_list), 2):
            print(f'ID : {contack_list[i-1]}', end='; ')
            print(*contack_list[i])
            print()

    def open_print(self):
        print('Файл успешно открыт!\n')

    def save_print(self):
        print('Файл успешно сохранен!\n')




po = PrintOut()

    







