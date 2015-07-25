import os
from flask import Flask, redirect, request, render_template, url_for
from pymongo import MongoClient


DB_PORT_27017_TCP_ADDR = os.environ.get('DB_PORT_27017_TCP_ADDR', '127.0.0.8')


app = Flask(__name__)

client = MongoClient(DB_PORT_27017_TCP_ADDR, 27017)
db = client.tododb


@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
