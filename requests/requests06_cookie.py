# 需求： 使用requests库调用TPshop登录功能的相关接口，完成登录操作，登录成功后获取‘我的订单’页面
# 相关接口：
# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify GET
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login POST
# 登录提交的参数: {"username":"xxxxx","password":"yyyy","verify_code":"zzzz"},非 JSON 提交
# 我的订单：http://localhost/Home/Order/order_list.html GET

# 0 导包
import requests

# 1 获取验证码  -- 服务器产生了session 并返回了cookie
response1 = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response1.content)

#   如何获取提交cookie？

# A. 从第一次响应中提取cookie
print("响应回的cookie", response1.cookies)

# 获取cookie的值
cookie_value = response1.cookies.get("PHPSESSID")

# B 第二次访问时提交cookie

# 2 登录  -- 需要提交cookie
mydata = {"username":"13246758795","password":"tttangdo","verify_code":"666574"}

cookie = {"PHPSESSID":cookie_value}

response2 = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=mydata, cookies=cookie)
print("状态码", response2.status_code)
print("响应体", response2.json())


# 3 查看订单
response3 = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookie)
print("状态码", response3.status_code)
print("响应体", response3.json())

