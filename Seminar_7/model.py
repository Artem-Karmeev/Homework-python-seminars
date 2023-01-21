class Options:
    phone_book = []
    path = ''

    def __init__(self, path: str = r'Seminar_7\txt\data.txt'):
        self.path = path

    def get(self):
        return self.phone_book

    def update(self, contact: list):
        self.phone_book.append(contact)

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                self.phone_book.append(line.strip().split(';'))

    def save(self):
        data = []
        for line in self.phone_book:
            data.append(';'.join(line))
        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write('n'.join(data))

    def search(self, user_search: str):
        search_res = []
        for line in self.phone_book:
            for field in line:
                if user_search in field:
                    search_res.append(line)
                    break
        return search_res

dp = Options()