class data:

    def __init__(self) -> None:
        pass


    def imp_num(self) -> str:        

        with open(r'Seminar_8\school_classes\list_of_classes.txt', 'r', encoding='UTF-8') as file:
            open_names = file.read().split(',') # Возможно, стоит это вынести в отдельную функцию 

        while True:
            num = input('Какой класс?').lower()
            if num in open_names:
                return num
            else:
                print('ERROR')


    def inp_subject(self, my_dict: dict) -> dict:
        while True:

            subject = input('Какой предмет?: ').lower()
            
            if len(subject) == 1:
                for key in my_dict:
                    if key[0] == subject:
                        subject = key
                        print(f'{subject}: ')
                        return subject
                else:
                    print('ERROR')

            elif len(subject) > 1:
                for key in my_dict:
                    if subject in key:
                        subject = key
                        print(f'{subject}: ')
                        return subject
                else:
                    print('ERROR')


    def imp_surname(self, clacc_dict: dict) -> str:
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


    def inp_rating(self) -> str:
        while True:
            score = input('Какая оценка?: ')

            if len(score) == 1 and score.isdigit() and 0 < int(score) < 6:
                return score
            elif len(score) == 2 and score[0].isdigit() and 0 < int(score[0]) < 6:
                if score[1] == '-' or score[1] == '+':
                    return score
                else:
                    print('ERROR')
            else:
                print('ERROR')


    def print_class(self, my_di: dict):
        for k, v in my_di.items():
            print(f'{k}: {v}')


            
d = data()