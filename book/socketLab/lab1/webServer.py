from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverName = '127.0.0.1'
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        # 从请求报文中解析文件名
        filename = message.split()[1][1:]  # 去掉前面的 '/'
        if filename == "":
            filename = "hello.html"  # 默认文件

        with open(filename, "r") as f:
            filecontent = f.read()
        
        print(">>> Request message from client:")
        print(message)
        # filecontent = 'Hello World'
        response_line = 'HTTP/1.1 200 OK\r\n'
        headers = f'Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(filecontent)}\r\nConnection: close\r\n\r\n'
        http_response = response_line + headers + filecontent

        connectionSocket.send(http_response.encode())
    except IOError:
        # 文件不存在 -> 返回404
        error_page = "<html><body><h1>404 Not Found</h1></body></html>"
        response_line = "HTTP/1.1 404 Not Found\r\n"
        headers = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(error_page)}\r\nConnection: close\r\n\r\n"
        http_response = response_line + headers + error_page
        connectionSocket.send(http_response.encode())

    connectionSocket.close()

