import requests

from auto_frame_itheima import app

class Channels:

    class Login:

        # 封装资源路径
        def __init__(self):
            self.channels_url = app.BASE_URL + "app/v1_0/channels"
    # 获取频道列表的函数
    def get_channels(self):
        response = requests.get(self.get_channels_url)
        return response

