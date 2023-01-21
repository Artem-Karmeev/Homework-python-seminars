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


class PrintOut:

    def __init__(self) -> None:
        pass
    
    def show_contacts(self, contack_list: list): 
        for i in range(len(contack_list)):
            print(*contack_list[i])

    def open_print(self):
        print('Файл успешно открыт!\n')

    def save_print(self):
        print('Файл успешно сохранен!\n')

    

dp_po = PrintOut()

    







