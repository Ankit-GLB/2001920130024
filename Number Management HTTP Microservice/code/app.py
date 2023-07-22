from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    numbers = set()

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.ok:
                data = response.json()
                if 'numbers' in data:
                    numbers.update(data['numbers'])
        except requests.Timeout:
            pass

    numbers_list = sorted(list(numbers))
    return jsonify({"numbers": numbers_list})

if __name__ == '__main__':
    app.run(port=8008)
