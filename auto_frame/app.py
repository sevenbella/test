# 封装程序中使用的常量
import os

BASE_URL = "http://localhost/"

# 获取资源绝对路径
ABS_PATH = os.path.abspath(_file_)
print(ABS_PATH)
BASE_PATH = os.path.dirname(ABS_PATH)
print(BASE_PATH)
