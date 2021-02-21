import requests

from auto_frame.app import BASE_URL


class Login:

    # 封装资源路径
    def __init__(self):
        self.get_verity_code_url = BASE_URL+"app/v1_0/sms/codes/:mobile"
        self.Login_url = BASE_URL+"app/v1_0/authorizations"

    # 1. 获取验证码函数
    def get_verity_code(self,moblie):
        #发送requests请求
        return requests.get(self.get_verify_code_url+moblie)

    # 2. 登录函数
    def Login(self, mobile, code):
        myJson = {}
        if mobile:
            myJson["mobile"]=mobile
        if code:
            myJson["code"]=code
        return requests.post(self.Login_url, json=myJson)

