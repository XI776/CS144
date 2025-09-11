# UDPPingerClient.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

server_port = 12000
server_name = '127.0.0.1'
transferCnt, i = 10, 0
buffer_size = 1024
print('Client >> ')
maxRTT, minRTT, avgRTT = 0, 1, 0
lostNum = 0
while i < transferCnt:
    try:
        # message = f'Ping {i}'
        start = time.time()
        rand = random.randint(0, 10)
        if rand < 5:
            message = f'{i - 3} {start}'
        else:
            message = f'{i} {start}'

        # start = time.time()
        clientSocket.sendto(message.encode(), (server_name, server_port))
        data, server_address = clientSocket.recvfrom(buffer_size)
        # end = time.time()
        # seconds = end - start
        # if seconds < minRTT:
        #     minRTT = seconds
        # if seconds > maxRTT:
        #     maxRTT = seconds
        # avgRTT += seconds
        print(f'server response: {data.decode()}')
        # print(f'rtt = {seconds} seconds')
    except timeout:
        lostNum += 1
        print('Request timed out')
    i += 1
# print(f'maxRTT = {maxRTT} minRTT = {minRTT} avgRTT = {avgRTT}')
# print(f'packet loss rate = {lostNum / transferCnt * 100} %')



