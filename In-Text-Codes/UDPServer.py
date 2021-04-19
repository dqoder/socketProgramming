#! python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('clientAddress: ', clientAddress)
    modifiedMessage = message.decode().upper()
    import time
    time.sleep(20)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
