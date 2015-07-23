import os
from flask import Flask, redirect, request, render_template, url_for
from pymongo import MongoClient


INJILA_DB_URL = os.environ.setdefault('INJILA_DB_URL', '127.0.0.1')
INJILA_SERVICE_URL = os.environ.setdefault('INJILA_SERVICE_URL', '127.0.0.1')


app = Flask(__name__)

client = MongoClient('127.0.0.1', 27017)
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
    app.run(host='127.0.0.1', port=8080, debug=True)
