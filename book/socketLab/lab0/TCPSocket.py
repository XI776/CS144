from socket import *

serverName = '127.0.0.1'
serverPort = 12000
serverNumber = 37
numberLimit = 100

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("[SERVER] Server is ready to receive on", (serverName, serverPort))

while True:
    print("[SERVER] Waiting for connection...")
    connectionSocket, addr = serverSocket.accept()
    print("[SERVER] Connection accepted from", addr)

    message = connectionSocket.recv(1024).decode()

    # 用 split 分割
    parts = message.split('\n')
    clientName = parts[0]
    clientNumber = int(parts[1])

    print("[SERVER] Client name:", clientName)
    print("[SERVER] Client number:", clientNumber)
    print("[SERVER] Server number:", serverNumber)

    if clientNumber < 1 or clientNumber > numberLimit:
        print("[SERVER] Invalid number, closing connection.")
        connectionSocket.close()
        continue
    total = clientNumber + serverNumber
    print("[SERVER] Sum is", total)
    response = f"{clientName} {total}"
    sentence = clientName + ' ' + str(clientNumber)
    connectionSocket.send(sentence.encode())
    print("[SERVER] Sent response:", response)
    connectionSocket.close()
    print("[SERVER] Connection closed.\n")
