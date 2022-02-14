#导包
import unittest
import requests
import app
from app import BASE_URL,BASE_DIR

class Upload_picture():
    def __init__(self):
        self.url = BASE_URL+"api/os/upload-picture"


    def upload_picture(self,files):
        proxies = {
            'http': 'http://127.0.0.1:8888',
            'https': 'http://127.0.0.1:8888'
        }
        #上传文件的路径
        path = requests.post(url=self.url, files=files, headers=app.headers_data).json().get("data")
        print("path={}".format(path))
        return path
        #返回数据

        # "returnCode": "0000",
        # "returnMsg": "Success",
        # "nonceStr": "3195b15fc7694042a8f7b79c6b29ecb5",
        # "success": true,
        # "data": "os/20220214/759848f57533438cb972cdcd175e2252.jpg"

# path = BASE_DIR+"/data/图片.jpg"
#
# files = {
# 'file':open(path,'rb')
# }
# Upload_picture().upload_picture(files)