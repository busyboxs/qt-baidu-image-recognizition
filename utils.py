import freetype
import requests
import base64


def get_token_key():
    client_id = 'add your API key here'  # API key
    client_secret = 'add your Secret key here'  # Secret key
    url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
        f'&client_id={client_id}&client_secret={client_secret}'
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    res = requests.post(url, headers=headers)
    token_content = res.json()
    assert "error" not in token_content, f"{token_content['error_description']}"
    token_key = token_content['access_token']
    return token_key


def pic_base64(image):
    with open(image, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data


def draw_zh(image, texts, left, top, color):
    face = freetype.Face("font/msyh.ttc")
    face.set_char_size(32*32)
    last_left = 0
    for text in texts:
        face.load_char(text)
        bitmap = face.glyph.bitmap
        # print(bitmap.buffer)
        # print(bitmap.rows)
        # print(bitmap.width)
        rows = bitmap.rows
        cols = bitmap.width
        buffer = bitmap.buffer
        # print(len(buffer))
        start = (16 - rows) // 2
        for i in range(top + start, top + rows + start):
            for j in range(left + last_left, left + cols + last_left):
                if buffer[(i - top - start) * cols + (j - left - last_left)] != 0:
                    for k in range(3):
                            image[i][j][k] = color[k]
        last_left += bitmap.width + 1
