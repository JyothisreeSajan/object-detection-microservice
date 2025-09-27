# Object Detection Microservice Documentation

## Prerequisites
- Docker: Install Docker Desktop[](https://www.docker.com/products/docker-desktop).
- Python (Flask): Included in the Docker image.
- Lightweight Detection Model: YOLOv8n (auto-downloaded by Ultralytics).

## Steps to Replicate
## Steps to Replicate
1. Clone the GitHub repo or unzip the `technical-assessment.zip` folder.
2. Ensure the `outputs` folder exists in the project root (create with `mkdir outputs` if needed).
3. Verify `sample.png` is in the project root (included as an example; replace with your own `.png` if desired).
4. Run `docker-compose up --build` to start the services.
5. Test the API with the following command:
curl -X POST -F "image=@sample.png" http://localhost:5000/upload
6. Check `outputs/output.jpg` (with bounding boxes) and `outputs/output.json` for the latest results.
7. Sample outputs are included in `sample_outputs/` (`sample_output.jpg` and `sample_output.json`) for reference.

## How I Reached the Solution
- Used Flask for `ui_backend` (image upload) and `ai_backend` (detection).
- Selected YOLOv8n for lightweight object detection (reference: https://github.com/ultralytics/ultralytics).
- Implemented Docker with `docker-compose` for portability.
- Configured `ui_backend` to forward images to `ai_backend` via requests.
- Enhanced `ai_backend` to return structured JSON and save `output.jpg` and `output.json` in the `outputs` folder (mounted volume).
- Troubleshooted volume mounts, file paths, and method allowed errors.

## References
- Ultralytics YOLO: https://github.com/ultralytics/ultralytics
- Flask: https://flask.palletsprojects.com
- Docker Compose: https://docs.docker.com/compose


