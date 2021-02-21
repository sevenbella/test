# 需求:测试购物车接口，但是需要先调用登录接口(登录实现比较复杂: 需要录入手机号码，以及服务器发送的验证码)
# 要求使用 mock模拟登录功能，最终无论录入什么样的手机号或验证码都能登录

# 导入unittets

import unittest
from unittest import mock

# 确定被模拟的接口
        # 登录函数
        #需要参数  手机号 验证码
        # 返回值 True False

def login(tel,verity_code):
        #验证手机号和服务器发送的验证码是否匹配，是返回True, 返回False
    return False

class TestLogin(unittest.TestCase):
    def test_cart(self):                      # 测试登录的函数
        login = mock.Mock(return_value=True)     # 创建mock服务
        result = login('11456', '999999')        # 调用Mock服务并先登录
        ...                                      # 之后测试购物车...

        print('登录结果', result)                # 断言  判断登录结果
        self.assertEqual(True, result)



