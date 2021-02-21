import requests

from auto_frame_itheima import app


class Collections:

    def __init__(self):
        self.collections_url = app.BASE_URL+"app/v1_0/article/collections"

    def save(self, id, token):    # 收藏
        myJson = {"target":id}
        # 获取到token后提交
        myHeader = {"Content-Type": "application/json",
                    "Authorzation": "Bearer" + token}
        return requests.post(self.collections_url, json=myJson, headers=myHeader)

    def cancel(self, id, token):    # 取消收藏
        return requests.delete(self.collections_url + "/" + id, headers=myHeader)

