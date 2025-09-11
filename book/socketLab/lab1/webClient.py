import sys
from socket import *

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 webClient.py <server_ip> <server_port> <filename>")
        sys.exit(1)
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # 创建 TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_ip, server_port))
    # 2. 构造 HTTP GET 请求
    request_line = f'GET {filename} HTTP/1.1\r\n'
    headers = f'Host: {server_ip}:{server_port}\r\nConnection: close\r\n\r\n'
    http_request = request_line + headers
    # 3. 发送请求
    clientSocket.send(http_request.encode())
    # 4. 接收并打印响应
    response = ''
    data = clientSocket.recv(1024).decode()
    response += data
    
    print("---- Server Response ----")
    print(response)
    # print(response.decode(errors="ignore"))
    clientSocket.close()

if __name__ == "__main__":
    main()


