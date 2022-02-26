from flask import Flask, render_template, jsonify
from flask_navigation import Navigation
from pymongo import MongoClient

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Test Page', 'test')
])

client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.cisbf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/mbti", methods=["GET"])
def user_get():
    user_list = list(db.hhnn.find({}, {'_id': False}))
    # user_list = None
    # print(user_list)
    return jsonify({'user_list': user_list})


@app.route("/test")
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
