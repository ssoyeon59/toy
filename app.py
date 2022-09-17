from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://test:sparta@cluster0.nbw8ry5.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route("/perfume/like", methods=["POST"])
def perfume_like():
    id_receive = request.form['id_give']
    db.perfumes.update_one({'id': int(id_receive)}, {'$set': {'like': 1}})

    return jsonify({'msg': '좋아요!'})

@app.route("/perfume/nolike", methods=["POST"])
def perfume_nolike():
    id_receive = request.form['id_give']
    db.perfumes.update_one({'id': int(id_receive)}, {'$set': {'like': 0}})

    return jsonify({'msg': '좋아요 취소!'})
    
    if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
