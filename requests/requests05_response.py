# 使用requests库访问学生关联系统的学院查询相关接口

# 0 导包
import requests

# 1 设置资源路径 请求方式
url = 'http://127.0.0.1:8000/api/departments/'

# 2 设置提交数据 两要素设计并发送
#查询所有，无提交内容
response = requests.get(url)

# 3 查看响应结果
# response响应中的API调用：

# ----- 行 ------
print('url', response.url)
print('状态码', response.status_code)

# ------ 头 ------
print('响应头', response.headers)
print('指定响应头', response.headers.get("content-type"))
print('编码集', response.encoding)
print('获取cookie', response.cookies)

# ------ 体 ------
print('文本方式显示响应体', response.text)
print('二进制方式显示响应体', response.content)  #  获取图片或音频视频等非文本的二进制数据
print('将响应体数据解析为json格式', response.json().get("results"))   # 转化成json后可以调用json的解析函数

# 如果响应体为非Json数据，json()函数调用会抛出异常


