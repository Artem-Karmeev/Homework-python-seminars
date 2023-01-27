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
        

    def init_subject(self, key: str) -> dict:
        self.key = key           
        self.subject_dict = self.my_dict[key]


    def get_subject(self):
        return self.subject_dict


    def update_score(self, surname_key: str, score: str):
        self.subject_dict[surname_key] += f', {score}'
        

    def update_data(self):
        self.my_dict[self.key] = self.subject_dict


    def save_data(self):
        temp_str = ''

        for key in self.my_dict:
            temp_str += f'{key}: '
            for k, v in self.my_dict[key].items():
                temp_str += f'{k} = {v}; '
            temp_str = temp_str[: -2] + '\n' 

        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write(temp_str)



        

dp = my_class()