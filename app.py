from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.cisbf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mbti", methods=["GET"])
def user_get():
    user_list = list(db.hhnn.find({}, {'_id': False}))
    print(user_list)
    return jsonify({'user_list': user_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
