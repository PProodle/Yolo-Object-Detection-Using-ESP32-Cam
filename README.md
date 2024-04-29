# ESP32-CAM Image Server with YOLO Object Detection

## Project Description
This project combines an ESP32-CAM module to serve images at different resolutions and a YOLO object detection model for detecting objects within the captured images.

## Table of Contents
- [Project Name](#project-name)
  - [Project Description](#project-description)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Getting Started
To get a copy of the project running on your local machine, follow the instructions below.

### Prerequisites
- Arduino IDE for ESP32 development
- Python environment with OpenCV and ultralytics library

### Installation
1. Clone the repository to your local machine.
2. Open the ESP32.ino file in the Arduino IDE and upload it to the ESP32 board.
3. Install the required Python dependencies using `pip install opencv-python ultralytics`.

## Usage
- After uploading the ESP32 sketch, the ESP32-CAM module will serve images at different resolutions.
- Run the YOLO.py script to perform object detection on the captured images. Ensure the YOLO model file 'yolov8n.pt' is present in the specified directory.

## Contributing
Contributions are welcome! If you have ideas for improvements or new features, please submit an issue or open a pull request.
