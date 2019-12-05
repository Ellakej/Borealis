import socket

s = socket.socket()
host = '192.168.1.14'# ip of raspberry pi
port = 8888
s.connect((host, port))
print(s.recv(1024))
s.close()
