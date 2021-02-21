# 需求：添加新的学院信息

# 0 导包
import requests

# 1 URL
url = 'http://127.0.0.1:8000/api/departments/'

# 2 两要素 提交数据
myJson = {
			"data": [
					{
						"dep_id":"T01",
						"dep_name":"Test学院",
						"master_name":"Test-Master",
						"slogan":"Here is Slogan"
					}
				]
			}

response = requests.post(url, json=myJson)     # post提交的数据可以是Json(json=xxx),也可以是键值对（date=xxx)

# 3 处理响应
print('状态码', response.status_code)
print('响应体', response.text)

