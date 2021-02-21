# 需求： 使用requests库调用TPshop登录功能的相关接口，完成登录操作，登录成功后获取‘我的订单’页面
# 相关接口：
# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify GET
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login POST
# 登录提交的参数: {"username":"xxxxx","password":"yyyy","verify_code":"zzzz"},非 JSON 提交
# 我的订单：http://localhost/Home/Order/order_list.html GET

# 0 导包
import requests

# 1 获取session对象      requests中提供session对象，该对象包含了cookie的提取组织与提交，简化cookie的应用
session = requests.session()

# 2 获取验证码
response1 = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response1.content)

# 3 登录
mydata = {"username":"13246758795","password":"tttangdo","verify_code":"666574"}
response2 = session.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=mydata)

print("状态码", response2.status_code)
print("响应体", response2.json())

# 4 获取订单
response3 = session.get("http://localhost/Home/Order/order_list.html")
print("状态码", response3.status_code)
print("响应体", response3.text)