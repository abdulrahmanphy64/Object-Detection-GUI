import os
import sys
import random
from detectors.detect import objectdetection
from PySide6.QtCore import Slot
from PySide6.QtWidgets import *

##### Do not run this file ####
##### Instead Run app.py ####
#### This is only for testing purpose
class Application:

    def __init__(self):
        #self.Detect = objectdetection()
        self.app = QApplication(sys.argv)
        self.setup_ui()
        self.app.exec()


    # Setup the UI for app
    def setup_ui(self):
        self.window = QWidget()
        self.window.setGeometry(100,100,100,100)
        Image = QPushButton("Image")
        Video = QPushButton("Video")
        Webcam = QPushButton("Web Cam")
        vbox = QHBoxLayout(self.window)
        Image.clicked.connect(self.Select_image_file)
        vbox.addWidget(Image)
        vbox.addWidget(Video)
        vbox.addWidget(Webcam)
        self.window.show()

    @Slot()
    def say_hello(self):
        print("Button clicked, Hello!")

    @Slot()
    def Select_image_file(self):
        dialog = QFileDialog.getOpenFileName()
        print(dialog)
        self.imagedetect = objectdetection.image_detection(dialog[0])
        #image = detect.objectdetection.image_detection(dialog)
        print(type(dialog))
        
        #dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        print("File selected successfully")
        



    
    # Create Qt Application

    


if __name__ == "__main__":
    app = Application()
    