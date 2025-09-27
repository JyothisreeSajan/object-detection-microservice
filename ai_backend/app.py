from flask import Flask, request, jsonify
from ultralytics import YOLO
import numpy as np
import cv2
import os
import json

app = Flask(__name__)
model = YOLO('models/yolov8n.pt')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        print("Error: No image provided")
        return "No image provided", 400
    
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        print("Error: Could not load image")
        return "Failed to load image", 400
    
    results = model(img)
    annotated_img = results[0].plot()

    # Prepare structured JSON with detections
    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            conf = float(box.conf[0])
            detections.append({
                'x': x1,
                'y': y1,
                'width': x2 - x1,
                'height': y2 - y1,
                'label': label,
                'confidence': conf
            })

    # Save annotated image and JSON
    output_dir = '/app/outputs'
    os.makedirs(output_dir, exist_ok=True)
    output_img_path = os.path.join(output_dir, 'output.jpg')
    output_json_path = os.path.join(output_dir, 'output.json')
    cv2.imwrite(output_img_path, annotated_img)
    with open(output_json_path, 'w') as f:
        json.dump({'objects': detections}, f)
    print(f"Output saved to {output_img_path} and {output_json_path}")

    # Return structured JSON
    return jsonify({'objects': detections}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)