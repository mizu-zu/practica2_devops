from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    data = {'message': 'Привет от Службы 1'}
    
    # Используем имя сервиса вместо host.docker.internal
    service2_url = f"http://service2:8002/process"
    
    try:
        response = requests.post(service2_url, json=data, timeout=5)
        print(f"Sent to service2: {data}")
        return {'sent_to_service1': data, 'service2_response': response.json()}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)