# 需求 使用unittest集成requests库，测试获取验证码 登录 订单查询

# 搭框架
import requests
import unittest

class TestTPshop(unittest.TestCase):
    # 创建setUp函数初始化session
    def setUp(self):
        self.session =requests.Session()

    #销毁session
    def teardown(self):
        self.session.close()

     # 2 requests库调用各个接口
    # 3 断言判断响应结果
    # 函数1 测试验证码获取
    def test_get_verity_code(self):
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print('响应体', response.content)

        # 断言响应头
        print("内容类型", response.headers.get("Content-Type"))
        self.assertEqual("img/png", response.headers.get("Content-Type"))


    # 函数2 测试登录
    def test_login(self):
        # 登录之前需要调用获取验证码
        self.test_get_verity_code()
        mydata = {"username": "13246758795", "password": "tttangdo", "verify_code": "666574"}
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=do_login", data = mydata)
        print('响应体', response.jason())

        # 断言   可以同时添加多个断言
        print(response.json().get("msg"))
        self.assertIn("登陆成功", response.json().get("msg"))

    # 函数3 测试订单查询
    def test_get_order(self):
        #需要先登录
        self.test_login()
        response = self.session.get("http://localhost/Home/Order/order_list.html")
        print('响应体', response.text)

        # 断言
        self.assertIn("订单", response.text)

        pass



#