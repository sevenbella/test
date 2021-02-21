import unittest

from auto_frame_itheima import app
from auto_frame_itheima.api.ColletionsAPI import Collections


class TestColletions(unittest.TestCase):

    def setUp(self):
        self.colletions = Collections()
    # 测试收藏功能
    def test_save(self):


        # 1 服务器会为用户开辟存储空间
        # 2 用户访问自身存储空间需要使用标记 cookie or token
          # 实现收藏功能 （关联）
        # 1 从登陆响应的数据中提取token
        # 2 收藏时提交token到服务器

        # 传入收藏文章的id
        response = self.colletions.save(1, app.TOKEN)


        # 断言
        self.assertEqual("ok", response.json().get("message"))

        pass

    #测试取消收藏
    def test_cacel(self):
        response = self.collections.cancel("1", app.TOKEN)
        self.assertEqual(204, response.status_code)
