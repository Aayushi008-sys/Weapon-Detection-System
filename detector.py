from ultralytics import YOLO 
class ObjectDetector: 
  def __init__(self): 
    self.knife_model = YOLO("weights/knife_yolo.pt") 
    self.person_model = YOLO("yolov8n.pt") 
def detect_knife(self, frame): 
    return self.knife_model(frame, conf=0.4) 
def detect_person(self, frame): 
    return self.person_model(frame, classes=[0], conf=0.5)
