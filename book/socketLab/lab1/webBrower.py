#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 6789
serverName = '127.0.0.1'
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
#Fill in end
while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        filecontent = f.read()
        f.close()
        outputdata = []
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        print(f"Client {addr} requested {filename}")
        print(">>> Sent 200 OK response")
        outputdata.append('HTTP/1.1 200 OK')
        outputdata.append('Content-Type: text/html')
        outputdata.append(f'Content-Length: {len(filecontent)}')
        outputdata.append('Connection: close')        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(filecontent.encode())
        connectionSocket.close()
    except IOError:
        print(f"Client {addr} requested {filename}, but file not found\r\n")
        print(">>> Sent 404 Not Found response\r\n")

        outputdata = []
        error_page = "<html><body><h1>404 Not Found</h1></body></html>"
        outputdata.append('HTTP/1.1 404 Not Found')
        outputdata.append('Content-Type: text/html; charset=utf-8')
        outputdata.append(f'Content-Length: {len(error_page)}')
        outputdata.append('Connection: close')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(error_page.encode())
        connectionSocket.close()
    #Send response message for file not found
    #Fill in start
    #Fill in end
    #Close client socket
    #Fill in start
    #Fill in end
        serverSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data 