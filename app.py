from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

url = 'http://www.yes24.com/24/category/bestseller'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

best_list = soup.select('#bestList > ol > li')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bestseller', methods=["GET"])
def best_get():
    sorted_list = []
    for best in best_list:
        img_url = best.select_one('p:nth-child(2) > a > img')['src']
        title = best.select_one('p:nth-child(3) > a').text
        sorted_list.append({'img_url': img_url, 'title': title})
    print(sorted_list)
    return jsonify({'best_list': sorted_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
