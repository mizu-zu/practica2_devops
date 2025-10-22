from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    data['message'] += ' processed by Service 2'
    
    # Используем имя сервиса вместо host.docker.internal
    main_app_url = f"http://main_app:8000/receive"
    
    try:
        response = requests.post(main_app_url, json=data, timeout=5)
        print(f"Sent to main_app: {data}")
        return {'processed_data': data, 'main_app_response': response.json()}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)