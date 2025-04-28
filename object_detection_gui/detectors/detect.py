import cv2
import os
from pathlib import Path
from ultralytics import YOLO

class objectdetection:
    def __init__(self):
        self.image_detection_model = YOLO("yolov8n.pt")
        self.video_detection_model = YOLO("yolov8s.pt")

    # This function detect the image
    def image_detection(self, image_path):
        ext = os.path.splitext(image_path)[1].lower()
        if ext in ['.jpg','.jpeg','.png']:
            result = self.image_detection_model(image_path)
            result[0].show()
            
        print("Select proper file format")
        


    def video_detection(self, video_path):
        frame = video_path
        ext = os.path.splitext(video_path)[1].lower()
        if ext  in ['.mp4']:
            results = self.video_detection_model.track(frame, stream = True)
            cv2.namedWindow("Video detection", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Video detection", 800, 430)
            for result in results:
                frame = result.plot()
                cv2.imshow("Video detection", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()
            print("Detection Successfull!!")

        print("Select Proper file format")

    def webcam_detection(self):
        path = 0
        results = self.video_detection_model.track(path, stream = True)
        cv2.namedWindow("Video detection", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Video detection", 800, 430)
        for result in results:
            frame = result.plot()
            cv2.imshow("Video detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        print("Detection Successfull!!")








if __name__ == "__main__":
    simpledetection = objectdetection()



