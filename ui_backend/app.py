from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    files = {'image': file}
    try:
        print(f"Sending request to http://ai_backend:5001/detect with file {file.filename}")
        response = requests.post('http://ai_backend:5001/detect', files=files, timeout=10)
        print(f"Received response: {response.text}, status: {response.status_code}")
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to ai_backend: {str(e)}")
        return jsonify({'error': 'Failed to connect to detection service'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)