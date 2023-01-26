class my_class:
    my_dict = {}
    path = ''

    subject_dict = {}
    key = ''


    def __init__(self) -> None:
        pass


    def init_path(self, num_class: str): 
        self.path = f'Seminar_8\school_classes\{num_class}.txt'
    

    def get(self) -> dict:
        return self.my_dict


    def open(self): # Cамое главное работает)
        temp_list = []
        with open(self.path, 'r', encoding='UTF-8') as file:
            my_list = file.readlines()

        for line in my_list:
            temp_list.append(line.replace(' ', '').replace(',', ', ').strip().split(':'))
                
        for i in range(len(temp_list)):
            temp_list[i][1] = temp_list[i][1].split(';')
                
        for i in range(len(temp_list)):
            for j in range(len(temp_list[i][1])):
                temp_list[i][1][j] = temp_list[i][1][j].split('=')
 
        for i in range(len(temp_list)):
            temp_dict = {}
            for j in range(len(temp_list[i][1])):
                temp_dict[temp_list[i][1][j][0]] = temp_list[i][1][j][1]
            self.my_dict[temp_list[i][0]] = temp_dict
        

    def init_subject(sels, key: str) -> dict:
        sels.key = key           
        sels.subject_dict = sels.my_dict[key]


    def get_subject(sels):
        return sels.subject_dict


    def update_score(sels, surname_key: str, score: str):
        sels.subject_dict[surname_key] += f', {score}'
        

    def update_data(sels):
        sels.my_dict[sels.key] = sels.subject_dict


    def save_data(sels):
        temp_str = ''

        for key in sels.my_dict:
            temp_str += f'{key}: '
            for k, v in sels.my_dict[key].items():
                temp_str += f'{k} = {v}; '
            temp_str = temp_str[: -2] + '\n' 

        with open(sels.path, 'w', encoding='UTF-8') as file:
            data = file.write(temp_str)



        

dp = my_class()