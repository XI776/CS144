import base64
from socket import *
import ssl
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com' #fill
server_port = 587
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
#Fill in end
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, server_port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO mycomputer\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')
# Send STARTTLS command
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)
if recv_tls[:3] != '220':
    print('220 reply not received from server after STARTTLS.')

# Upgrade the socket to SSL
clientSocket = ssl.wrap_socket(clientSocket)

# After STARTTLS, we must EHLO again
clientSocket.send(heloCommand.encode())
recv1b = clientSocket.recv(1024).decode()
print(recv1b)


# Authentication (AUTH LOGIN)
username = "sizumi675@gmail.com"
password = "lhmv rivp ewrl exqz"  # 注意：要用 Gmail 的 App Password，不是普通密码

authCommand = "AUTH LOGIN\r\n"
clientSocket.send(authCommand.encode())
print(clientSocket.recv(1024).decode())

clientSocket.send(base64.b64encode(username.encode()) + b"\r\n")
print(clientSocket.recv(1024).decode())

clientSocket.send(base64.b64encode(password.encode()) + b"\r\n")
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
# Fill in start
# MAIL FROM
mailFrom = 'MAIL FROM:<your_gmail@gmail.com>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# RCPT TO
rcptTo = 'RCPT TO:<3157941570@qq.com>\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# DATA
clientSocket.send('DATA\r\n'.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send message data
message = "Subject: Test mail\r\n\r\n" + msg
clientSocket.send(message.encode())

# End message with period
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# QUIT
clientSocket.send('QUIT\r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)