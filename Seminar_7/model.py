from copy import deepcopy
class Options:
    phone_book = []
    phone_book_copy = []
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
        self.phone_book_copy = deepcopy(self.phone_book)

    def save(self):
        data = []
        for line in self.phone_book:
            data.append(';'.join(line))
        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write('\n'.join(data))

    def search(self, user_search: str) -> list:
        search_res = []
        for line in self.phone_book:
            for field in line:
                if user_search in field:
                    search_res.append(line)
                    break
        return search_res

    def search_index(self, user_search: str) -> list:
        search_res = []
        for i in range(len(self.phone_book)):
            for j in self.phone_book[i]:
                if user_search in j:
                    search_res.append(i)
                    search_res.append(self.phone_book[i])
                    break
        return search_res

    def delete(self, index: int):
        del self.phone_book[index]

    def change(self, li: list, index: int):
        self.phone_book[index] = li

    def check_changes(self) -> bool:
        res = False
        if self.phone_book == self.phone_book_copy:
            res = True
            return res
        else:
            return res




dp = Options()