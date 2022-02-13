# 导包
import time

from app import BASE_DIR
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test01_login import TestLogin
# 组装测试套件

suit =unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestLogin))

# 指定测试报告的路径
report = BASE_DIR+"/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report,"wb") as f:
    # 创建HTML.TestRunner运行器
    runner = HTMLTestRunner(f,title="API Report")
    # 执行测试套件
    runner.run(suit)