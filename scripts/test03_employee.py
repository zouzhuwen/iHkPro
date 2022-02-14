#导包
import unittest
from api.employee import EmployeeApi
from utils import common_assert
from api.upload_picture import Upload_picture
import app


#创建类
class TestEmployee(unittest.TestCase):
    employee_userid = None
    employee_roleId = None
    employee_userName=None


    def setUp(self):
        self.employee_api = EmployeeApi()
        self.upload_picture=Upload_picture()


    #添加员工
    def test01_add_employee(self):
        #上传头像
        files = {
            "file":open(app.BASE_DIR+"/data/图片.jpg","rb")
        }
        path =self.upload_picture.upload_picture(files)
        data = {
            "userName":"xx",
            "mobile":"13522222226",
            "storeId":"880034396923645952",
            "roleId":"882344396056453120",
            "password":"e52f073160e5604f72b24a7d6df0d526b5c0b0e2fa7ecac31ca45223ebe9a0d1",
            "file":path
        }

        reponse = self.employee_api.add_employee(data)
        print(reponse.json())

        #断言
        common_assert(self,reponse) #使用公共断言方法的默认值

        #获取创建的员工userid 和roleId和userName
        TestEmployee.employee_userid,TestEmployee.employee_roleId,TestEmployee.employee_userName = self.employee_api.get_employee_id(data["mobile"])


    # 编辑员工
    def test02_edit_employee(self):
        data = {
            "userId":TestEmployee.employee_userid,
            "userName": "xxoo",
            "mobile": "13522222226",
            "storeId": "880034396923645952",
            "roleId": "882344396056453120",
            "beforeRoleId": "882344396056453120"
        }

        reponse = self.employee_api.edit_employee(data)
        print(reponse.json())

        #更新userid 和roleId和userName的值
        TestEmployee.employee_userid, TestEmployee.employee_roleId, TestEmployee.employee_userName = self.employee_api.get_employee_id(
            data["mobile"])

        # 断言
        common_assert(self,reponse)



    # 查看员工详情
    def test03_get_employee(self):
        data = {
            "pageSize":10,
            "pageNum": 1,
            "userId": TestEmployee.employee_userid
        }

        reponse = self.employee_api.get_employee(data)
        print(reponse.json())

        # 断言
        common_assert(self,reponse)



    # 删除员工
    def test04_delete_employee(self):

        data = {
            "userName":TestEmployee.employee_userName,
            "userId": TestEmployee.employee_userid+":"+TestEmployee.employee_roleId
        }

        reponse = self.employee_api.detele_employee(data)
        print(reponse.json())

        # 断言
        common_assert(self,reponse)