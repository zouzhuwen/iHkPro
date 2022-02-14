#导包
import json
import unittest
from api.login import LoginApi
from parameterized import parameterized
from app import BASE_DIR

#构造数据
def bulid_data():
    test_data = []
    file = BASE_DIR+"/data/login.json"
    with open(file,encoding="utf-8") as f:
        data = json.load(f)
        for case_data in data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            returnCode = case_data.get("returnCode")
            returnMsg = case_data.get("returnMsg")

            test_data.append((login_data,status_code,returnCode,returnMsg))
            print("test_data={}".format((login_data,status_code,returnCode,returnMsg)))

    return test_data

#创建测试类
class TestLogin02(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginApi()


    #后置处理

    #定义测试用例
    #登录成功
    @parameterized.expand(bulid_data())
    def test01_login(self,login_data,status_code,returnCode,returnMsg):
        response = self.login_api.login(login_data)
        print(response.json())
        #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(returnCode, response.json().get("returnCode"))
        self.assertIn(returnMsg, response.json().get("returnMsg"))
