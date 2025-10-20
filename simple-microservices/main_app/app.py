from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    print('Hello, World! Received:', data)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)