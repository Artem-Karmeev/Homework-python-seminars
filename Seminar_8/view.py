class data:

    def __init__(self) -> None:
        pass


    def imp_num(self) -> str:        
        '''запрашиваем номер класса в формате: цифра -> буква'''
        open_names = ['a','b','c'] # хорошо было бы эту инфу из файла подтянуть

        while True:
            num = input('Какой класс?').lower()
            if len(num) == 2: # нужно сделать для 10 и 11 классов
                if num[0].isdigit():
                    if num[1] in open_names:
                        return num
                    else:
                        print('ERROR')
                else:
                    print('ERROR')
            else:
                print('ERROR')


    def inp_subject(sels, my_dict: dict) -> dict: # нужно сделать более 'юсер френдли'
        while True:
            subject = input('Какой предмет?').lower()
            if subject in my_dict:
                return subject
            else:
                print('ERROR')


    def imp_surname(sels, clacc_dict: dict) -> str:
        while True:
            temp_surname = input('Кто пойдет отвечать?: ').strip()
            surname = temp_surname[0].upper()
            for i in range(1, len(temp_surname)):
                surname += temp_surname[i].lower()
            if surname == 'Exit':
                return surname
            elif surname in clacc_dict:
                return surname
            else:
                print('ERROR')


    def inp_rating(sels) -> str:
        while True:
            score = input('Какая оценка?: ')
            if len(score) == 1 and 0 < int(score) < 6:
                return score
            elif len(score) == 2 and 0 < int(score[0]) < 6:
                if score[1] == '-' or score[1] == '+':
                    return score
                else:
                    print('ERROR')
            else:
                print('ERROR')


    def print_class(sels, my_di: dict):
        for k, v in my_di.items():
            print(f'{k}: {v}')


            
d = data()