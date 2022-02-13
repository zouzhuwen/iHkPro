import os


#项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

#项目域名
BASE_URL="http://192.168.0.99:9080/"


#token
TOKEN= None

#请求头数据
headers_data={
    "Cookie":"token=8d3cb438228b4aa18fdddb48fefdf828"
}