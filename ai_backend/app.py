from ultralytics import YOLO
import cv2

model = YOLO('models/yolov8n.pt')

image_path = 'sample.jpg'
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load image")
else:
    
    results = model(img)
    annotated_img = results[0].plot()

    
    cv2.imshow("YOLOv8 Detection", annotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
