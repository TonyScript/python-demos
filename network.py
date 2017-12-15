# -*- coding: UTF-8 -*-
import socket

# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接，参数是一个 tuple 类型,包含地址和端口号
s.connect(('www.sina.com.cn', 80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收响应
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接
s.close()
# 打印响应头并将响应结果作为文件保存
header, html = data.split(b'\r\n\r\n',1)
print (header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)
