# -*- encoding: utf-8 -*-
import requests
import cv2


class ObjectDetect(object):

    def __init__(self, image_base64, token_key, with_face=1):
        self.image_base64 = image_base64
        self.token_key = token_key
        self.with_face = with_face
        self.data = self.get_data()

    def get_data(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
        params_d = dict()
        params_d['image'] = str(self.image_base64, encoding='utf-8')
        params_d['with_face'] = self.with_face
        access_token = self.token_key
        request_url = request_url + "?access_token=" + access_token
        res = requests.post(url=request_url,
                            data=params_d,
                            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        data = res.json()
        assert 'error_code' not in data, f'Error: {data["error_msg"]}'
        return data

    def get_log_id(self):
        return self.data['log_id']

    def get_result(self):
        return self.data['result']

    def parse_data(self):
        result = self.get_result()
        bbox = list()
        bbox.append(result['left'])
        bbox.append(result['top'])
        bbox.append(result['left'] + result['width'])
        bbox.append(result['top'] + result['height'])
        return bbox

    def draw_bbox(self, im, color):
        bbox = self.parse_data()
        cv2.rectangle(im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 6)
        return im
