from flask import Flask
import requests

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    data = {'message': 'Привет от Службы 1'}
    requests.post('http://service2:8002/process', json=data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)