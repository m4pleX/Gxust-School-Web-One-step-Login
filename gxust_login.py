import requests    # 用于向目标网站发送请求
import os

f = open("./config.txt", "r", encoding='utf-8')
user=f.readline()
password=f.readline()
op=f.readline()
f.close()

if not op[9:]:
    op=''
elif op[9:] == '移动':
    op='%40cmcc'
elif op[9:] == '联通':
    op='%40unicom'
elif op[9:] == '电信':
    op='%40telecom'
else:
    print("运营商填写错误，请查看文档来正确填写")
    os.system("pause")

url = 'http://172.16.1.11/drcom/login?callback=dr1003&DDDDD='+user[9:-1]+op+'&upass='+password[9:-1]+'&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1.3&v=10163&lang=zh'
response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
print("状态码{}".format(response))  # 打印状态码
os.system("pause")
