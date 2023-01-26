from model import dp
from view import d

def journal():

    num_class = d.imp_num() # запросили номер класса
    dp.init_path(num_class) # присвоили адрес файла
    dp.open() # открыли файл, перевели его в json

    file = dp.get() # Вернули файл json

    temp_key = d.inp_subject(file) # присвоили имя предмета
    dp.init_subject(temp_key) # разбили на ключ и значение(словарь)


    while True:
        temp_dict = dp.get_subject() # вернули словарь с учениками и оценками
        d.print_class(temp_dict) # принтонули словарь с учениками и оценками
        surname = d.imp_surname(temp_dict) # запросили фамилию уч-ка
        if surname == 'Exit':
            dp.update_data()
            dp.save_data()
            break # будем сохранять в файл 
        score = d.inp_rating() # запросили оценку
        dp.update_score(surname, score) # поставили оценку





