from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Главное приложение работает!"})

@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.json
    print(f"Main app received: {data}")
    return jsonify({
        "status": "success", 
        "message": "Данные получены main_app",
        "received_data": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)