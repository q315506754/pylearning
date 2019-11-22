import socket

# Address
HOST = ''
PORT = 8000

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# http://localhost:8000

# infinite loop, server forever
while True:
    try:
        # 3: maximum number of requests waiting
        s.listen(30)
        conn, addr = s.accept()
        request    = conn.recv(1024).decode()
        method    = request.split(' ')[0]
        src            = request.split(' ')[1]

        # deal with GET method
        # if method == 'GET':
        # ULR
        # if src == '/test.jpg':
        #     content = pic_content
        # else: content = text_content.encode()

        print ('Connected by', addr)
        print ('Request is:', request)
        conn.sendall('HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\nsadsfsdfsdfsdfsd'.encode('utf-8'))
        # conn.sendmsg('aaaaaaaaaaaaaa'.encode('utf-8'))

        # close connection
        conn.close()
    except Exception as e:
        e.with_traceback(None)
        # print(e)
        pass
