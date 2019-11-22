import socket

# Address
HOST = 'localhost'
PORT = 8000

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('GET /favicon.ico HTTP/1.1\r\nPragma: no-cache\r\n\r\n'.encode('utf-8'))  # 发消息

# http://localhost:8000
str = s.recv(1024).decode()
print(str)
