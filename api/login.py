"""
被测系统的接口封装
登录：http://192.168.0.99:9080/api/uaa/web-backend-os-login
"""

#导包

import requests

#创建接口类

class LoginApi():
    #初始化
    def __init__(self):
        self.url = "http://192.168.0.99:9080/api/uaa/web-backend-os-login"


    #定义接口调用方法
    def login(self,login_data):
        proxies = {
            'http': 'http://127.0.0.1:8888',
            'https': 'http://127.0.0.1:8888'
        }

        return requests.post(url=self.url,json=login_data)