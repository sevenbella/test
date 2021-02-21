# 组织测试套件 先登录 然后再取消收藏
# 需要先修改Testcase中文件读取路径，使用绝对路径

# 导入 unittes

import unittest

# 创建suit对象
from auto_frame_itheima.case import TestColletions
from auto_frame_itheima.case.TestLogin import TestLogin

suite = unittest.TestSuite()

# suite添加被执行函数
suite.addTest(TestLogin("Test_Login_sucsess"))
suite.addTest(TestColletions("Test_cacel"))

# 执行suite
unittest.TextTestRunner().run(suite)