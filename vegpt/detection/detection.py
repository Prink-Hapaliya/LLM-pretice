from ultralytics import YOLO

class detection:
    def __init__(self):
        self.model = YOLO('yolov8n.pt') 

    def run(self, image):
        self.image=image
        result = self.model(self.image) 
        return self.image