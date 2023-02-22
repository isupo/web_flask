from flask import Flask
from flask import redirect, url_for, request

from src.db import MyDB


class Shop:
    def __init__(self, dbname: str):
        # я храню базу данных внутри нашего магазина
        self.db = MyDB(dbname)

    def push_new_buy(self, item, quantity, package):
        # я делаю из записей строку
        record = item + ' ' + str(quantity) + ' ' + package
        # с помощью ранее написанного класса мы добавляем запись в хранилище
        self.db.add(record)

    def __str__(self):
        s = ''
        # с помощью ранее написанного класса мы читаем всё из хранилища
        # и просто возращаем
        for el in self.db.output():
            s += el + " <br>"
        return s


shop = Shop('shopdb.txt')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return str(shop) + "ссылочка на добавление"


@app.route('/hello')
def hello_world2():
    return 'hello'


@app.route('/pushdata', methods=['POST', 'GET'])
def push_data():
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        package = request.form['package']
        shop.push_new_buy(item, quantity, package)

        return redirect('/')
    else:

        with open('./html/main.html', 'r', encoding='UTF-8') as f:

            return f.read()


app.run()
