# 作用  运行并生成html测试报告

#  0 导包
import unittest

# 1 组织测试套件
from datetime import time
from auto_frame import app
from auto_frame.CASE import TestTPshop
from auto_frame.tools import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTPshop))

# 2  使用htmlTestRunner运行套件
#  声明测试报告保存文件
file = app.BASE_PATH+"/report/hello.html"    #  此处生成报告名称不写死， 使用时间戳：

file = app.BASE_PATH+"/report/" + time.strftime("%Y-%m-%H%M%S") + ".html"

# 打开文件流执行写操作
with open(file,"wb") as f:

    #写出运行结果
    runner = HTMLTestRunner(f, title="接口测试报告", description = "测试登录业务")
    runner.run(suite)


