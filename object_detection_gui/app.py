import os
import sys
import random
from detectors.detect import objectdetection
from PySide6.QtCore import Slot
from PySide6.QtWidgets import *

class Application:

    def __init__(self):
        self.Detect = objectdetection()
        self.app = QApplication(sys.argv)
        self.setup_ui()
        self.app.exec()


    # Setup the UI for app
    def setup_ui(self):
        self.window = QWidget()
        self.window.setGeometry(150,150,150,250)
        Image = QPushButton("Image")
        Video = QPushButton("Video")
        Webcam = QPushButton("Web Cam")
        vbox = QHBoxLayout(self.window)
        Image.clicked.connect(self.Select_image_file)
        Video.clicked.connect(self.Select_video_file)
        Webcam.clicked.connect(self.Detect.webcam_detection)
        vbox.addWidget(Image)
        vbox.addWidget(Video)
        vbox.addWidget(Webcam)
        self.window.show()


    # For image detection
    @Slot()
    def Select_image_file(self):
        dialog = QFileDialog.getOpenFileName()
        print(dialog)
        self.imagedetect = self.Detect.image_detection(dialog[0])
        print("Image detected successfully!!")

    @Slot()
    def Select_video_file(self):
        file = QFileDialog.getOpenFileName()
        print(file)
        self.videodetect = self.Detect.video_detection(file[0])
        print("video detection successfull!!")
        



    

    


if __name__ == "__main__":
    app = Application()
    