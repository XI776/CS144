#import socket module
from socket import *
import sys
import threading

serverPort = 6789
serverName = '127.0.0.1'

def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            connectionSocket.close()
            return

        filename = message.split()[1]
        f = open(filename[1:])
        filecontent = f.read()
        f.close()

        # 构建响应头
        outputdata = []
        outputdata.append('HTTP/1.1 200 OK')
        outputdata.append('Content-Type: text/html; charset=utf-8')
        outputdata.append(f'Content-Length: {len(filecontent)}')
        outputdata.append('Connection: close')

        # 发送响应
        for line in outputdata:
            connectionSocket.send(line.encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())  # 空行
        connectionSocket.send(filecontent.encode())
        print(f"Client {addr} requested {filename} -> 200 OK")

    except IOError:
        # 文件未找到，返回 404
        error_page = "<html><body><h1>404 Not Found</h1></body></html>"
        outputdata = []
        outputdata.append('HTTP/1.1 404 Not Found')
        outputdata.append('Content-Type: text/html; charset=utf-8')
        outputdata.append(f'Content-Length: {len(error_page)}')
        outputdata.append('Connection: close')

        for line in outputdata:
            connectionSocket.send(line.encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(error_page.encode())
        print(f"Client {addr} requested {filename} -> 404 Not Found")

    finally:
        connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(5)   # 支持最多5个等待连接
    print(f"Server running on {serverName}:{serverPort}")

    while True:
        connectionSocket, addr = serverSocket.accept()
        # 每个客户端开一个线程
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
