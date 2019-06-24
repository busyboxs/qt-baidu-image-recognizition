import cv2
import requests
from pprint import pprint
import base64
from general_scene import General
from object_detect import ObjectDetect
from utils import pic_base64, draw_zh, get_token_key


def detect(image_name, color):
    token_key = '24.ee979f01de5bb475b60df105dadaefad.2592000.1563092622.282335-16137500'
    # image_name = 'images/001.png'
    image = cv2.imread(image_name)
    image_base64 = pic_base64(image_name)
    general = General(image_base64, token_key, 1)
    obj = ObjectDetect(image_base64, token_key)
    general_data = general.parse_data()
    bbox = obj.parse_data()
    name = general_data[0][0]
    score = general_data[0][1]
    baike = general_data[0][2]
    image = obj.draw_bbox(image, color)
    # draw_zh(image, name, bbox[0], bbox[1] - 16, color)
    cv2.cvtColor(image, cv2.COLOR_BGR2RGB, image)
    return image, name, score, baike
