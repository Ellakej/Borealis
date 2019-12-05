import socket
import os

s = socket.socket()
host = '192.168.1.14' #ip of raspberry pi
port = 8888
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Obteniendo conexion de',addr)
  c.send('Conexion a la Raspberry Pi Exitosa!')
  c.send(os.system('ls'))
  c.close()
