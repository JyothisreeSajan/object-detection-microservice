from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    files = {'image': file}
    response = requests.post('http://ai_backend:5001/detect', files=files)
    
    return response.text, response.status_code
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
