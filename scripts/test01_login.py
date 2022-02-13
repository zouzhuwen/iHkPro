#导包
import unittest
from api.login import LoginApi
import app

#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginApi()


    #后置处理

    #定义测试用例
    #登录成功
    def test01_case001(self):
        response = self.login_api.login({"loginName":"13500000000","password":"e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        #断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("0000", response.json().get("returnCode"))
        self.assertIn("Success", response.json().get("returnMsg"))

        #print(response.json().get("data").get("token"))
        app.TOKEN="token={}".format(response.json().get("data").get("token"))
        app.headers_data["Cookie"]=app.TOKEN
        print(app.headers_data)

    #密码错误
    def test02_case002(self):
        response = self.login_api.login({"loginName":"13500000000","password":"1e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        #断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("IHKER04", response.json().get("returnCode"))
        self.assertIn("账号或密码有误，请重新输入。提示：账号或密码输入错误超过5次，系统将锁定30分钟", response.json().get("returnMsg"))

    # 账号不存在
    def test03_case003(self):
        response = self.login_api.login({"loginName": "13500000999",
                                         "password": "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("IHK14", response.json().get("returnCode"))
        self.assertIn("用户不存在", response.json().get("returnMsg"))

    # 账号为空
    def test04_case004(self):
        response = self.login_api.login({"loginName": "",
                                         "password": "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("UAA88", response.json().get("returnCode"))
        self.assertIn("参数异常", response.json().get("returnMsg"))

    # 密码为空
    def test05_case005(self):
        response = self.login_api.login({"loginName": "13500000000",
                                         "password": ""})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("IHKER04", response.json().get("returnCode"))
        self.assertIn("账号或密码有误，请重新输入。提示：账号或密码输入错误超过5次，系统将锁定30分钟", response.json().get("returnMsg"))

    # 账号密码都为空
    def test06_case006(self):
        response = self.login_api.login({"loginName": "",
                                         "password": ""})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("UAA88", response.json().get("returnCode"))
        self.assertIn("参数异常", response.json().get("returnMsg"))

    # 账号少于11位
    def test07_case007(self):
        response = self.login_api.login({"loginName": "1350000000",
                                         "password": "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("IHK14", response.json().get("returnCode"))
        self.assertIn("用户不存在", response.json().get("returnMsg"))

    # 账号大于11位
    def test08_case008(self):
        response = self.login_api.login({"loginName": "135000000001",
                                         "password": "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("IHK14", response.json().get("returnCode"))
        self.assertIn("用户不存在", response.json().get("returnMsg"))

    # 不传loginName参数
    def test09_case009(self):
        response = self.login_api.login({
                                         "password": "e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("UAA88", response.json().get("returnCode"))
        self.assertIn("参数异常", response.json().get("returnMsg"))

    # 不传password参数
    def test10_case010(self):
        response = self.login_api.login({"loginName": "13500000000"})
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("500", response.json().get("returnCode"))
        self.assertIn("系统处理异常，请联系管理员！", response.json().get("returnMsg"))

    # 不传loginName和password参数
    def test11_case011(self):
        response = self.login_api.login({})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual("UAA88", response.json().get("returnCode"))
        self.assertIn("参数异常", response.json().get("returnMsg"))
