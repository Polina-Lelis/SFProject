# import os
# import requests
# import asyncio
# import io
# import glob
# import sys
# import time
# import uuid
# import cv2
# from urllib.parse import urlparse
# from io import BytesIO
import matplotlib.pyplot as plt
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = "369beb885ba34c55804a073c2e751799"
    ENDPOINT = "https://facelelis.cognitiveservices.azure.com/"
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

def get_face_landmarks(local_image_path):
   """  local_image = open(local_image_path, "rb")

    face_client = get_face_client()
    attributes = ["emotion", "glasses", "smile"]
    include_id = True
    include_landmarks = True

    detected_faces = face_client.face.detect_with_stream(local_image, include_id, return_face_landmarks=True, return_face_attributes = attributes, recognition_model='recognition_01', detectionModel='detection_01')
    landmark = detected_faces[0].face_landmarks
    #print(landmark)
    return landmark """

def is_criminal(local_image_path):
    local_image = open(local_image_path, "rb")
    
    face_client = get_face_client()
    attributes = ["emotion", "glasses", "smile"]
    include_id = True
    include_landmarks = True

    detected_faces = face_client.face.detect_with_stream(local_image, include_id, return_face_landmarks=True, return_face_attributes = attributes, recognition_model='recognition_01', detectionModel='detection_01')
    landmark = detected_faces[0].face_landmarks
    #print(landmark)
    k = 0
    #Высота губ
    top_lip_y = landmark.upper_lip_top.y
    top_bottom_lip_y = landmark.upper_lip_bottom.y
    bottom_top_lip_y = landmark.under_lip_top.y
    bottom_lip_y = landmark.under_lip_bottom.y
    height_mouth = top_lip_y - bottom_lip_y

    top_lip = top_lip_y - top_bottom_lip_y
    bottom_lip = bottom_top_lip_y - bottom_lip_y

    #Ширина губ
    mouth_l_x = landmark.mouth_left.x
    mouth_r_x = landmark.mouth_right.x
    width_mouth = mouth_r_x - mouth_l_x

    #Отношение длины и ширины губ
    #print(abs(width_mouth/height_mouth))
    if (abs(width_mouth/height_mouth) < 3.2 or abs(width_mouth/height_mouth) > 3.9 ):
        k += 1

    #Отношение высот правого глаза
    eye_r_top_y = landmark.eye_right_top.y
    eye_r_bottom_y = landmark.eye_right_bottom.y
    eye_r_height = eye_r_top_y - eye_r_bottom_y

    eye_r_inner_x = landmark.eye_right_inner.x
    eye_r_outer_x = landmark.eye_right_outer.x
    eye_r_width = eye_r_inner_x - eye_r_outer_x

    #print('Отношение высот правого глаза')
    #print(abs(eye_r_width/eye_r_height))

    if(abs(eye_r_width/eye_r_height) > 2.6):
        k += 1

    #Отношение высот левого глаза
    eye_l_top_y = landmark.eye_left_top.y
    eye_l_bottom_y = landmark.eye_left_bottom.y
    eye_l_height = eye_l_top_y - eye_l_bottom_y

    eye_l_inner_x = landmark.eye_left_inner.x
    eye_l_outer_x = landmark.eye_left_outer.x
    eye_l_width = eye_l_inner_x - eye_l_outer_x

    #print('Отношение высот левого глаза')
    #print(abs(eye_l_width/eye_l_height))

    if (abs(eye_l_width/eye_l_height) >2.6):
        k += 1

    #Высота губы
    bottom_lip_y = landmark.under_lip_bottom.y
    height_mouth = top_lip_y - bottom_lip_y


    #Соотношение расстояния между глаз
    eye_width = eye_r_outer_x - eye_l_outer_x
    eye_inside_length = eye_r_inner_x - eye_l_inner_x

    nose_left = landmark.nose_root_left.y
    nose_right = landmark.nose_root_right.y
    center_nose = landmark.nose_tip.y
    length_nose = nose_right - center_nose

    #Соотношение глаз с носом
    #print('Соотношение глаз с носом')
    #print(abs(length_nose/eye_r_height))

    if(abs(length_nose/eye_r_height) > 3.9):
        k += 1
    if(abs(length_nose/eye_l_height) > 3.9):
        k += 1

    #print(k)
    answer = False
    if k >= 2:
        answer = True
    else: 
        answer = False
        
    return answer 
    
