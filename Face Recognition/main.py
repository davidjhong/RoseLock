import face_recognition
import os, sys
import cv2
import numpy as np
import math

def faceConfidence(faceDistance, faceMatchThreshold = 0.6):
    range = (1.0 - faceMatchThreshold)
    linearVal = (1.0 - faceDistance) / (range * 2.0)

    if faceDistance > faceMatchThreshold:
        return str(round(linearVal * 100, 2)) + '%'
    
    else:
        value = (linearVal +((1.0 - linearVal) * math.pow((linearVal - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


class FaceRecognition:
    faceLocations = []
    faceEncodings = []
    faceNames = []
    knownFaceEncodings = []
    knownFaceNames = []
    processCurrentFrame = True

    def __init__(self):
        self.encodeFaces()
        # encode faces

    def encodeFaces(self):
        for image in os.listdir('faces'):
            faceImage = face_recognition.load_image_file(f'faces/{image}')
            faceEncoding = face_recognition.face_encodings(faceImage)[0] #check this code

            self.knownFaceEncodings.append(faceEncoding)
            self.knownFaceNames.append(image)
            
        print(self.knownFaceNames)

        

if __name__ == '__main__':
    fr = FaceRecognition()
