# Real-Time Object Detection GUI

This project is a GUI application that uses real-time object detection to process video feeds. The object detection is handled through a pre-trained model. Users can upload videos,images and even detect through webcam  which are then processed to detect and highlight objects in real-time. 

## Features

- Upload video, image  files for object detection.
- Real-time object detection using pre-trained models.
- Display video with detected objects highlighted.
- Easy-to-use GUI interface.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

Make sure you have Python 3.x and pip installed.

1. Clone the repository:

    ```bash
    git clone https://github.com/abdulrahmanphy64/Object-Detection-GUI
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. If you haven't already, download or prepare a pre-trained object detection model that works with your project. You can modify the object detection logic as needed in the `detect.py` file.

### Running the Application

1. Start the app.py:

    ```bash
    python app.py
    ```



2. Upload a video,image or webcam and the object detection will begin processing in real-time.


