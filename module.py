import cv2
import matplotlib.pyplot as plt
import easyocr
from ultralytics import YOLO
import json
import os



def load_object(path1):
    model1 = YOLO(path1)
    return model1 

def load_ocr():
    model2 = easyocr.Reader(['en'])
    return model2

def load_image(path3):
    image = cv2.imread(path3)
    return image

def get_coordinates(image, obj_det):
    result = obj_det.predict(image, verbose = False)
    x1 = int(result[0].boxes.xyxy.numpy()[0][0])
    y1 = int(result[0].boxes.xyxy.numpy()[0][1])
    x2 = int(result[0].boxes.xyxy.numpy()[0][2])
    y2 = int(result[0].boxes.xyxy.numpy()[0][3])
    return x1, y1, x2, y2

def cropped_image(img, coordinates):
    new_x1 = coordinates[0]
    new_y1 = coordinates[1]
    new_x2 = coordinates[2]
    new_y2 = coordinates[3]
    cropped_img = img[new_y1:new_y2, new_x1:new_x2]
    return cropped_img

def extract_text(image, ocr, database_path):
    
    with open(database_path, "r") as file:
        db = json.load(file)
        file.close()

    characters = ocr.readtext(image)
    state_name = db.get(characters[0][1][:2]) 
    return state_name



