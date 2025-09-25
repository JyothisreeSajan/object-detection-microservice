from flask import Flask, request
from ultralytics import YOLO
import  numpy as np
import cv2

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
    results = model(img)
    annotated_img = results[0].plot()

    cv2.imshow("YOLOv8 Detection", annotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
