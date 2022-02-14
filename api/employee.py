"""
员工添加
员工修改
员工查询
员工删除
"""

# 导包
# 封装类
import app
import requests


class EmployeeApi():
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    #初始化
    def __init__(self):
        self.url_add_employee = app.BASE_URL+"api/os/add-or-edit-user"
        self.url_edit_employee=app.BASE_URL+"api/os/add-or-edit-user"
        self.url_get_employee = app.BASE_URL+"api/os/login-log-list"
        self.url_detele_employee= app.BASE_URL+"api/os/delete-user"
        self.url_get_employee_id = app.BASE_URL+"api/os/user-list"

    # 封装接口
    #根据手机号码查询员工userId,roleId,userName
    def get_employee_id(self,mobile):
        data = {
            "pageSize":10,
            "pageNum":1,
            "startTime": "",
            "endTime": "",
            "storeId": "",
            "roleId": "",
            "keyword":mobile
        }


        #pageSize=10&pageNum=1&startTime=&endTime=&storeId=&roleId=&keyword=13522222225
        userId = requests.get(self.url_get_employee_id, params=data, headers=app.headers_data).json().get("data").get("list")[
            0].get("userId")
        roleId = requests.get(self.url_get_employee_id, params=data, headers=app.headers_data).json().get("data").get("list")[
            0].get("roleId")
        userName = requests.get(self.url_get_employee_id, params=data, headers=app.headers_data).json().get("data").get("list")[
            0].get("userName")
        return userId,roleId,userName


    # 员工添加
    def add_employee(self,data):
        print(app.headers_data)
        return  requests.post(url=self.url_add_employee,data=data,headers=app.headers_data)

    # 员工修改
    def edit_employee(self,data):
        return requests.post(url=self.url_edit_employee,data=data,headers=app.headers_data)

    # 员工查询
    def get_employee(self,data):
        return requests.get(url=self.url_get_employee,params=data,headers=app.headers_data)

    # 员工删除
    def detele_employee(self,data):
        return requests.get(url=self.url_detele_employee,params=data,headers=app.headers_data)



