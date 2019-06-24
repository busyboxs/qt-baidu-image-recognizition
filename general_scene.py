import requests


class General(object):

    def __init__(self, image_base64, token_key, baike_num=0):
        self.image_base64 = image_base64
        self.token_key = token_key
        self.baike_num = baike_num
        self.data = self.get_data()

    def get_data(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        params_d = dict()
        params_d['image'] = str(self.image_base64, encoding='utf-8')
        params_d['baike_num'] = self.baike_num
        access_token = self.token_key
        request_url = request_url + "?access_token=" + access_token
        res = requests.post(url=request_url,
                            data=params_d,
                            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        data = res.json()
        assert 'error_code' not in data, f'Error: {data["error_msg"]}'
        return data

    def get_result_num(self):
        return self.data['result_num']

    def get_log_id(self):
        return self.data['log_id']

    def get_result(self):
        return self.data['result']

    def parse_data(self):
        result_num = self.get_result_num()
        result = self.get_result()
        res = list()
        for i in range(result_num):
            if i < self.baike_num:
                res.append((result[i]['keyword'], result[i]['score'], result[i]['baike_info']))
            else:
                res.append((result[i]['keyword'], result[i]['score'], None))
        return res




