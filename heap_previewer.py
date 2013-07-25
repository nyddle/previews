# -*-coding: utf-8 -*-
from flask import Flask, request, jsonify

from app.models import MongoDbClient
from app.adapters import EmbedLy

app = Flask(__name__)
mongodb = MongoDbClient()

@app.route('/post', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        adapter = EmbedLy(request.form['url'])
        data = jsonify(adapter.read())
        for entry in data:
            mongodb.add_url(entry['url'], entry['title'], entry['description'], entry['content'])
        return jsonify({'result': True})
    return jsonify({'result': False})


@app.route('/get/<url>', methods=['GET', 'POST'])
def get(url):
    return jsonify(mongodb.get_url(url))


if __name__ == '__main__':
    app.run(debug=True)
