# 搭建框架： 分析流程 所需函数 以及相应属性

# 导包
import json
import unittest

# 创建测试类
from auto_frame.API.LoginAPI import Login
from parameterized import parameterized

# 读取json文件
from auto_frame_itheima import app


def read_from_json():
    # 1 创建空列表接收读取的数据
    data = []

    # 2 创建文件流，使用json解析，并将解析结果转换成元组添加进列表
    with open(app.ABS_DIR + "/Login_case.Json") as f:
        values = json.load(f)       #获取所有值
        for value in values:       #获取值的mobile code ...组织成元组
            mobile = values.get("mobile")
            code = values.get("code")
            status_code = values.get("status_code")
            message = values.get("message")
            case_one = (mobile, code, status_code, message)
            # 元组添加进列表
            data.append(case_one)

    # 3 返回列表
    return data


class TestLogin(unittest.TestCase):    # 集成

    #初始化函数创建Login对象
    def setUp(self):
        self.login = Login()     # 创建API对象


    # 创建登录函数 测试登录
    # 函数1 获取验证码  只需提交正确手机号即可
    def test_get_verity_code(self):
        # 调用API实现
        response = self.login.get_verity_code("15816875503")
        print(response.json())

    # 函数2  测试登录
    # 参数化导入data的测试数据
    @parameterized.expand(read_from_json)
    def test_login(self, mobile, code, status_code, message):
        print(mobile, code, status_code, message)

        # 调用API实现
        response = self.login.login(mobile, code)
        print(response.text)

        # 响应判断
         # 判断状态
        self.assertEqual(status_code,response.status_code)

         # 判断响应体
        self.assertIn(message,response.text)

    # 编写成功登录测试函数
    def test_Login_success(self):
        # 调用API 并传入正确的手机号和验证码

        response = self.login.login("15816875503", "")
        token = response.json().get("data").get("token")  # 从响应体获取token
        app.TOKEN = token

        # 断言
        self.assertEqual(201, response.status_code)
        self.assertIn("ok", response.text)