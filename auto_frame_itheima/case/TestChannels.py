import unittest

from auto_frame_itheima.api.ChannelsAPI import Channels


class TestChannels(unittest.TestCase):

    #编写获取频道列表的测试函数
    # 1 无提交的测试数据 不需设置data
    # 2 调用API实现

    def test_get_channels(self):
        self.channels = Channels()
        response = self.channels.get_channels()

        # 断言判断
        self.assertEqual("ok", response.json().get("message"))