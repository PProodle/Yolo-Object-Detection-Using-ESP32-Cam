import cv2
import urllib.request
import numpy as np
from ultralytics import YOLO

# Replace the URL with the IP camera's stream URL
url = 'http://192.168.195.147/cam-lo.jpg'

# Initialize YOLO model
model = YOLO('yolov8n.pt')

# Create a VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the IP camera stream is opened successfully
if not cap.isOpened():
    print("Failed to open the IP camera stream")
    exit()

# Read and display video frames
while True:
    # Read a frame from the video stream
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    im = cv2.imdecode(imgnp, -1)

    # Perform object detection on the frame
    results = model(im, show=True)  # Perform object detection and show results

    cv2.imshow('live Cam Testing', im)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
