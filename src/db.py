class MyDB:
    def __init__(self, filename='db.txt'):
        self.db = filename
        with open(filename, 'a', encoding='UTF-8') as f:
            f.write('')

    def add(self, data: str):
        with open(self.db, 'a', encoding='UTF-8') as f:
            f.write(data + '\n')

    def output(self):
        with open(self.db, encoding='UTF-8') as f:
            return f.readlines()
