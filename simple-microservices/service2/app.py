from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    data['message'] += ' processed by Service 2'
    requests.post('http://host.docker.internal:8000/receive', json=data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)