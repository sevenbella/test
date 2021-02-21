# 需求：根据id列表删除学院信息

# 0 导包
import requests

# 1 url
url = 'http://127.0.0.1:8000/api/departments/'

# 两要素 提交发送
myParam = {"$dep_id_list": "T01, T02, TO3"}
response = requests.delete(url, params=myParam)

response = requests.delete("http://127.0.0.1:8000/api/departments/?$dep_id_list = T01, T02, TO3")  # 该写法也可

# 处理响应
print("状态码：", response.status_code )
print("响应体：", response.text )


