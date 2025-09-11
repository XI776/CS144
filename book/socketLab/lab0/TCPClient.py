from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
print("[CLIENT] Connecting to server...")
clientSocket.connect((serverName, serverPort))
print("[CLIENT] Connected to", (serverName, serverPort))

clientName = input("Enter your name: ")
clientNumber = input("Enter a number: ")

message = clientName + "\n" + clientNumber
print("[CLIENT] Sending message:", message)
clientSocket.send(message.encode())

print("[CLIENT] Waiting for reply...")
response = clientSocket.recv(1024).decode()
print("[CLIENT] Received from server:", response)

clientSocket.close()
print("[CLIENT] Connection closed.")
