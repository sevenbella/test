# 需求：修改id为3的学院信息

# 0 导包
import requests

# 1 URL
url = 'http://127.0.0.1:8000/api/departments/'

# 2 两要素 提交数据
myJson = {
                "data": [
                    {
                        "dep_id": "T03",
                        "dep_name": "C++/学院",
                        "master_name": "C++-Master",
                        "slogan": "Here is Slogan"
                    }
                ]
            }

response = requests.put(url, json=myJson)

# 3 处理响应
print('状态码', response.status_code)
print('响应体', response.text)

