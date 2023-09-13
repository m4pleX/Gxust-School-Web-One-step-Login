import requests    # 用于向目标网站发送请求
import os
import json

with open('config.json') as f:
    config = json.load(f)

url = "http://172.16.1.11/drcom/login?callback=dr1003&DDDDD="+config['account']+"%40"+config['operator']+"&upass="+config['password']+"&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1.3&v=10163&lang=zh"
response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
print("状态码{}\ntips:可前往172.16.1.11查看是否登上了".format(response))  # 打印状态码
os.system("pause")
