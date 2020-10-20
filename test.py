#!/usr/bin/env python3
from flask import Flask, request
from bson.json_util import dumps
from flask_cors import CORS
from flask_pymongo import PyMongo
import json

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
#comment

app.config["MONGO_URI"] = "mongodb://localhost:27017/bookstore"
mongo = PyMongo(app)

def pack(book):
    return json.loads(book.decode('utf-8'))

def unpack(book):
    return dumps(book, indent=2)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/books', methods=['POST'])
def post_books():
    mongo.db.books.insert_one(pack(request.data))
    return 'Books posted.'

@app.route('/books', methods=['GET'])
def get_books():
    result = mongo.db.books.find({}) 
    return unpack(result)

@app.route('/books', methods=['DELETE'])
def delete_books():
    mongo.db.books.delete_many({})

    return 'All books deleted.'


@app.route('/book/<id>', methods=['GET'])
def get_id(id):
    result = mongo.db.books.find({'id':id})
    return unpack(result)

@app.route('/book/<id>', methods=['PUT'])
def put_id(id):
    mongo.db.books.update_one({'id':id},{"$set":pack(request.data)})
    return "Book " + id + " placed."

@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({'id':id})
    return 'Book '+id+' deleted.'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')