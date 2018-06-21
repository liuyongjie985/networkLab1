# coding:utf-8
from socket import *

HOST = "127.0.0.1"
TCP_PORT = 21567
UDP_PORT = 21568
BUFSIZE = 1024
TCP_ADDR = (HOST, TCP_PORT)
UDP_ADDR = (HOST, UDP_PORT)

# SOCK_STREAM是指用TCP方式连接

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(TCP_ADDR)

# SOCK_DGRAM是指用UDP方式连接

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:

    selected = raw_input("请选择你要使用的传输方式：1.TCP   2.UDP")
    try:
        if selected.strip() == "1":
            data = raw_input("请输入要传输的数据\n>")
            if not data:
                break
            tcpCliSock.send(data)
            # 用UDP接受数据
            # data, ADDR = udpCliSock.recvfrom(BUFSIZE)  # 接受数据
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            print data
        else:

            data = raw_input("请输入要传输的数据\n>")
            if not data:
                break
            udpCliSock.sendto(data, UDP_ADDR)  # 发送数据
            # 用tcp接收数据
            # data = tcpCliSock.recv(BUFSIZE)
            data, ADDR = udpCliSock.recvfrom(BUFSIZE)  # 接受数据
            if not data:
                break
            print  data

    except Exception, e:
        print 'Error: ', e

tcpCliSock.close()
udpCliSock.close()
