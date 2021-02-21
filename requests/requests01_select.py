# 使用requests库访问学生关联系统的学院查询相关接口

# 0 导包
import requests

# 1 设置资源路径 请求方式
url = 'http://127.0.0.1:8000/api/departments/'

# 2 设置提交数据 两要素设计并发送

#查询所有，无提交内容
response = requests.get(url)

# 根据id列表查询学院信息，可以使用字典格式保存提交数据
Myparams = {"$dep_id_list": "T01, T02"}
response = requests.get(url, params=Myparams)

response = requests.get("http://127.0.0.1:8000/api/departments/?$dep_id_list = T01, T02")   # 该写法也可 不够优雅

# 3 查看响应结果
print('状态码', response.status_code)
print('响应体', response.text)



print('响应体', response.text)




